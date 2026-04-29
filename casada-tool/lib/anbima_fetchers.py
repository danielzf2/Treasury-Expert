"""Fetchers ANBIMA: PU oficial de TPFs (TXT) + VNA D0 (Brasil Indicadores).

Duas fontes oficiais sem token:

1. ANBIMA TXT: https://www.anbima.com.br/informacoes/merc-sec/arqs/ms{YYMMDD}.txt
   - PU, taxa indicativa/compra/venda, intervalos D0/D+1
   - Defasagem: D-1 util (publicado apos 18h)
   - Formato: latin-1, separador @, decimal com virgula

2. VNA Brasil Indicadores: https://brasilindicadores.com.br/titulos-publicos/vna/
   - VNA D0 da NTN-B (com IPCA pro-rata projetado), NTN-C, LFT
   - Defasagem: D0 (publicado pela manha)
   - Formato: HTML (scraping)

Codigos SELIC:
- 100000: LTN
- 210100: LFT
- 760199: NTN-B
- 770100: NTN-C
- 950199: NTN-F

Cache em memoria com TTL configuravel.
"""

from __future__ import annotations

import re
import time
import urllib.request
import urllib.error
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta


CACHE_TTL_SECONDS = 1800  # 30 min — feed eh D-1, nao precisa hit frequente

# Codigos SELIC do feed ANBIMA
SELIC_CODE_TO_INSTRUMENT = {
    "100000": "LTN",
    "210100": "LFT",
    "760199": "NTN-B",
    "770100": "NTN-C",
    "950199": "NTN-F",
}


@dataclass
class _CacheEntry:
    data: object
    timestamp: float


_cache: dict[str, _CacheEntry] = {}


def clear_cache() -> None:
    """Limpa cache de todos os fetchers ANBIMA."""
    _cache.clear()


# ============================================================================
# Helpers
# ============================================================================

def _parse_br_decimal(s: str) -> float:
    """'14,2656' -> 14.2656; '976,984714' -> 976.984714; '4.687,318378' -> 4687.318378."""
    s = s.strip()
    if not s:
        return 0.0
    # Remove separadores de milhar (ponto antes da virgula) e troca virgula por ponto
    s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return 0.0


def _parse_yyyymmdd(s: str) -> date | None:
    s = s.strip()
    if len(s) != 8 or not s.isdigit():
        return None
    try:
        return date(int(s[:4]), int(s[4:6]), int(s[6:8]))
    except ValueError:
        return None


def _parse_ddmmyyyy(s: str) -> date | None:
    s = s.strip()
    parts = s.split("/")
    if len(parts) != 3:
        return None
    try:
        return date(int(parts[2]), int(parts[1]), int(parts[0]))
    except ValueError:
        return None


def _previous_business_days(d: date, n: int) -> list[date]:
    """Lista os ultimos N dias uteis ate d, decrescente. Reusa calendario lib."""
    from .calendar import is_du

    out: list[date] = []
    cur = d
    while len(out) < n and cur > date(2020, 1, 1):
        if is_du(cur):
            out.append(cur)
        cur -= timedelta(days=1)
    return out


def _http_get(url: str, timeout: int = 10, headers: dict | None = None) -> bytes | None:
    """GET retornando bytes ou None se falhar (sem raise)."""
    req = urllib.request.Request(url)
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return None


# ============================================================================
# 1. ANBIMA TXT — TPF mercado secundario
# ============================================================================

@dataclass
class TPFRecord:
    """Registro de um titulo no feed ANBIMA TXT."""
    instrument: str          # LTN, LFT, NTN-B, NTN-C, NTN-F
    selic_code: str          # 100000, 210100, etc.
    data_ref: date           # data referencia (D-1 util)
    data_emissao: date | None
    data_vencimento: date
    tx_compra: float         # % a.a.
    tx_venda: float          # % a.a.
    tx_indicativa: float     # % a.a.
    pu: float                # PU em R$ (T-6 ANBIMA)
    desvio_padrao: float
    intervalo_d0_inf: float
    intervalo_d0_sup: float
    intervalo_d1_inf: float
    intervalo_d1_sup: float
    criterio: str            # 'Calculado' | 'Apurado'

    def to_dict(self) -> dict:
        return {
            "instrument": self.instrument,
            "selic_code": self.selic_code,
            "data_ref": self.data_ref.strftime("%Y-%m-%d"),
            "data_emissao": self.data_emissao.strftime("%Y-%m-%d") if self.data_emissao else None,
            "data_vencimento": self.data_vencimento.strftime("%Y-%m-%d"),
            "tx_compra": self.tx_compra,
            "tx_venda": self.tx_venda,
            "tx_indicativa": self.tx_indicativa,
            "pu": self.pu,
            "desvio_padrao": self.desvio_padrao,
            "intervalo_d0_inf": self.intervalo_d0_inf,
            "intervalo_d0_sup": self.intervalo_d0_sup,
            "intervalo_d1_inf": self.intervalo_d1_inf,
            "intervalo_d1_sup": self.intervalo_d1_sup,
            "criterio": self.criterio,
        }


def parse_anbima_tpf_txt(content: str) -> list[TPFRecord]:
    """Parse do feed ANBIMA TXT. Aceita string ja decodificada.

    Layout esperado (pula primeiras 2 linhas - cabecalho + nomes de colunas):
    Titulo@DataRef@CodSELIC@DataEmissao@DataVcto@TxCompra@TxVenda@TxIndic@PU@Desv@D0Inf@D0Sup@D1Inf@D1Sup@Criterio
    """
    records: list[TPFRecord] = []
    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line or "@" not in line:
            continue
        if line.startswith("Titulo@") or line.startswith("ANBIMA"):
            continue

        parts = line.split("@")
        if len(parts) < 15:
            continue
        try:
            instr = parts[0].strip().upper()
            # Normaliza nome do instrumento (NTN-B Princ vira NTN-B Princ)
            if instr not in ("LTN", "LFT", "NTN-B", "NTN-C", "NTN-F", "NTN-B PRINC"):
                continue
            data_ref = _parse_yyyymmdd(parts[1])
            data_emissao = _parse_yyyymmdd(parts[3])
            data_vcto = _parse_yyyymmdd(parts[4])
            if not data_ref or not data_vcto:
                continue
            rec = TPFRecord(
                instrument=instr,
                selic_code=parts[2].strip(),
                data_ref=data_ref,
                data_emissao=data_emissao,
                data_vencimento=data_vcto,
                tx_compra=_parse_br_decimal(parts[5]),
                tx_venda=_parse_br_decimal(parts[6]),
                tx_indicativa=_parse_br_decimal(parts[7]),
                pu=_parse_br_decimal(parts[8]),
                desvio_padrao=_parse_br_decimal(parts[9]),
                intervalo_d0_inf=_parse_br_decimal(parts[10]),
                intervalo_d0_sup=_parse_br_decimal(parts[11]),
                intervalo_d1_inf=_parse_br_decimal(parts[12]),
                intervalo_d1_sup=_parse_br_decimal(parts[13]),
                criterio=parts[14].strip(),
            )
            records.append(rec)
        except (IndexError, ValueError):
            continue
    return records


def _anbima_tpf_url(d: date) -> str:
    return f"https://www.anbima.com.br/informacoes/merc-sec/arqs/ms{d.strftime('%y%m%d')}.txt"


def fetch_anbima_tpf_txt(reference_date: date | None = None,
                          fallback_lookback: int = 7) -> list[TPFRecord]:
    """Busca o feed ANBIMA TXT mais recente.

    Args:
        reference_date: data alvo. Default = ontem util. Se feed nao existir,
                        tenta ate `fallback_lookback` dias uteis anteriores.
        fallback_lookback: numero de dias uteis para tentar.

    Returns:
        Lista de TPFRecord. Vazia se nao conseguir buscar nenhum dia.
    """
    from .calendar import is_du

    today = reference_date or date.today()
    # Comecar pelo dia anterior se hoje (feed eh D-1)
    if reference_date is None:
        # Usar D-1 util
        d = today - timedelta(days=1)
        while not is_du(d):
            d -= timedelta(days=1)
        candidates = _previous_business_days(d, fallback_lookback)
    else:
        candidates = _previous_business_days(reference_date, fallback_lookback)

    for d in candidates:
        cache_key = f"anbima_tpf_{d.isoformat()}"
        now = time.time()
        if cache_key in _cache and (now - _cache[cache_key].timestamp) < CACHE_TTL_SECONDS:
            return _cache[cache_key].data

        url = _anbima_tpf_url(d)
        body = _http_get(url, timeout=12)
        if not body:
            continue
        try:
            text = body.decode("latin-1")
        except Exception:
            continue
        records = parse_anbima_tpf_txt(text)
        if records:
            _cache[cache_key] = _CacheEntry(records, now)
            return records

    return []


# ============================================================================
# 2. VNA Brasil Indicadores
# ============================================================================

@dataclass
class VNARecord:
    """VNA D0 de um titulo indexado."""
    instrument: str          # LFT, NTN-B, NTN-C
    selic_code: str
    data_ref: date           # data de referencia
    vna: float               # valor em R$
    indice_str: str          # ex: '0,67% (indice projetado)' ou '14,65%'
    data_atualizacao: date | None

    def to_dict(self) -> dict:
        return {
            "instrument": self.instrument,
            "selic_code": self.selic_code,
            "data_ref": self.data_ref.strftime("%Y-%m-%d"),
            "vna": self.vna,
            "indice_str": self.indice_str,
            "data_atualizacao": self.data_atualizacao.strftime("%Y-%m-%d") if self.data_atualizacao else None,
        }


# Mapping de codigos no Brasil Indicadores para nossos instrumentos
_VNA_CODE_MAP = {
    "210100": "LFT",
    "760199": "NTN-B",
    "770100": "NTN-C",
}

# Regex flexivel: captura linha de codigo SELIC + data + valor + indice.
# data_atualizacao eh opcional (LFT tem 4 tds, NTN-B/NTN-C tem 5).
_VNA_ROW_RE = re.compile(
    r"<td>\s*(?P<code>\d{6})\s*</td>\s*"
    r"<td>\s*(?P<data_ref>\d{2}/\d{2}/\d{4})\s*</td>\s*"
    r"<td>\s*R\$\s*(?P<vna>[\d.,]+)\s*</td>\s*"
    r"<td>\s*(?P<indice>[^<]*)\s*</td>"
    r"(?:\s*<td>\s*(?P<data_atu>\d{2}/\d{2}/\d{4})\s*</td>)?",
    re.IGNORECASE,
)


def parse_vna_brasil_indicadores(html: str) -> list[VNARecord]:
    """Parse do HTML de Brasil Indicadores VNA. Aceita string com tags."""
    records: list[VNARecord] = []
    for m in _VNA_ROW_RE.finditer(html):
        code = m.group("code")
        if code not in _VNA_CODE_MAP:
            continue
        data_ref = _parse_ddmmyyyy(m.group("data_ref"))
        if not data_ref:
            continue
        data_atu_str = m.group("data_atu")
        records.append(VNARecord(
            instrument=_VNA_CODE_MAP[code],
            selic_code=code,
            data_ref=data_ref,
            vna=_parse_br_decimal(m.group("vna")),
            indice_str=m.group("indice").strip(),
            data_atualizacao=_parse_ddmmyyyy(data_atu_str) if data_atu_str else None,
        ))
    return records


def fetch_vna_brasil_indicadores() -> list[VNARecord]:
    """Busca VNA D0 do Brasil Indicadores (cache 30min).

    Returns:
        Lista com VNA das 3 series principais (LFT, NTN-B, NTN-C).
        Vazia se falhar.
    """
    cache_key = "vna_brasil_indicadores"
    now = time.time()
    if cache_key in _cache and (now - _cache[cache_key].timestamp) < CACHE_TTL_SECONDS:
        return _cache[cache_key].data

    body = _http_get(
        "https://brasilindicadores.com.br/titulos-publicos/vna/",
        timeout=12,
        headers={"User-Agent": "Mozilla/5.0 (compatible; TreasuryExpert/1.0)"},
    )
    if not body:
        return []
    try:
        html = body.decode("utf-8")
    except UnicodeDecodeError:
        html = body.decode("latin-1", errors="ignore")

    records = parse_vna_brasil_indicadores(html)
    if records:
        _cache[cache_key] = _CacheEntry(records, now)
    return records


def get_vna_ntnb() -> float | None:
    """Atalho: VNA D0 da NTN-B (None se nao disponivel)."""
    records = fetch_vna_brasil_indicadores()
    for r in records:
        if r.instrument == "NTN-B":
            return r.vna
    return None


def get_vna_lft() -> float | None:
    """Atalho: VNA D0 da LFT/Selic (None se nao disponivel)."""
    records = fetch_vna_brasil_indicadores()
    for r in records:
        if r.instrument == "LFT":
            return r.vna
    return None


# ============================================================================
# 3. Helpers de uso
# ============================================================================

def get_anbima_tpf_grouped() -> dict[str, list[TPFRecord]]:
    """Agrupa TPFs do feed por instrumento."""
    out: dict[str, list[TPFRecord]] = {
        "LTN": [], "LFT": [], "NTN-B": [], "NTN-C": [], "NTN-F": [],
    }
    for r in fetch_anbima_tpf_txt():
        if r.instrument in out:
            out[r.instrument].append(r)
    for k in out:
        out[k].sort(key=lambda x: x.data_vencimento)
    return out


def get_anbima_tpf_vencimentos(instrument: str) -> list[str]:
    """Lista de vencimentos disponiveis no feed ANBIMA para um instrumento.

    Returns:
        Lista de strings YYYY-MM-DD ordenada.
        Se feed nao disponivel, retorna [].
    """
    grouped = get_anbima_tpf_grouped()
    return [r.data_vencimento.strftime("%Y-%m-%d") for r in grouped.get(instrument, [])]


# ============================================================================
# 3. ETTJ ANBIMA — Estrutura a Termo de Taxas de Juros
# ============================================================================

ETTJ_URL = "https://www.anbima.com.br/informacoes/est-termo/CZ-down.asp"


@dataclass
class ETTJVertex:
    """Vertice da ETTJ ANBIMA."""
    du: int             # dias uteis
    taxa_ipca: float | None   # % a.a. IPCA (cupom real)
    taxa_pre: float | None    # % a.a. Pre
    inflacao_implicita: float | None  # % a.a. breakeven


@dataclass
class ETTJData:
    """Dados completos da ETTJ ANBIMA."""
    data_ref: date | None
    nss_pre: dict  # {beta1, beta2, beta3, beta4, lambda1, lambda2}
    nss_ipca: dict
    vertices: list[ETTJVertex]
    vertices_pre_3361: list[tuple[int, float]]  # verts Circular 3361


def parse_ettj(content: str) -> ETTJData:
    """Parse do arquivo CZ-down.asp da ANBIMA (encoding latin-1, separador ;).

    Layout:
      Linha 1: DD/MM/YYYY;Beta 1;Beta 2;...
      Linha 2: PREFIXADOS;b1;b2;b3;b4;l1;l2
      Linha 3: IPCA;b1;b2;b3;b4;l1;l2
      Linha 4: (vazia)
      Linha 5: ETTJ Inflacao Implicita (IPCA)
      Linha 6: Vertices;ETTJ IPCA;ETTJ PREF;Inflacao Implicita
      Linhas seguintes: du;ipca;pre;breakeven (ou du;ipca;; se pre nao disponivel)
      (vazia)
      PREFIXADOS (CIRCULAR 3.361)
      Vertices;Taxa (%a.a.)
      du;taxa
      ...
    """
    lines = content.strip().splitlines()
    if not lines:
        return ETTJData(None, {}, {}, [], [])

    # Linha 1: data
    first_parts = lines[0].split(";")
    data_ref = _parse_ddmmyyyy(first_parts[0]) if first_parts else None

    # NSS params
    nss_pre = {}
    nss_ipca = {}
    for line in lines[1:4]:
        parts = line.split(";")
        if len(parts) < 7:
            continue
        label = parts[0].strip().upper()
        try:
            params = {
                "beta1": float(parts[1].replace(",", ".")),
                "beta2": float(parts[2].replace(",", ".")),
                "beta3": float(parts[3].replace(",", ".")),
                "beta4": float(parts[4].replace(",", ".")),
                "lambda1": float(parts[5].replace(",", ".")),
                "lambda2": float(parts[6].replace(",", ".")),
            }
        except (ValueError, IndexError):
            continue
        if "PREFIXADO" in label:
            nss_pre = params
        elif "IPCA" in label:
            nss_ipca = params

    # Vertices ETTJ
    vertices: list[ETTJVertex] = []
    in_vertices = False
    in_3361 = False
    verts_3361: list[tuple[int, float]] = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            in_vertices = False
            continue

        if "Vertices;ETTJ IPCA" in stripped:
            in_vertices = True
            continue

        if "CIRCULAR 3.361" in stripped.upper():
            in_vertices = False
            in_3361 = True
            continue

        if in_3361 and "Vertices;Taxa" in stripped:
            continue

        if "Erro" in stripped and "Titulo" in stripped:
            in_3361 = False
            continue

        if in_vertices:
            parts = stripped.split(";")
            if len(parts) < 2:
                continue
            try:
                du = int(parts[0].replace(".", "").strip())
                ipca = _parse_br_decimal(parts[1]) if parts[1].strip() else None
                pre = _parse_br_decimal(parts[2]) if len(parts) > 2 and parts[2].strip() else None
                infl = _parse_br_decimal(parts[3]) if len(parts) > 3 and parts[3].strip() else None
                vertices.append(ETTJVertex(du=du, taxa_ipca=ipca, taxa_pre=pre, inflacao_implicita=infl))
            except (ValueError, IndexError):
                continue

        if in_3361:
            parts = stripped.split(";")
            if len(parts) >= 2:
                try:
                    du = int(parts[0].replace(".", "").strip())
                    taxa = _parse_br_decimal(parts[1])
                    verts_3361.append((du, taxa))
                except (ValueError, IndexError):
                    pass

    return ETTJData(
        data_ref=data_ref,
        nss_pre=nss_pre,
        nss_ipca=nss_ipca,
        vertices=vertices,
        vertices_pre_3361=verts_3361,
    )


def fetch_ettj() -> ETTJData:
    """Busca ETTJ ANBIMA (cache 30min). Retorna ETTJData.

    Fonte: https://www.anbima.com.br/informacoes/est-termo/CZ-down.asp
    Publicado D-1 util apos 18h. Formato latin-1, separador ;.
    """
    cache_key = "anbima_ettj"
    now = time.time()
    if cache_key in _cache and (now - _cache[cache_key].timestamp) < CACHE_TTL_SECONDS:
        return _cache[cache_key].data

    body = _http_get(ETTJ_URL, timeout=12,
                     headers={"User-Agent": "Mozilla/5.0 (compatible; TreasuryExpert/1.0)"})
    if not body:
        return ETTJData(None, {}, {}, [], [])

    try:
        text = body.decode("latin-1")
    except UnicodeDecodeError:
        text = body.decode("utf-8", errors="ignore")

    data = parse_ettj(text)
    if data.vertices:
        _cache[cache_key] = _CacheEntry(data, now)
    return data


def get_ettj_pre_vertices() -> list[tuple[int, float]]:
    """Vertices da curva Pre ANBIMA como (du, taxa_aa %). Fallback pra curva B3 quando vazia."""
    ettj = fetch_ettj()
    return [(v.du, v.taxa_pre) for v in ettj.vertices if v.taxa_pre is not None]


def get_ettj_ipca_vertices() -> list[tuple[int, float]]:
    """Vertices da curva IPCA (real) ANBIMA como (du, taxa_aa %)."""
    ettj = fetch_ettj()
    return [(v.du, v.taxa_ipca) for v in ettj.vertices if v.taxa_ipca is not None]


def get_ettj_breakeven_vertices() -> list[tuple[int, float]]:
    """Inflacao implicita (breakeven) ANBIMA como (du, taxa_aa %)."""
    ettj = fetch_ettj()
    return [(v.du, v.inflacao_implicita) for v in ettj.vertices if v.inflacao_implicita is not None]


def find_anbima_tpf(instrument: str, vencimento: date) -> TPFRecord | None:
    """Encontra o registro ANBIMA pra um TPF (instrumento + vencimento)."""
    for r in fetch_anbima_tpf_txt():
        if r.instrument == instrument and r.data_vencimento == vencimento:
            return r
    return None
