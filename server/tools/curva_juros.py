"""
Ferramentas MCP para curva de juros: interpolação flat forward, forwards implícitos,
PU a partir de taxa spot e referência rápida de convenções (base 252, capitalização exponencial).
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _dec_from_pct(taxa_aa: float) -> float:
    """Converte taxa em % a.a. para taxa decimal (12,5 → 0,125)."""
    return taxa_aa / 100.0


def _pct_from_dec(i: float) -> float:
    """Converte taxa decimal para % a.a."""
    return i * 100.0


def _sep_int_br(n: int) -> str:
    """Parte inteira com separador de milhar (ponto), sem sinal."""
    n = abs(int(n))
    s = str(n)
    parts: list[str] = []
    for idx, ch in enumerate(reversed(s)):
        if idx and idx % 3 == 0:
            parts.append(".")
        parts.append(ch)
    return "".join(reversed(parts))


def _fmt_br_float(x: float, frac_digits: int = 4) -> str:
    """Formata número no padrão brasileiro (milhar com ponto, decimal com vírgula)."""
    neg = x < 0
    x = abs(float(x))
    scale = 10**frac_digits
    ip = int(x)
    fp = round((x - ip) * scale)
    if fp >= scale:
        ip += 1
        fp -= int(scale)
    int_str = _sep_int_br(ip)
    frac_str = str(int(fp)).zfill(frac_digits)
    out = f"{int_str},{frac_str}"
    return f"-{out}" if neg else out


def _md_table(headers: tuple[str, ...], rows: list[tuple[str, str]]) -> str:
    h0, h1 = headers
    lines = [
        f"| {h0} | {h1} |",
        "|---|---|",
    ]
    for a, b in rows:
        lines.append(f"| {a} | {b} |")
    return "\n".join(lines)


def _section(title: str, body: str) -> str:
    return f"## {title}\n\n{body.strip()}\n"


def interpolar_flat_forward(
    taxa1_aa: float,
    du1: int,
    taxa2_aa: float,
    du2: int,
    du_alvo: int,
) -> str:
    """
    Interpola taxa spot na hipótese de forward constante (flat forward) entre dois vértices,
    com capitalização exponencial e base 252 dias úteis.

    Retorna texto com premissas, cálculo passo a passo e resultado (forward implícito e taxa interpolada).
    """
    i1 = _dec_from_pct(taxa1_aa)
    i2 = _dec_from_pct(taxa2_aa)
    prem = _md_table(
        ("Parâmetro", "Valor"),
        [
            ("Taxa no vértice 1 (i₁)", f"{_fmt_br_float(taxa1_aa, 6)}% a.a."),
            ("DU vértice 1 (du₁)", str(du1)),
            ("Taxa no vértice 2 (i₂)", f"{_fmt_br_float(taxa2_aa, 6)}% a.a."),
            ("DU vértice 2 (du₂)", str(du2)),
            ("DU alvo (du_alvo)", str(du_alvo)),
            ("Base", "252 du"),
            ("Capitalização", "exponencial: fator (1 + i)^(du/252)"),
        ],
    )

    if du2 <= du1:
        body = (
            "Para definir um forward único entre os vértices, é necessário **du₂ > du₁**.\n\n"
            f"Recebido: du₁ = {du1}, du₂ = {du2}."
        )
        return "\n\n".join([_section("Premissas", prem), _section("Cálculo (passo a passo)", body)])

    if du_alvo <= 0:
        body = (
            "Com **du_alvo ≤ 0**, a convenção (1 + i)^(du_alvo/252) não permite inferir uma taxa spot "
            "única de forma estável (expoente nulo torna o fator igual a 1, independente de i).\n\n"
            "Use **du_alvo > 0**."
        )
        return "\n\n".join([_section("Premissas", prem), _section("Cálculo (passo a passo)", body)])

    delta = du2 - du1
    fator1 = math.pow(1.0 + i1, du1 / 252.0)
    fator2 = math.pow(1.0 + i2, du2 / 252.0)
    ratio = fator2 / fator1
    fwd = math.pow(ratio, 252.0 / delta) - 1.0

    fator_alvo = fator1 * math.pow(1.0 + fwd, (du_alvo - du1) / 252.0)
    i_alvo = math.pow(fator_alvo, 252.0 / du_alvo) - 1.0
    taxa_alvo_aa = _pct_from_dec(i_alvo)

    calc = "\n".join(
        [
            "**Passo 1 — fatores de desconto/capitalização nos vértices**",
            "",
            f"F₁ = (1 + i₁)^(du₁/252) = (1 + {_fmt_br_float(taxa1_aa, 6)}/100)^({du1}/252) = {_fmt_br_float(fator1, 8)}",
            f"F₂ = (1 + i₂)^(du₂/252) = (1 + {_fmt_br_float(taxa2_aa, 6)}/100)^({du2}/252) = {_fmt_br_float(fator2, 8)}",
            "",
            "**Passo 2 — forward flat entre du₁ e du₂**",
            "",
            "Relação:",
            "",
            "```",
            "(1 + fwd)^((du₂ - du₁)/252) = F₂ / F₁",
            "```",
            "",
            f"Razão F₂/F₁ = {_fmt_br_float(ratio, 8)}",
            f"Expoente aplicado na inversão: 252/(du₂ - du₁) = 252/{delta}",
            "",
            f"fwd = (F₂/F₁)^(252/(du₂ - du₁)) - 1 = {_fmt_br_float(fwd, 8)} (decimal)",
            f"**Taxa forward (flat) = {_fmt_br_float(_pct_from_dec(fwd), 6)}% a.a.**",
            "",
            "**Passo 3 — taxa spot interpolada em du_alvo**",
            "",
            "Relação:",
            "",
            "```",
            "(1 + i_alvo)^(du_alvo/252) = F₁ × (1 + fwd)^((du_alvo - du₁)/252)",
            "```",
            "",
            f"F_alvo = F₁ × (1 + fwd)^((du_alvo - du₁)/252) = {_fmt_br_float(fator_alvo, 8)}",
            f"i_alvo = F_alvo^(252/du_alvo) - 1 = {_fmt_br_float(i_alvo, 8)} (decimal)",
            f"**Taxa spot interpolada = {_fmt_br_float(taxa_alvo_aa, 6)}% a.a.**",
        ]
    )

    res = _md_table(
        ("Métrica", "Valor"),
        [
            ("Forward flat (du₁→du₂)", f"{_fmt_br_float(_pct_from_dec(fwd), 6)}% a.a."),
            ("Taxa spot em du_alvo", f"{_fmt_br_float(taxa_alvo_aa, 6)}% a.a."),
            ("fwd (decimal)", _fmt_br_float(fwd, 8)),
            ("i_alvo (decimal)", _fmt_br_float(i_alvo, 8)),
        ],
    )

    return "\n\n".join(
        [
            _section("Premissas", prem),
            _section("Cálculo (passo a passo)", calc),
            _section("Resultado", res),
        ]
    )


def calcular_forward(
    taxa_curta_aa: float,
    du_curto: int,
    taxa_longa_aa: float,
    du_longo: int,
) -> str:
    """
    Calcula a taxa forward implícita entre dois vértices da curva, na convenção exponencial base 252.

    Usa (1 + fwd)^((du_longo - du_curto)/252) = (1 + i_longo)^(du_longo/252) / (1 + i_curto)^(du_curto/252).
    """
    i_c = _dec_from_pct(taxa_curta_aa)
    i_l = _dec_from_pct(taxa_longa_aa)
    prem = _md_table(
        ("Parâmetro", "Valor"),
        [
            ("Taxa no prazo curto", f"{_fmt_br_float(taxa_curta_aa, 6)}% a.a."),
            ("DU curto", str(du_curto)),
            ("Taxa no prazo longo", f"{_fmt_br_float(taxa_longa_aa, 6)}% a.a."),
            ("DU longo", str(du_longo)),
            ("Base", "252 du"),
        ],
    )

    if du_longo <= du_curto:
        body = (
            "É necessário **DU longo > DU curto** para definir o forward no intervalo.\n\n"
            f"Recebido: DU curto = {du_curto}, DU longo = {du_longo}."
        )
        return "\n\n".join([_section("Premissas", prem), _section("Cálculo (passo a passo)", body)])

    delta = du_longo - du_curto
    fc = math.pow(1.0 + i_c, du_curto / 252.0)
    fl = math.pow(1.0 + i_l, du_longo / 252.0)
    ratio = fl / fc
    fwd = math.pow(ratio, 252.0 / delta) - 1.0
    fwd_aa = _pct_from_dec(fwd)

    calc = "\n".join(
        [
            "**Passo 1 — fatores nos dois vértices**",
            "",
            f"F_curto = (1 + i_curto)^(DU_curto/252) = {_fmt_br_float(fc, 8)}",
            f"F_longo = (1 + i_longo)^(DU_longo/252) = {_fmt_br_float(fl, 8)}",
            "",
            "**Passo 2 — forward implícito**",
            "",
            "```",
            "(1 + fwd)^((DU_longo - DU_curto)/252) = F_longo / F_curto",
            "```",
            "",
            f"Razão = {_fmt_br_float(ratio, 8)}",
            f"fwd = (Razão)^(252/(DU_longo - DU_curto)) - 1",
            f"fwd (decimal) = {_fmt_br_float(fwd, 8)}",
            f"**Taxa forward = {_fmt_br_float(fwd_aa, 6)}% a.a.**",
        ]
    )

    res = _md_table(
        ("Métrica", "Valor"),
        [
            ("Período forward (DU)", str(delta)),
            ("Taxa forward implícita", f"{_fmt_br_float(fwd_aa, 6)}% a.a."),
            ("fwd (decimal)", _fmt_br_float(fwd, 8)),
        ],
    )

    return "\n\n".join(
        [
            _section("Premissas", prem),
            _section("Cálculo (passo a passo)", calc),
            _section("Resultado", res),
        ]
    )


def taxa_spot_para_pu(taxa_aa: float, du: int, vf: float = 100_000.0) -> str:
    """
    Converte taxa spot (em % a.a., base 252, exponencial) em PU dado valor de face VF.

    PU = VF / (1 + taxa/100)^(du/252). Também mostra a reconstrução da taxa a partir do PU.
    """
    prem = _md_table(
        ("Parâmetro", "Valor"),
        [
            ("Taxa spot (entrada)", f"{_fmt_br_float(taxa_aa, 6)}% a.a."),
            ("DU", str(du)),
            ("VF (valor de face)", f"BRL {_fmt_br_float(vf, 2)}"),
            ("Base", "252 du"),
        ],
    )

    if du < 0:
        body = "**DU** não pode ser negativo nesta convenção de precificação."
        return "\n\n".join([_section("Premissas", prem), _section("Cálculo (passo a passo)", body)])

    if vf <= 0:
        body = "**VF** deve ser positivo."
        return "\n\n".join([_section("Premissas", prem), _section("Cálculo (passo a passo)", body)])

    if du == 0:
        pu = vf
        calc = "\n".join(
            [
                "**Passo 1 — caso DU = 0**",
                "",
                "Sem prazo útil, não há desconto composto nessa etapa:",
                "",
                "```",
                "PU = VF",
                "```",
                "",
                f"PU = {_fmt_br_float(pu, 2)}",
                "",
                "**Passo 2 — taxa implícita a partir do PU (DU = 0)**",
                "",
                "Com DU = 0, a taxa spot não fica identificada apenas por PU = VF (há degeneração da convenção).",
            ]
        )
        res = _md_table(
            ("Métrica", "Valor"),
            [
                ("PU", f"BRL {_fmt_br_float(pu, 2)}"),
                ("Taxa implícita a partir do PU", "indeterminada com DU = 0"),
            ],
        )
        return "\n\n".join(
            [
                _section("Premissas", prem),
                _section("Cálculo (passo a passo)", calc),
                _section("Resultado", res),
            ]
        )

    r = _dec_from_pct(taxa_aa)
    fator = math.pow(1.0 + r, du / 252.0)
    pu = vf / fator
    taxa_de_volta = _pct_from_dec(math.pow(vf / pu, 252.0 / du) - 1.0)

    calc = "\n".join(
        [
            "**Passo 1 — fator de capitalização**",
            "",
            "```",
            "fator = (1 + taxa/100)^(DU/252)",
            "```",
            "",
            f"fator = (1 + {_fmt_br_float(taxa_aa, 6)}/100)^({du}/252) = {_fmt_br_float(fator, 8)}",
            "",
            "**Passo 2 — PU**",
            "",
            "```",
            "PU = VF / fator",
            "```",
            "",
            f"PU = {_fmt_br_float(vf, 2)} / {_fmt_br_float(fator, 8)} = {_fmt_br_float(pu, 8)}",
            "",
            "**Passo 3 — volta da taxa a partir do PU (verificação)**",
            "",
            "```",
            "taxa = 100 × ((VF/PU)^(252/DU) - 1)",
            "```",
            "",
            f"taxa reconstruída = {_fmt_br_float(taxa_de_volta, 6)}% a.a.",
        ]
    )

    res = _md_table(
        ("Métrica", "Valor"),
        [
            ("PU", _fmt_br_float(pu, 8)),
            ("PU (financeiro, se VF em BRL)", f"BRL {_fmt_br_float(pu, 2)}"),
            ("Taxa de entrada", f"{_fmt_br_float(taxa_aa, 6)}% a.a."),
            ("Taxa obtida de volta pelo PU", f"{_fmt_br_float(taxa_de_volta, 6)}% a.a."),
        ],
    )

    return "\n\n".join(
        [
            _section("Premissas", prem),
            _section("Cálculo (passo a passo)", calc),
            _section("Resultado", res),
        ]
    )


def ref_curva_juros() -> str:
    """
    Referência rápida: flat forward, interpolação linear de taxa, bootstrapping e convenções (252, exponencial).
    """
    body = "\n".join(
        [
            "### Flat forward (forward constante entre dois vértices)",
            "",
            "Entre **du₁** e **du₂**, existe uma taxa forward **fwd** (decimal) tal que:",
            "",
            "```",
            "(1 + fwd)^((du₂ - du₁)/252) = (1 + i₂)^(du₂/252) / (1 + i₁)^(du₁/252)",
            "```",
            "",
            "Interpolação do spot em **du_alvo** (na mesma hipótese):",
            "",
            "```",
            "(1 + i_alvo)^(du_alvo/252) = (1 + i₁)^(du₁/252) × (1 + fwd)^((du_alvo - du₁)/252)",
            "```",
            "",
            "- **i₁, i₂, i_alvo** em decimal; na prática costuma-se digitar **% a.a.** e dividir por 100.",
            "",
            "### Interpolação linear (taxa)",
            "",
            "Entre vértices (du₁, y₁) e (du₂, y₂), com **y** na mesma unidade (por exemplo, % a.a.):",
            "",
            "```",
            "y(du) = y₁ + (du - du₁) × (y₂ - y₁) / (du₂ - du₁)",
            "```",
            "",
            "Útil como aproximação rápida; **não** implica, em geral, consistência de forwards com capitalização exponencial.",
            "",
            "### Bootstrapping (ideia)",
            "",
            "Construir a curva spot/zero a partir de preços observados (ou taxas de instrumentos líquidos), resolvendo vértice a vértice:",
            "",
            "1. Precifica o mais curto com o menor número de incógnitas.",
            "2. Para cada instrumento seguinte, usa-se a curva já obtida nos fluxos anteriores e isola-se a taxa (ou fator) do novo vértice.",
            "",
            "Em títulos com múltiplos fluxos, o preço do título vincula uma equação envolvendo vários fatores; o bootstrapping **encadeia** essas soluções em ordem de vencimento.",
            "",
            "### Convenções usadas nestas ferramentas",
            "",
            _md_table(
                ("Item", "Convenção"),
                [
                    ("Dia-count / prazo", "dias úteis (DU), base **252**"),
                    ("Capitalização", "**exponencial**: fatores `(1 + i)^(DU/252)`"),
                    ("Taxa informada", "**percentual**: 12,5 significa 12,5% a.a. → i = 0,125"),
                    ("PU a partir de spot", "`PU = VF / (1 + taxa/100)^(DU/252)`"),
                ],
            ),
        ]
    )

    prem = _md_table(
        ("Tipo", "Conteúdo"),
        [
            ("Objetivo", "Cola operacional para curva: fórmulas e convenções"),
            ("Uso", "Checagem rápida de hipóteses (flat forward vs linear) e lembrete de bootstrap"),
        ],
    )

    return "\n\n".join(
        [
            _section("Premissas", prem),
            _section("Cálculo (passo a passo)", body),
            _section(
                "Resultado",
                "Referência entregue em texto estruturado acima (sem parâmetros numéricos de mercado).",
            ),
        ]
    )


def register(mcp: FastMCP) -> None:
    """Registra as ferramentas de curva de juros no servidor FastMCP."""

    mcp.tool()(interpolar_flat_forward)
    mcp.tool()(calcular_forward)
    mcp.tool()(taxa_spot_para_pu)
    mcp.tool()(ref_curva_juros)
