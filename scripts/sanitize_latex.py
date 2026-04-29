"""Limpa residuos de LaTeX malformado em arquivos .md gerados por OCR.

Mistral OCR as vezes embute equacoes em delimitadores torcidos
($$...$$, \(...\), $...$) com formatacao incompleta. Este script normaliza
a saida pra deixar o markdown mais legivel e indexavel pelo BM25.

Heuristicas aplicadas (idempotentes):
1. Remove fences vazios ou com whitespace puro.
2. Normaliza $$...$$ multilinha pra blocos com newline antes/depois.
3. Substitui \\backslash literal por \\.
4. Remove caracteres invisiveis comuns do OCR (zero-width, BOM).
5. Colapsa espacos triplos.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

INVISIBLE = "\u200b\u200c\u200d\ufeff\u00a0"


def sanitize(text: str) -> str:
    # remove caracteres invisiveis
    for ch in INVISIBLE:
        text = text.replace(ch, " " if ch == "\u00a0" else "")

    # remove $$...$$ vazios
    text = re.sub(r"\$\$\s*\$\$", "", text)
    # remove $...$ vazios
    text = re.sub(r"\$\s*\$", "", text)
    # remove \(...\) vazios
    text = re.sub(r"\\\(\s*\\\)", "", text)

    # normaliza $$ display blocks: garante newline antes e depois
    def _normalize_display(m):
        body = m.group(1).strip()
        if not body:
            return ""
        return f"\n\n$$\n{body}\n$$\n\n"

    text = re.sub(r"\$\$([^$]+?)\$\$", _normalize_display, text, flags=re.DOTALL)

    # \\backslash literal -> \\
    text = text.replace("\\\\backslash", "\\")

    # colapsa multiplas linhas em branco
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    # colapsa espacos triplos
    text = re.sub(r"   +", "  ", text)

    return text.strip() + "\n"


def main():
    if len(sys.argv) < 2:
        print("uso: sanitize_latex.py <arquivo.md> [<arquivo2.md> ...]")
        sys.exit(1)

    for path_str in sys.argv[1:]:
        p = Path(path_str)
        if not p.exists():
            print(f"[skip] {p}: nao existe")
            continue
        text = p.read_text(encoding="utf-8")
        cleaned = sanitize(text)
        if cleaned != text:
            p.write_text(cleaned, encoding="utf-8")
            print(f"[ok] {p}")
        else:
            print(f"[unchanged] {p}")


if __name__ == "__main__":
    main()
