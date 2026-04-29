"""
Treasury Docs MCP Server
Servidor MCP custom com busca BM25, expansão de sinônimos e indexação por seção.
Suporta transporte stdio (local) e HTTP Streamable (remoto).
"""

import logging
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from rank_bm25 import BM25Okapi
from fastmcp import FastMCP

sys.path.insert(0, str(Path(__file__).resolve().parent))
from synonyms import SYNONYM_GROUPS, TOPIC_TAXONOMY, build_synonym_lookup

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
log = logging.getLogger("treasury-mcp")

DOCS_DIR = Path(os.environ.get("DOCS_DIR", "")).resolve() if os.environ.get("DOCS_DIR") else (
    Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "docs"
)
SNIPPET_LEN = 600
MIN_SECTION_CHARS = 80
MAX_SECTION_CHARS = 3000

# ── Texto ─────────────────────────────────────────────────────────────────────

_PT_STOPWORDS = {
    "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "um", "uma", "uns", "umas", "ao", "aos", "por", "para", "com",
    "se", "ou", "que", "como", "mais", "mas", "sua", "seu", "seus",
    "suas", "este", "esta", "esse", "essa", "isso", "isto", "entre",
    "sobre", "ate", "ser", "ter", "foi", "sao", "tem", "pode", "deve",
    "cada", "pelo", "pela", "pelos", "pelas", "quando", "onde",
    "the", "and", "for", "with", "from", "that", "this", "are", "was",
}


def normalize_text(text: str) -> str:
    text = text.lower()
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c))


def tokenize(text: str) -> list[str]:
    text = normalize_text(text)
    tokens = re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text)
    return [t for t in tokens if len(t) > 1 and t not in _PT_STOPWORDS]


# ── Modelo de dados ───────────────────────────────────────────────────────────

@dataclass
class Section:
    doc_path: str
    doc_title: str
    section_title: str
    content: str
    tokens: list[str] = field(default_factory=list)


@dataclass
class Document:
    path: str
    title: str
    frontmatter: dict
    raw_content: str
    sections: list[Section] = field(default_factory=list)


# ── Índice ────────────────────────────────────────────────────────────────────

class TreasuryIndex:
    def __init__(self, docs_dir: Path):
        self.docs_dir = docs_dir
        self.documents: dict[str, Document] = {}
        self.sections: list[Section] = []
        self.bm25: BM25Okapi | None = None
        self._synonym_lookup = build_synonym_lookup()
        self._file_mtimes: dict[str, float] = {}
        self._rebuild()

    # ── construção ────────────────────────────────────────────────────

    def _rebuild(self):
        self.documents.clear()
        self.sections.clear()
        self.bm25 = None

        if not self.docs_dir.exists():
            log.warning("Docs directory not found: %s", self.docs_dir)
            return

        md_files = sorted(self.docs_dir.rglob("*.md"))
        if not md_files:
            log.warning("No markdown files found in %s", self.docs_dir)
            return

        for md_path in md_files:
            rel = str(md_path.relative_to(self.docs_dir))
            self._file_mtimes[rel] = md_path.stat().st_mtime
            try:
                raw = md_path.read_text(encoding="utf-8")
            except Exception:
                log.exception("Failed to read %s", md_path)
                continue

            frontmatter, body = self._split_frontmatter(raw)
            title = frontmatter.get("title", md_path.stem.replace("-", " ").title())
            doc = Document(path=rel, title=title, frontmatter=frontmatter, raw_content=body)
            doc.sections = self._parse_sections(rel, title, body)
            self.documents[rel] = doc
            self.sections.extend(doc.sections)

        if self.sections:
            for sec in self.sections:
                sec.tokens = tokenize(sec.content + " " + sec.section_title)
            corpus = [sec.tokens for sec in self.sections]
            self.bm25 = BM25Okapi(corpus)

        log.info(
            "Indexed %d documents, %d sections",
            len(self.documents),
            len(self.sections),
        )

    def _check_rebuild(self):
        """Reconstrói se algum arquivo mudou desde a última indexação."""
        if not self.docs_dir.exists():
            return
        current: dict[str, float] = {}
        for md_path in self.docs_dir.rglob("*.md"):
            rel = str(md_path.relative_to(self.docs_dir))
            current[rel] = md_path.stat().st_mtime
        if current != self._file_mtimes:
            log.info("Files changed — rebuilding index")
            self._rebuild()

    # ── parsing ───────────────────────────────────────────────────────

    @staticmethod
    def _split_frontmatter(raw: str) -> tuple[dict, str]:
        fm: dict = {}
        body = raw
        if raw.startswith("---"):
            parts = raw.split("---", 2)
            if len(parts) >= 3:
                for line in parts[1].strip().splitlines():
                    if ":" in line:
                        k, v = line.split(":", 1)
                        fm[k.strip()] = v.strip().strip('"').strip("'")
                body = parts[2]
        return fm, body

    @staticmethod
    def _split_long_section(rel_path: str, doc_title: str, title: str, content: str) -> list[Section]:
        """Divide seções que excedem MAX_SECTION_CHARS em sub-chunks por parágrafo."""
        if len(content) <= MAX_SECTION_CHARS:
            return [Section(doc_path=rel_path, doc_title=doc_title, section_title=title, content=content)]

        paragraphs = content.split("\n\n")
        chunks: list[Section] = []
        buf: list[str] = []
        buf_len = 0
        part = 1

        for para in paragraphs:
            para_len = len(para)
            if buf and buf_len + para_len > MAX_SECTION_CHARS:
                chunk_title = f"{title} (parte {part})" if part > 1 or para_len > 0 else title
                chunks.append(Section(
                    doc_path=rel_path, doc_title=doc_title,
                    section_title=chunk_title,
                    content="\n\n".join(buf).strip(),
                ))
                buf = []
                buf_len = 0
                part += 1
            buf.append(para)
            buf_len += para_len

        if buf:
            chunk_title = f"{title} (parte {part})" if part > 1 else title
            text = "\n\n".join(buf).strip()
            if len(text) >= MIN_SECTION_CHARS:
                chunks.append(Section(
                    doc_path=rel_path, doc_title=doc_title,
                    section_title=chunk_title, content=text,
                ))

        return chunks if chunks else [Section(doc_path=rel_path, doc_title=doc_title, section_title=title, content=content)]

    @staticmethod
    def _parse_sections(rel_path: str, doc_title: str, body: str) -> list[Section]:
        raw_sections: list[tuple[str, str]] = []
        current_title = "Introdução"
        current_lines: list[str] = []

        for line in body.split("\n"):
            header_match = re.match(r"^(#{1,4})\s+(.+)$", line)
            if header_match:
                content = "\n".join(current_lines).strip()
                if len(content) >= MIN_SECTION_CHARS:
                    raw_sections.append((current_title, content))
                current_title = header_match.group(2).strip()
                current_lines = []
            else:
                current_lines.append(line)

        content = "\n".join(current_lines).strip()
        if len(content) >= MIN_SECTION_CHARS:
            raw_sections.append((current_title, content))

        if not raw_sections and body.strip():
            raw_sections.append(("Conteúdo", body.strip()))

        sections: list[Section] = []
        for title, text in raw_sections:
            sections.extend(TreasuryIndex._split_long_section(rel_path, doc_title, title, text))

        return sections

    # ── busca ─────────────────────────────────────────────────────────

    def _expand_query(self, query: str) -> str:
        query_norm = normalize_text(query)
        query_tokens = set(tokenize(query))
        expanded_parts = [query]
        matched: set[int] = set()

        for i, group in enumerate(SYNONYM_GROUPS):
            for alias in group:
                alias_norm = normalize_text(alias)
                if len(alias_norm) >= 3 and (
                    alias_norm in query_norm or query_norm in alias_norm
                ):
                    expanded_parts.extend(group)
                    matched.add(i)
                    break

        if not matched:
            significant = {t for t in query_tokens if len(t) >= 3}
            for i, group in enumerate(SYNONYM_GROUPS):
                if i in matched:
                    continue
                group_tokens: set[str] = set()
                for alias in group:
                    group_tokens.update(tokenize(alias))
                if significant & group_tokens:
                    expanded_parts.extend(group)
                    matched.add(i)

        return " ".join(expanded_parts)

    def search(self, query: str, top_k: int = 10) -> list[dict]:
        self._check_rebuild()
        if not self.bm25 or not self.sections:
            return []

        expanded = self._expand_query(query)
        tokens = tokenize(expanded)
        if not tokens:
            return []

        scores = self.bm25.get_scores(tokens)
        ranked = np.argsort(scores)[::-1][:top_k]

        results = []
        for idx in ranked:
            score = float(scores[idx])
            if score <= 0:
                break
            sec = self.sections[idx]
            snippet = self._smart_snippet(sec.content, tokens)
            results.append({
                "document": sec.doc_path,
                "doc_title": sec.doc_title,
                "section": sec.section_title,
                "score": round(score, 2),
                "snippet": snippet,
            })
        return results

    @staticmethod
    def _smart_snippet(content: str, query_tokens: list[str]) -> str:
        """Extrai snippet centrado na região com maior concentração de tokens do query."""
        if len(content) <= SNIPPET_LEN:
            return content

        content_lower = normalize_text(content)
        best_pos = 0
        best_count = 0

        for i in range(0, len(content_lower) - 100, 50):
            window = content_lower[i:i + SNIPPET_LEN]
            count = sum(1 for t in query_tokens if t in window)
            if count > best_count:
                best_count = count
                best_pos = i

        start = max(0, best_pos)
        end = min(len(content), start + SNIPPET_LEN)
        snippet = content[start:end]

        prefix = "..." if start > 0 else ""
        suffix = "..." if end < len(content) else ""
        return prefix + snippet + suffix

    # ── leitura ───────────────────────────────────────────────────────

    def read_document(self, path: str) -> str | None:
        self._check_rebuild()
        doc = self.documents.get(path)
        return doc.raw_content if doc else None

    def read_section(self, path: str, section_title: str) -> str | None:
        self._check_rebuild()
        doc = self.documents.get(path)
        if not doc:
            return None
        section_norm = normalize_text(section_title)
        for sec in doc.sections:
            if normalize_text(sec.section_title) == section_norm:
                return sec.content
        for sec in doc.sections:
            if section_norm in normalize_text(sec.section_title):
                return sec.content
        return None

    def list_documents(self) -> list[dict]:
        self._check_rebuild()
        result = []
        for path, doc in sorted(self.documents.items()):
            result.append({
                "path": path,
                "title": doc.title,
                "sections": len(doc.sections),
                "frontmatter": doc.frontmatter,
            })
        return result

    def list_sections(self, path: str) -> list[str] | None:
        self._check_rebuild()
        doc = self.documents.get(path)
        if not doc:
            return None
        return [sec.section_title for sec in doc.sections]

    def glossary(self, term: str) -> dict:
        term_norm = normalize_text(term)
        synonyms = self._synonym_lookup.get(term_norm)

        if not synonyms:
            term_tokens = set(tokenize(term))
            for key, group in self._synonym_lookup.items():
                key_tokens = set(tokenize(key))
                if term_tokens & key_tokens and len(term_tokens & key_tokens) > 0:
                    synonyms = group
                    break

        if not synonyms:
            return {"term": term, "found": False, "suggestion": "Termo não encontrado. Tente variações."}

        related_docs = []
        if self.bm25 and self.sections:
            tokens = tokenize(" ".join(synonyms))
            scores = self.bm25.get_scores(tokens)
            top_idx = np.argsort(scores)[::-1][:5]
            seen_docs: set[str] = set()
            for idx in top_idx:
                if scores[idx] <= 0:
                    break
                sec = self.sections[idx]
                if sec.doc_path not in seen_docs:
                    related_docs.append({
                        "document": sec.doc_path,
                        "section": sec.section_title,
                    })
                    seen_docs.add(sec.doc_path)

        topics = []
        for category, subtopics in TOPIC_TAXONOMY.items():
            for subtopic, terms in subtopics.items():
                for t in terms:
                    if normalize_text(t) in [normalize_text(s) for s in synonyms]:
                        topics.append(f"{category} > {subtopic}")
                        break

        return {
            "term": term,
            "found": True,
            "synonyms": synonyms,
            "topics": topics,
            "related_documents": related_docs,
        }


# ── MCP Server ────────────────────────────────────────────────────────────────

mcp = FastMCP("treasury-expert-dzf")
index: TreasuryIndex | None = None


def get_index() -> TreasuryIndex:
    global index
    if index is None:
        log.info("Initializing index from %s", DOCS_DIR)
        index = TreasuryIndex(DOCS_DIR)
    return index


# ── Registrar módulos de cálculo (server/tools/) ─────────────────────────────

from tools import (
    titulos_publicos, curva_juros,
    futuros_di, futuros_dol, futuros_dap, futuros_frc,
    swaps, cambio, risco, opcoes,
    conversoes_taxas, calculo_financeiro, convencoes,
    dias_uteis, inflacao_implicita, cambio_produtos,
    risco_mercado, credito_privado, estrategias,
)

_calc_modules = [
    titulos_publicos, curva_juros,
    futuros_di, futuros_dol, futuros_dap, futuros_frc,
    swaps, cambio, risco, opcoes,
    conversoes_taxas, calculo_financeiro, convencoes,
    dias_uteis, inflacao_implicita, cambio_produtos,
    risco_mercado, credito_privado, estrategias,
]

for _mod in _calc_modules:
    _mod.register(mcp)
    log.info("Registered tools from %s", _mod.__name__)


# ── Health Check (disponível apenas no transporte HTTP) ───────────────────────

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    from starlette.responses import JSONResponse
    idx = get_index()
    return JSONResponse({
        "status": "healthy",
        "documents": len(idx.documents),
        "sections": len(idx.sections),
    })


@mcp.tool()
def search(query: str, top_k: int = 10) -> str:
    """Busca documentos de tesouraria por relevância (BM25 + sinônimos).
    Retorna seções ranqueadas com snippets. Use para encontrar conteúdo
    sobre qualquer tema: renda fixa, derivativos, precificação, risco, etc.
    """
    results = get_index().search(query, top_k=top_k)
    if not results:
        return "Nenhum resultado encontrado para: " + query

    lines = [f"Resultados para: '{query}' ({len(results)} encontrados)\n"]
    for i, r in enumerate(results, 1):
        lines.append(
            f"[{i}] {r['document']} > {r['section']}  (score: {r['score']})\n"
            f"    Documento: {r['doc_title']}\n"
            f"    ---\n"
            f"    {r['snippet']}\n"
        )
    return "\n".join(lines)


@mcp.tool()
def read_document(path: str) -> str:
    """Lê o conteúdo completo de um documento markdown.
    Use o path retornado por list_documents ou search (ex: 'books/mercado-renda-fixa.md').
    """
    content = get_index().read_document(path)
    if content is None:
        available = [d["path"] for d in get_index().list_documents()]
        return f"Documento não encontrado: {path}\nDisponíveis: {', '.join(available)}"
    return content


@mcp.tool()
def read_section(path: str, section: str) -> str:
    """Lê uma seção específica de um documento.
    Use path do documento e título da seção (obtido via list_sections ou search).
    """
    content = get_index().read_section(path, section)
    if content is None:
        sections = get_index().list_sections(path)
        if sections is None:
            return f"Documento não encontrado: {path}"
        return (
            f"Seção '{section}' não encontrada em {path}.\n"
            f"Seções disponíveis:\n" + "\n".join(f"  - {s}" for s in sections)
        )
    return content


@mcp.tool()
def list_documents() -> str:
    """Lista todos os documentos disponíveis na base de conhecimento,
    com título, número de seções e metadados.
    """
    docs = get_index().list_documents()
    if not docs:
        return "Nenhum documento encontrado na base."

    lines = [f"Base de conhecimento: {len(docs)} documentos\n"]
    for d in docs:
        lines.append(
            f"  {d['path']}\n"
            f"    Título: {d['title']}\n"
            f"    Seções: {d['sections']}\n"
        )
    return "\n".join(lines)


@mcp.tool()
def list_sections(path: str) -> str:
    """Lista todas as seções (índice/sumário) de um documento específico.
    Use para navegar o conteúdo antes de ler uma seção.
    """
    sections = get_index().list_sections(path)
    if sections is None:
        return f"Documento não encontrado: {path}"
    lines = [f"Seções de {path} ({len(sections)} total):\n"]
    for i, s in enumerate(sections, 1):
        lines.append(f"  {i}. {s}")
    return "\n".join(lines)


@mcp.tool()
def glossary(term: str) -> str:
    """Consulta o glossário de tesouraria. Retorna sinônimos, tópicos
    relacionados e documentos que cobrem o termo.
    """
    result = get_index().glossary(term)
    if not result["found"]:
        return f"Termo '{term}' não encontrado no glossário. Tente variações ou sinônimos."

    lines = [
        f"Termo: {term}",
        f"Sinônimos: {', '.join(result['synonyms'])}",
    ]
    if result["topics"]:
        lines.append(f"Tópicos: {', '.join(result['topics'])}")
    if result["related_documents"]:
        lines.append("Documentos relacionados:")
        for rd in result["related_documents"]:
            lines.append(f"  - {rd['document']} > {rd['section']}")
    return "\n".join(lines)


@mcp.tool()
def list_topics() -> str:
    """Lista a taxonomia completa de tópicos de tesouraria.
    Útil para explorar a base de conhecimento por área temática.
    """
    lines = ["Taxonomia de Tópicos de Tesouraria\n"]
    for category, subtopics in TOPIC_TAXONOMY.items():
        lines.append(f"  {category}")
        for subtopic, terms in subtopics.items():
            lines.append(f"    {subtopic}: {', '.join(terms)}")
    return "\n".join(lines)


# ── Entrypoint ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    transport = os.environ.get("TRANSPORT", "http")
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))

    log.info("Starting Treasury Docs MCP Server (docs: %s, transport: %s)", DOCS_DIR, transport)
    get_index()

    if transport == "stdio":
        mcp.run()
    else:
        mcp.run(transport="http", host=host, port=port, stateless_http=True)
