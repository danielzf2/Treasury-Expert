"""Exposicao economica, deteccao de estrategia, fatores de risco e sugestao de hedge."""

from __future__ import annotations
from .instruments import INSTRUMENTS, duration, dv01


def get_exposure(instrumento: str, direcao: str, taxa: float) -> dict:
    """Retorna ativo/passivo economico de uma perna.

    Compra LTN    → Ativo: Pre X%,     Passivo: —
    Compra DI1    → Ativo: CDI,        Passivo: Pre Y%
    Compra DOL    → Ativo: DOL cotacao, Passivo: —
    Compra DDI    → Ativo: CDI,        Passivo: CupSujo X%
    Compra FRC    → Ativo: CDI,        Passivo: CupLimpo X%
    Compra DAP    → Ativo: IPCA,       Passivo: IPCA+ Y%
    """
    info = INSTRUMENTS[instrumento]
    rs = f"{taxa:.3f}%"

    if info.conv == "price":
        cotacao = f"DOL {taxa:.1f}"
        return {"ativo": cotacao, "passivo": "—"} if direcao == "C" else {"ativo": "—", "passivo": cotacao}

    if info.type == "tpf":
        val = f"{info.benchmark} {rs}"
        return {"ativo": val, "passivo": "—"} if direcao == "C" else {"ativo": "—", "passivo": val}

    if info.type == "cupom":
        val = f"{info.benchmark} {rs}"
        return {"ativo": "CDI", "passivo": val} if direcao == "C" else {"ativo": val, "passivo": "CDI"}

    # Swap equivalente do livro B3:
    # - DI1 comprado: ativo CDI, passivo Pre (livro Mercado Renda Fixa 14.2.1)
    # - DAP comprado: ativo CDI/DI Over, passivo IPCA + cupom (livro DAP, Swap Equivalente):
    #   "o comprador do DAP fica ativo em DI Over e passivo em IPCA + Cupom"
    if instrumento == "DAP":
        pay_bm = "IPCA+"
        rec_bm = "CDI"  # DI Over conforme swap equivalente do livro DAP B3
    else:  # DI1
        pay_bm = "Pre"
        rec_bm = "CDI"
    val = f"{pay_bm} {rs}"
    return {"ativo": rec_bm, "passivo": val} if direcao == "C" else {"ativo": val, "passivo": rec_bm}


# ---------------------------------------------------------------------------
# Motor generico de exposicoes
# ---------------------------------------------------------------------------

# Fatores reconhecidos e regras de equivalencia
_FACTOR_EQUIVALENCES = {"Selic+": "CDI"}  # Selic ~= CDI para cancelamento


def _parse_exposure_entry(side_str: str) -> list[dict]:
    """Converte string ativo/passivo em lista de {factor, rate}.

    Exemplos:
      'CDI'             -> [{'factor': 'CDI', 'rate': None}]
      'Pre 13.650%'     -> [{'factor': 'Pre', 'rate': 13.65}]
      'IPCA+ 7.400%'    -> [{'factor': 'IPCA+', 'rate': 7.40}]
      'CupLimpo 5.060%' -> [{'factor': 'CupLimpo', 'rate': 5.06}]
      'DOL 4976.5'      -> [{'factor': 'USD', 'rate': 4976.5}]
      '—'               -> []
    """
    s = side_str.strip()
    if not s or s == "—":
        return []

    if s.startswith("DOL"):
        parts = s.split()
        rate = float(parts[1]) if len(parts) > 1 else 0.0
        return [{"factor": "USD", "rate": rate}]

    parts = s.split()
    if len(parts) == 1:
        factor = _FACTOR_EQUIVALENCES.get(parts[0], parts[0])
        return [{"factor": factor, "rate": None}]

    factor = parts[0]
    rate_str = parts[1].replace("%", "").strip()
    try:
        rate = float(rate_str)
    except ValueError:
        rate = None
    factor = _FACTOR_EQUIVALENCES.get(factor, factor)
    return [{"factor": factor, "rate": rate}]


def compute_net_exposure(legs: list[dict]) -> dict:
    """Soma exposicoes de todas as pernas e cancela fatores iguais.

    Para cada perna:
    1. Chama get_exposure(instrumento, direcao, taxa) -> {ativo, passivo}
    2. Parseia cada lado em entries {factor, rate}
    3. Acumula em bags: bags[factor]["ativo"] e bags[factor]["passivo"]

    Cancelamento:
    - Se um fator aparece em AMBOS os lados (ativo e passivo), cancela.
    - Se ambos tem taxa explicita, spread = soma_ativo - soma_passivo (em %).
    - Se taxa eh implicita (CDI puro), cancela zerado.
    - Fatores sem contraparte ficam como exposicao residual.

    Retorna dict com:
      entries: lista de todas as entries brutas
      bags: {factor: {ativo: [{rate, leg_label}], passivo: [...]}}
      cancelled: [{factor, ativo_total, passivo_total, spread_pct}]
      residual: [{factor, side, rate_total, direction}]
      result_label: string concisa (ex: 'CDI +11 bps')
      result_description: explicacao de 1-2 linhas
    """
    bags: dict[str, dict[str, list]] = {}
    all_entries: list[dict] = []

    for leg in legs:
        inst = leg["instrument"]
        direction = leg["direction"]
        taxa = leg.get("tax_fin", leg.get("taxa", 0))
        label = f"{direction} {inst} {leg.get('parsed', {}).get('label', leg.get('parsed_label', ''))}"

        exp = get_exposure(inst, direction, taxa)

        for side in ("ativo", "passivo"):
            entries = _parse_exposure_entry(exp.get(side, "—"))
            for e in entries:
                factor = e["factor"]
                if factor not in bags:
                    bags[factor] = {"ativo": [], "passivo": []}
                bags[factor][side].append({
                    "rate": e["rate"],
                    "leg_label": label,
                    "instrument": inst,
                })
                all_entries.append({**e, "side": side, "leg_label": label})

    cancelled: list[dict] = []
    residual: list[dict] = []

    for factor, sides in bags.items():
        has_ativo = len(sides["ativo"]) > 0
        has_passivo = len(sides["passivo"]) > 0

        if has_ativo and has_passivo:
            ativo_rates = [e["rate"] for e in sides["ativo"] if e["rate"] is not None]
            passivo_rates = [e["rate"] for e in sides["passivo"] if e["rate"] is not None]

            if ativo_rates and passivo_rates:
                spread = sum(ativo_rates) - sum(passivo_rates)
            else:
                spread = 0.0

            ativo_legs = [e["leg_label"] for e in sides["ativo"]]
            passivo_legs = [e["leg_label"] for e in sides["passivo"]]
            cancelled.append({
                "factor": factor,
                "ativo_total": sum(ativo_rates) if ativo_rates else None,
                "passivo_total": sum(passivo_rates) if passivo_rates else None,
                "spread_pct": spread,
                "spread_bps": round(spread * 100, 2) if spread else 0.0,
                "ativo_legs": ativo_legs,
                "passivo_legs": passivo_legs,
            })
        else:
            side = "ativo" if has_ativo else "passivo"
            entries = sides[side]
            rates = [e["rate"] for e in entries if e["rate"] is not None]
            rate_total = sum(rates) if rates else None
            leg_labels = [e["leg_label"] for e in entries]
            direction = "recebe" if side == "ativo" else "paga"
            residual.append({
                "factor": factor,
                "side": side,
                "rate_total": rate_total,
                "direction": direction,
                "legs": leg_labels,
            })

    result_label = _build_result_label(cancelled, residual)
    result_description = _build_result_description(cancelled, residual)

    return {
        "entries": all_entries,
        "bags": {f: {s: [dict(e) for e in es] for s, es in sv.items()} for f, sv in bags.items()},
        "cancelled": cancelled,
        "residual": residual,
        "result_label": result_label,
        "result_description": result_description,
    }


def _build_result_label(cancelled: list[dict], residual: list[dict]) -> str:
    """Gera label concisa tipo 'CDI +11 bps' ou 'IPCA+ 7.50% + USD direcional'."""
    parts: list[str] = []

    # Fatores cancelados com spread
    for c in cancelled:
        if c["factor"] == "CDI":
            continue  # CDI puro cancelando nao gera label proprio
        if c["spread_bps"]:
            parts.append(f"{c['factor']} cancela (spread {c['spread_bps']:+.0f} bps)")

    # CDI residual pos-cancelamento: se Pre cancelou com spread, resultado eh CDI + spread
    pre_cancel = next((c for c in cancelled if c["factor"] == "Pre"), None)
    ipca_cancel = next((c for c in cancelled if c["factor"] == "IPCA+"), None)

    base = ""
    if pre_cancel and pre_cancel["spread_bps"]:
        base = f"CDI {pre_cancel['spread_bps']:+.0f} bps"
    elif ipca_cancel and ipca_cancel["spread_bps"]:
        base = f"CDI {ipca_cancel['spread_bps']:+.0f} bps"

    # Fatores residuais (incluindo CDI quando relevante)
    residual_parts: list[str] = []
    for r in residual:
        factor = r["factor"]
        rate_str = f" {r['rate_total']:.2f}%" if r["rate_total"] is not None else ""
        dir_str = "recebe" if r["direction"] == "recebe" else "paga"
        residual_parts.append(f"{dir_str} {factor}{rate_str}")

    if base and residual_parts:
        return f"{base} + {' + '.join(residual_parts)}"
    if base:
        return base
    if residual_parts:
        return " | ".join(residual_parts)

    has_cdi = any(c["factor"] == "CDI" for c in cancelled) or any(r["factor"] == "CDI" for r in residual)
    if has_cdi:
        return "CDI puro (fatores cancelam)"
    return "Posicao neutra"


def _build_result_description(cancelled: list[dict], residual: list[dict]) -> str:
    """Gera descricao de 1-2 linhas explicando cancelamentos e resultado."""
    parts: list[str] = []

    for c in cancelled:
        if c["factor"] == "CDI" and c["spread_pct"] == 0:
            parts.append(f"CDI cancela entre {', '.join(c['ativo_legs'])} e {', '.join(c['passivo_legs'])}")
            continue
        ativo_str = f"{c['ativo_total']:.3f}%" if c["ativo_total"] is not None else "implicito"
        passivo_str = f"{c['passivo_total']:.3f}%" if c["passivo_total"] is not None else "implicito"
        if c["spread_bps"]:
            parts.append(
                f"{c['factor']} cancela ({', '.join(c['ativo_legs'])} {ativo_str} vs "
                f"{', '.join(c['passivo_legs'])} {passivo_str}, spread {c['spread_bps']:+.0f} bps)"
            )
        else:
            parts.append(f"{c['factor']} cancela entre pernas")

    for r in residual:
        if r["factor"] == "CDI":
            continue
        rate_str = f" {r['rate_total']:.2f}%" if r["rate_total"] is not None else ""
        parts.append(f"Exposto a {r['factor']}{rate_str} ({', '.join(r['legs'])})")

    pre_cancel = next((c for c in cancelled if c["factor"] == "Pre"), None)
    ipca_cancel = next((c for c in cancelled if c["factor"] == "IPCA+"), None)
    if pre_cancel and pre_cancel["spread_bps"]:
        parts.append(f"Resultado pos-fixado CDI {pre_cancel['spread_bps']:+.0f} bps de spread")
    elif ipca_cancel and ipca_cancel["spread_bps"]:
        parts.append(f"Resultado pos-fixado CDI {ipca_cancel['spread_bps']:+.0f} bps de spread real")

    return ". ".join(parts) + "." if parts else ""


def _dol_sintetico_fwd(spot: float, taxa_di: float, taxa_frc: float,
                       du: int, dc: int) -> float:
    """Calcula o dolar forward implicito de DI1+FRC pela paridade coberta.

    Futuro/Spot = (1+pre)^(DU/252) / (1+cupom*DC/360)
    """
    fator_pre = (1 + taxa_di / 100) ** (du / 252)
    fator_cupom = 1 + (taxa_frc / 100) * dc / 360
    return spot * fator_pre / fator_cupom if fator_cupom else 0


def detect_strategy(legs: list[dict], spot: float = 4.9724) -> dict:
    """Detecta estrategia conhecida a partir das pernas.

    Combinacoes reconhecidas:
    - LTN/NTN-F + DI1 (mesmo vcto, mesma direcao) → Casada Pre (CDI + spread bps)
    - NTN-B + DAP (mesmo vcto, mesma direcao)      → Casada IPCA (IPCA + spread bps)
    - DOL + DI1 (mesmo vcto, mesma direcao)         → Cupom Cambial Sintetico
    - DOL + DI1 (mesma vcto, direcao oposta)        → Direcional FX puro
    - Perna unica                                    → Direcional
    """
    from .instruments import cupom_cambial_implicito

    if len(legs) == 1:
        net = compute_net_exposure(legs)
        r = legs[0]
        info = INSTRUMENTS[r["instrument"]]
        d = "Comprado" if r["direction"] == "C" else "Vendido"
        if info.conv == "price":
            return {"result": f"{d} DOL {r['parsed']['label']} a {r['taxa']:.1f}", "type": "single",
                    "economic_description": net["result_description"], "net_exposure": net}
        if info.conv == "lin360":
            return {"result": f"{d} {info.benchmark} {r['taxa']:.2f}% a.a. lin360 ({r['parsed']['label']}), PU {r['pu']:.2f}", "type": "single",
                    "economic_description": net["result_description"], "net_exposure": net}
        return {"result": f"{d} {r['instrument']} {r['parsed']['label']} a {r['taxa']:.3f}%, PU {r['pu']:.2f}, Fin R$ {r['fin']:,.0f}", "type": "single",
                "economic_description": net["result_description"], "net_exposure": net}

    def _find_pair(legs_pool):
        """Tenta encontrar um par reconhecido dentro das pernas.

        Estrategias canonicas detectadas (ref: livro B3 DAP cap.6 Estrategias
        Operacionais):
        - Casada Pre LTN/NTN-F + DI1 (mesma direcao, mesmo vcto): pos-fixada CDI
        - Carteira IPCA Flutuante NTN-B + DAP (mesma direcao): pos-fixada CDI
        - Venda Casada NTN-B + DAP (V+V): caixa em CDI (mesmo branch acima)
        - NTN-B Sintetica LFT + V DAP (mesmo vcto, direcoes opostas): IPCA + cupom_DAP
        - Hedge IPCA Sintetico DI1 + V DAP (vcto similar, direcoes opostas): IPCA sint
        - Direcional Inclinacao DAP curto + DAP longo (direcoes opostas): FRA real
        - Cupom Cambial Sintetico DOL + DI1 (mesma direcao)
        - Dolar Sintetico DI1 + FRC ou DI1 + DDI (direcoes opostas)
        """
        tpfs = [l for l in legs_pool if INSTRUMENTS[l["instrument"]].type == "tpf"]
        dis = [l for l in legs_pool if l["instrument"] == "DI1"]
        daps = [l for l in legs_pool if l["instrument"] == "DAP"]
        dols = [l for l in legs_pool if l["instrument"] == "DOL"]
        lfts = [l for l in tpfs if l["instrument"] == "LFT"]
        ntnbs = [l for l in tpfs if l["instrument"] == "NTN-B"]
        ntnfs = [l for l in tpfs if l["instrument"] == "NTN-F"]
        ltns = [l for l in tpfs if l["instrument"] == "LTN"]

        # --- 1. Casada Pre: LTN/NTN-F + DI1, mesma direcao, mesmo vcto ---
        for t in (ltns + ntnfs):
            for d in dis:
                if t["parsed"]["label"] == d["parsed"]["label"] and t["direction"] == d["direction"]:
                    spread = (t["tax_fin"] - d["taxa"]) * 100
                    name = "Casada Pre (LTN/NTN-F+DI1)"
                    return {"type": "casada", "name": name,
                            "spread": spread, "bmk": "CDI",
                            "tpf": t, "di": d,
                            "result": f"CDI {spread:+.2f} bps"}

        # --- 2. Carteira NTN-B IPCA Flutuante: NTN-B + DAP mesma direcao ---
        for t in ntnbs:
            for d in daps:
                if t["parsed"]["label"] == d["parsed"]["label"] and t["direction"] == d["direction"]:
                    # Livro B3 DAP "Carteira de NTN-B com Cupom de IPCA Flutuante
                    # (Equivalente a uma carteira pos-fixada)". DAP comprado troca
                    # o cupom fixo por flutuante; IPCA cancela; resultado = CDI.
                    spread = (t["tax_fin"] - d["taxa"]) * 100
                    is_venda = t["direction"] == "V"
                    name = "Venda Casada NTN-B+DAP" if is_venda else "Carteira NTN-B com Cupom IPCA Flutuante"
                    return {"type": "casada", "name": name,
                            "spread": spread, "bmk": "CDI",
                            "tpf": t, "di": d,
                            "result": f"CDI {spread:+.2f} bps"}

        # --- 3. NTN-B Sintetica: LFT + DAP em direcoes opostas ---
        # Livro B3 DAP "NTN-B Sintetica (Conversao de uma carteira de LFT em NTN-B)"
        # LFT recebe Selic ≈ CDI; comprar DAP transforma essa rentabilidade em IPCA+cupom
        for t in lfts:
            for d in daps:
                if t["direction"] != d["direction"]:
                    cupom_dap = d["taxa"]
                    return {"type": "ntnb_sint", "name": "NTN-B Sintetica (LFT + DAP)",
                            "cupom_dap": cupom_dap,
                            "tpf": t, "di": d, "bmk": "IPCA",
                            "result": f"NTN-B Sintetica (LFT+DAP opostos): IPCA + {cupom_dap:.2f}%"}

        # --- 4. Hedge IPCA Sintetico: DI1 + DAP em direcoes opostas ---
        # Livro B3 DAP "Hedge em IPCA Sintetico" (DI + V DAP = IPCA sintetico via futuros)
        # IPCA = CDI - cupom_real. DI cancela CDI; DAP fornece IPCA - cupom_DAP. Soma: -cupom_DAP.
        for d in dis:
            for da in daps:
                if d["direction"] != da["direction"]:
                    spread = (d["taxa"] - da["taxa"]) * 100
                    direc = "Comprado" if d["direction"] == "C" else "Vendido"
                    return {"type": "ipca_sint", "name": "Hedge IPCA Sintetico (DI1 + DAP)",
                            "spread": spread,
                            "di": d, "dap": da, "bmk": "IPCA",
                            "result": f"{direc} IPCA Sintetico (DI1+DAP opostos): IPCA {spread:+.2f} bps"}

        # --- 5. Direcional Inclinacao / FRA Cupom IPCA: 2 DAPs vctos diferentes opostos ---
        # Livro B3 DAP "Posicoes direcionais em inclinacao e FRA de Cupom de IPCA"
        if len(daps) >= 2:
            for i, d1 in enumerate(daps):
                for d2 in daps[i+1:]:
                    if d1["direction"] != d2["direction"] and d1["parsed"]["label"] != d2["parsed"]["label"]:
                        curto = d1 if d1["du"] < d2["du"] else d2
                        longo = d2 if d1["du"] < d2["du"] else d1
                        spread = (longo["taxa"] - curto["taxa"]) * 100
                        direc_curto = "C" if curto["direction"] == "C" else "V"
                        direc_longo = "C" if longo["direction"] == "C" else "V"
                        return {"type": "fra_real", "name": "FRA Cupom IPCA / Direcional Inclinacao DAP",
                                "spread": spread,
                                "dap_curto": curto, "dap_longo": longo, "bmk": "Cupom IPCA fwd",
                                "result": f"FRA Cupom IPCA ({direc_curto} {curto['parsed']['label']} + {direc_longo} {longo['parsed']['label']}): inclinacao real {spread:+.2f} bps"}

        # --- 6. Cupom Cambial Sintetico: DOL + DI1 mesma direcao ---
        for dol in dols:
            for d in dis:
                if dol["direction"] == d["direction"]:
                    du_ref = d["du"]
                    dc_ref = d["dc"]
                    cupom = cupom_cambial_implicito(spot, dol["taxa"], d["taxa"], du_ref, dc_ref)
                    direc = "Comprado" if dol["direction"] == "C" else "Vendido"
                    vcto_note = "" if dol["parsed"]["label"] == d["parsed"]["label"] else f" (DOL {dol['parsed']['label']}, DI {d['parsed']['label']})"
                    return {"type": "cupom_sint", "name": "Cupom Cambial Sintetico (DOL + DI1)",
                            "cupom": cupom, "dol": dol, "di": d,
                            "result": f"{direc} Cupom Cambial Sintetico: {cupom:.2f}% a.a.{vcto_note}"}

        # --- 7. Dolar Sintetico: DI1 + FRC/DDI em direcoes opostas ---
        frcs = [l for l in legs_pool if l["instrument"] == "FRC"]
        ddis = [l for l in legs_pool if l["instrument"] == "DDI"]

        for d in dis:
            for f in frcs:
                if d["parsed"]["label"] == f["parsed"]["label"] and d["direction"] != f["direction"]:
                    direc = "Comprado" if d["direction"] == "C" else "Vendido"
                    fwd = _dol_sintetico_fwd(spot, d["taxa"], f["taxa"], d["du"], f["dc"])
                    return {"type": "dol_sint", "name": "Dolar Sintetico (DI1 + FRC)",
                            "di": d, "frc": f, "fwd": fwd,
                            "result": f"{direc} Dolar Sintetico (DI1+FRC): fwd ~{fwd:.2f}"}

        for d in dis:
            for dd in ddis:
                if d["parsed"]["label"] == dd["parsed"]["label"] and d["direction"] != dd["direction"]:
                    direc = "Comprado" if d["direction"] == "C" else "Vendido"
                    return {"type": "dol_sint_ddi", "name": "Dolar Sintetico (DI1 + DDI)",
                            "di": d, "ddi": dd,
                            "result": f"{direc} Dolar Sintetico (DI1+DDI)"}

        return None

    # 1. Motor generico SEMPRE roda: soma exposicoes, cancela fatores, gera resultado
    net = compute_net_exposure(legs)

    # 2. Hardcoded so decora com nome do livro (nunca sobrescreve resultado do motor)
    pair = _find_pair(legs)

    # Resultado vem SEMPRE do motor
    result = {
        "result": net["result_label"],
        "type": pair["type"] if pair else "generic",
        "net_exposure": net,
        "economic_description": net["result_description"],
    }

    # Hardcoded adiciona nome, bmk, spread e descricao do livro B3 por cima
    if pair:
        result["name"] = pair.get("name")
        result["bmk"] = pair.get("bmk")
        result["spread"] = pair.get("spread")
        for k in ("tpf", "di", "dol", "frc", "ddi", "dap",
                   "dap_curto", "dap_longo", "cupom", "fwd", "cupom_dap"):
            if k in pair:
                result[k] = pair[k]
        # Descricao economica precisa do result completo (com net_exposure) pra citar pernas extras
        result["economic_description"] = _describe_strategy_economic(legs, result)

    return result


def _describe_strategy_economic(legs: list[dict], strategy: dict) -> str:
    """Descricao economica de 1-2 linhas em linguagem do livro B3.

    Cita o nome canonico (quando aplicavel), o swap equivalente / resultado
    economico final e a referencia ao livro. Usado para explicar ao usuario
    o que a operacao significa (alem do label tecnico do strategy.result).
    """
    typ = strategy.get("type", "")

    if typ == "casada":
        tpf = strategy.get("tpf", {})
        tpf_inst = tpf.get("instrument", "TPF")

        # Pernas residuais alem do par (ex: 3a perna FRC em LTN+DI1+FRC)
        net = strategy.get("net_exposure", {})
        extra_residual = [
            r for r in net.get("residual", [])
            if r["factor"] not in ("CDI",)
        ]
        extra_str = ""
        if extra_residual:
            parts = [f"{r['direction']} {r['factor']} {r['rate_total']:.2f}%" if r["rate_total"] else f"{r['direction']} {r['factor']}" for r in extra_residual]
            extra_str = f" Adicionalmente: {', '.join(parts)}."

        if tpf_inst == "NTN-B":
            is_venda = tpf.get("direction") == "V"
            if is_venda:
                return (
                    "Venda Casada de NTN-B com Futuro de Cupom de IPCA (livro B3 DAP, cap.6). "
                    "Vende NTN-B a vista + vende DAP — caixa rendendo CDI + spread real."
                    + extra_str
                )
            return (
                "Carteira de NTN-B com Cupom de IPCA Flutuante (livro B3 DAP, cap.6). "
                "Compra NTN-B + compra DAP transforma cupom real fixo em flutuante; "
                "IPCA cancela e a posicao vira pos-fixada CDI + spread real."
                + extra_str
            )
        # LTN ou NTN-F + DI1
        return (
            "Casada Pre (LTN/NTN-F + DI1 mesma direcao). "
            "TPF financiada via DI futuro; o fator pre cancela e a posicao vira "
            "pos-fixada CDI + spread."
            + extra_str
        )

    if typ == "ntnb_sint":
        dap_leg = strategy.get("di", {})
        dap_dir = "vender" if dap_leg.get("direction") == "V" else "comprar"
        return (
            f"NTN-B Sintetica (Conversao de carteira de LFT em NTN-B, livro B3 DAP cap.6). "
            f"LFT recebe Selic ~CDI; {dap_dir} DAP transforma a rentabilidade em IPCA + cupom_DAP fixo."
        )

    if typ == "ipca_sint":
        return (
            "Hedge IPCA Sintetico (DI + DAP em direcoes opostas, livro B3 DAP cap.6). "
            "DI fornece CDI; DAP transforma CDI em IPCA + cupom; resultado = NTN-B sintetica."
        )

    if typ == "fra_real":
        return (
            "FRA de Cupom de IPCA / Direcional na Inclinacao da curva real (livro B3 DAP cap.6). "
            "2 DAPs em vencimentos diferentes em direcoes opostas; isola o cupom IPCA forward "
            "entre os dois prazos sem exposicao paralela."
        )

    if typ == "cupom_sint":
        return (
            "Cupom Cambial Sintetico via paridade coberta de juros. "
            "Comprar DOL + comprar DI (mesma direcao) cria exposicao ao cupom cambial implicito; "
            "P&L direcional ao FRC. Equivalente a vender FRC sintetico."
        )

    if typ in ("dol_sint", "dol_sint_ddi"):
        return (
            "Dolar Sintetico via paridade coberta (DI1 + FRC/DDI em direcoes opostas). "
            "DI fornece CDI BRL; FRC/DDI fornece cupom cambial USD; "
            "resultado eh forward USD/BRL implicito - posicao direcional pura no dolar spot."
        )

    if typ == "single":
        # ja tem result completo
        return ""

    if typ == "multi":
        return "Combinacao multi-perna sem padrao canonico reconhecido. Veja fatores de risco."

    return ""


def _hedge_instrument_for_tpf(tpf_inst: str) -> str:
    """Derivativo correto de hedge: DAP para NTN-B (curva real); DI1 para LTN/NTN-F (curva pre)."""
    return "DAP" if tpf_inst == "NTN-B" else "DI1"


def _curve_label_for_tpf(tpf_inst: str) -> str:
    """Curva relevante: 'real (IPCA)' para NTN-B; 'pre' para LTN/NTN-F."""
    return "real (IPCA)" if tpf_inst == "NTN-B" else "pre"


def analyze_risk_factors(legs: list[dict], strategy: dict) -> list[dict]:
    """Analisa fatores de risco em duas camadas:

    1. MOTOR (net_exposure): gera fatores base de cancelamento/residual
       para TODA combinacao de pernas (nunca perde uma perna)
    2. ESTRUTURAL: adiciona fatores de inclinacao, curvatura, convexidade,
       spread basis quando propriedades das pernas permitem

    Excecao: hedge mode (strip/duration/maturity) tem logica propria
    porque a analise depende do modo de hedge, nao so das exposicoes.
    """
    factors = []
    insts = {l["instrument"] for l in legs}
    has_cupom_tpf = any(INSTRUMENTS[l["instrument"]].cup_sem > 0 for l in legs)
    has_di = "DI1" in insts
    has_dap = "DAP" in insts
    has_dol = "DOL" in insts
    has_ntnb = "NTN-B" in insts

    # --- Hedge mode especifico (strip/duration/maturity) mantem logica propria ---
    coupon_tpf_with_hedge = next(
        (l for l in legs
         if INSTRUMENTS[l["instrument"]].cup_sem > 0
         and l.get("hedge_mode", "manual") in ("maturity", "duration", "strip")
         and not l.get("auto")),
        None,
    )
    if coupon_tpf_with_hedge:
        mode = coupon_tpf_with_hedge.get("hedge_mode")
        tpf_name = coupon_tpf_with_hedge["instrument"]
        hedge_inst = _hedge_instrument_for_tpf(tpf_name)
        curve_lbl = _curve_label_for_tpf(tpf_name)
        if mode == "strip":
            factors.append({"fator": "Nivel (shift paralelo)", "exposto": False,
                            "desc": f"Strip hedge: 1 {hedge_inst} por fluxo do {tpf_name} casa DV01 fluxo a fluxo na curva {curve_lbl}"})
            factors.append({"fator": "Inclinacao (steepening)", "exposto": False,
                            "desc": f"Cada cupom tem seu proprio {hedge_inst} no mesmo DU — neutraliza torcoes da curva {curve_lbl}"})
            factors.append({"fator": "Curvatura (butterfly)", "exposto": False,
                            "desc": f"Strip casa key-rates em todos os vertices do {tpf_name} — convexidade hedgeada"})
            factors.append({"fator": "Convexidade (gamma)", "exposto": False,
                            "desc": f"Convexidade replicada fluxo a fluxo via strip de {hedge_inst}"})
            if has_ntnb:
                factors.append({"fator": "Inflacao (IPCA)", "exposto": False,
                                "desc": "Strip de DAP fixa o cupom de IPCA em cada vertice — IPCA neutralizado"})
            return factors
        elif mode == "duration":
            factors.append({"fator": "Nivel (shift paralelo)", "exposto": False,
                            "desc": f"Duration hedge: 1 {hedge_inst} no D.Mac do {tpf_name} casa DV01 total no shift paralelo"})
            factors.append({"fator": "Inclinacao (steepening)", "exposto": True,
                            "desc": f"{hedge_inst} cobre 1 unico vertice (D.Mac); cupons do {tpf_name} ficam em outros vertices da curva {curve_lbl}"})
            factors.append({"fator": "Curvatura (butterfly)", "exposto": True,
                            "desc": f"Sem casamento de key-rates em {tpf_name} vs {hedge_inst} (1 vertice) → twist nao-paralelo gera P&L"})
            factors.append({"fator": "Convexidade (gamma)", "exposto": True,
                            "desc": f"{hedge_inst} (zero-coupon) tem convexidade diferente do {tpf_name} (cupons)"})
            if has_ntnb:
                factors.append({"fator": "Inflacao (IPCA)", "exposto": False,
                                "desc": "DAP no D.Mac hedgeia IPCA em 1a ordem (residual: spread IPCA por torcao)"})
            return factors
        elif mode == "maturity":
            factors.append({"fator": "Nivel (shift paralelo)", "exposto": False,
                            "desc": f"Vcto hedge: 1 {hedge_inst} no DU final do {tpf_name} (mismatch de DV01 leve por D.Mac < DU final)"})
            factors.append({"fator": "Inclinacao (steepening)", "exposto": True,
                            "desc": f"Hedge so na ponta longa; cupons intermediarios do {tpf_name} expostos a curto da curva {curve_lbl}"})
            factors.append({"fator": "Curvatura (butterfly)", "exposto": True,
                            "desc": f"Cupons em vertices intermediarios sem hedge — sensivel a movimento da barriga da curva {curve_lbl}"})
            factors.append({"fator": "Convexidade (gamma)", "exposto": True,
                            "desc": f"D.Mac do {tpf_name} < DU final → {hedge_inst} no vencimento gera dollar-duration excessivo no longo"})
            if has_ntnb:
                factors.append({"fator": "Inflacao (IPCA)", "exposto": False,
                                "desc": "DAP no vencimento hedgeia IPCA com mismatch (residual concentrado nos cupons curtos)"})
            return factors

    # === CAMADA 1: MOTOR — fatores derivados de net_exposure (SEMPRE roda) ===
    net = strategy.get("net_exposure")
    if net:
        for c in net["cancelled"]:
            if c["spread_bps"]:
                factors.append({"fator": f"{c['factor']} (cancela)", "exposto": False,
                                "desc": f"{c['factor']} cancela entre {', '.join(c['ativo_legs'])} e {', '.join(c['passivo_legs'])} (spread {c['spread_bps']:+.0f} bps)"})
            else:
                factors.append({"fator": f"{c['factor']} (cancela)", "exposto": False,
                                "desc": f"{c['factor']} cancela entre pernas"})
        for r in net["residual"]:
            rate_str = f" {r['rate_total']:.2f}%" if r["rate_total"] is not None else ""
            factors.append({"fator": r["factor"], "exposto": True,
                            "desc": f"{r['direction'].capitalize()} {r['factor']}{rate_str} ({', '.join(r['legs'])})"})

    # === CAMADA 2: ESTRUTURAL — detalhes de inclinacao, curvatura, convexidade ===

    # Spread basis (quando tem par de instrumentos com spread travado)
    spread = strategy.get("spread")
    if spread is not None:
        bmk = strategy.get("bmk", "CDI")
        factors.append({"fator": "Spread (basis)", "exposto": True,
                        "desc": f"Posicao trava a operacao em {bmk} {spread:+.2f} bps — abertura/fechamento do spread move o P&L direto"})

    # Inclinacao / Curvatura (titulos com cupom vs derivativo zero-coupon)
    if has_cupom_tpf:
        tpf_legs = [l for l in legs if INSTRUMENTS[l["instrument"]].cup_sem > 0]
        deriv_legs = [l for l in legs if l["instrument"] in ("DI1", "DAP")]
        for tpf_leg in tpf_legs:
            tpf_inst = tpf_leg["instrument"]
            hedge_inst = _hedge_instrument_for_tpf(tpf_inst)
            curve_lbl = _curve_label_for_tpf(tpf_inst)
            has_matching_deriv = any(d["instrument"] == hedge_inst for d in deriv_legs)
            if has_matching_deriv:
                factors.append({"fator": f"Inclinacao ({tpf_inst})", "exposto": True,
                                "desc": f"{tpf_inst} tem cupons em multiplos vertices da curva {curve_lbl}; {hedge_inst} cobre apenas 1 vertice"})
                factors.append({"fator": f"Curvatura ({tpf_inst})", "exposto": True,
                                "desc": f"{tpf_inst} (com cupons) vs {hedge_inst} (zero-coupon) — convexidades diferentes deixam barriga exposta"})
            else:
                factors.append({"fator": f"Inclinacao ({tpf_inst})", "exposto": True,
                                "desc": f"{tpf_inst} tem cupons em multiplos vertices — exposto a torcoes da curva {curve_lbl}"})

    # Convexidade (gamma) — quando TPF com cupom + derivativo, mostra D.Mac diff
    if has_cupom_tpf and (has_di or has_dap):
        tpf_leg = next((l for l in legs if INSTRUMENTS[l["instrument"]].cup_sem > 0), None)
        deriv_leg = next((l for l in legs if l["instrument"] in ("DI1", "DAP")), None)
        if tpf_leg and deriv_leg:
            diff = abs(tpf_leg["d_mac"] - deriv_leg["d_mac"])
            factors.append({"fator": "Convexidade (gamma)", "exposto": diff > 0.3,
                            "desc": f"D.Mac {tpf_leg['instrument']}={tpf_leg['d_mac']:.2f}a vs {deriv_leg['instrument']}={deriv_leg['d_mac']:.2f}a (diff {diff:.2f}a) — convexidade descasada gera P&L em movimentos grandes"})

    return factors


def suggest_hedge(legs: list[dict]):
    """Sugere quantidade de DI1/DAP para hedge de TPF com cupom.

    Tres modalidades:
    1. Vencimento: 1 contrato DI1/DAP no DU do vencimento final
    2. Duration: 1 contrato DI1/DAP no DU da Macaulay duration
    3. Strip (hedge perfeito): 1 contrato por fluxo, casando VP fluxo a fluxo
    """
    from .instruments import key_rate_duration

    tpf = next((l for l in legs if INSTRUMENTS[l["instrument"]].cup_sem > 0), None)
    if not tpf:
        return None

    hedge_inst = "DAP" if tpf["instrument"] == "NTN-B" else "DI1"

    di_rate = 13.65
    di_leg = next((l for l in legs if l["instrument"] in ("DI1", "DAP")), None)
    if di_leg:
        di_rate = di_leg["taxa"]

    du_dur = round(tpf["d_mac"] * 252)
    du_mat = tpf["du"]

    dv01_at_dur = dv01(hedge_inst, di_rate, du_dur, du_dur, 1)
    dv01_at_mat = dv01(hedge_inst, di_rate, du_mat, du_mat, 1)

    n_at_dur = round(tpf["dv01_total"] / dv01_at_dur.unit) if dv01_at_dur.unit else 0
    n_at_mat = round(tpf["dv01_total"] / dv01_at_mat.unit) if dv01_at_mat.unit else 0
    current_n = di_leg["quantity"] if di_leg else 0
    resid = tpf["dv01_total"] - (di_leg["dv01_total"] if di_leg else 0)

    strip_legs = []
    flows = key_rate_duration(
        tpf["instrument"], tpf["taxa"], tpf["du"],
        tpf.get("liq"), tpf.get("parsed", {}).get("date"),
    )
    tpf_vna = tpf.get("vna")
    vna_scale = (tpf_vna / 100) if (tpf["instrument"] == "NTN-B" and tpf_vna and tpf_vna > 0) else 1.0

    for f in flows:
        pv_scaled = f.pv * vna_scale
        flow_dmod = f.t_anos / (1 + tpf["taxa"] / 100)
        flow_dv01 = flow_dmod * pv_scaled * 0.0001
        flow_dv01_total = flow_dv01 * tpf["quantity"]

        di_dv01_1 = dv01(hedge_inst, di_rate, f.du, f.du, 1)
        n_strip = round(flow_dv01_total / di_dv01_1.unit) if di_dv01_1.unit else 0

        strip_legs.append({
            "label": f.label,
            "payment_date": f.payment_date,
            "du": f.du,
            "t_anos": f.t_anos,
            "pv_flow": pv_scaled,
            "pv_flow_total": pv_scaled * tpf["quantity"],
            "dv01_flow": flow_dv01_total,
            "hedge_instrument": hedge_inst,
            "hedge_du": f.du,
            "hedge_dv01_unit": di_dv01_1.unit,
            "hedge_n": n_strip,
        })

    return {
        "tpf": tpf,
        "hedge_instrument": hedge_inst,
        "di_rate": di_rate,
        "du_duration": du_dur,
        "du_maturity": du_mat,
        "n_at_duration": n_at_dur,
        "n_at_maturity": n_at_mat,
        "dv01_at_duration": dv01_at_dur.unit,
        "dv01_at_maturity": dv01_at_mat.unit,
        "current_n": current_n,
        "dv01_residual": resid,
        "strip": strip_legs,
        "n_strip_total": sum(s["hedge_n"] for s in strip_legs),
    }
