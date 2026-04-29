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

    pay_bm = "IPCA+" if instrumento == "DAP" else "Pre"
    rec_bm = "CDI" if instrumento == "DI1" else "IPCA"
    val = f"{pay_bm} {rs}"
    return {"ativo": rec_bm, "passivo": val} if direcao == "C" else {"ativo": val, "passivo": rec_bm}


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
        r = legs[0]
        info = INSTRUMENTS[r["instrument"]]
        d = "Comprado" if r["direction"] == "C" else "Vendido"
        if info.conv == "price":
            return {"result": f"{d} DOL {r['parsed']['label']} a {r['taxa']:.1f}", "type": "single"}
        if info.conv == "lin360":
            return {"result": f"{d} {info.benchmark} {r['taxa']:.2f}% a.a. lin360 ({r['parsed']['label']}), PU {r['pu']:.2f}", "type": "single"}
        return {"result": f"{d} {r['instrument']} {r['parsed']['label']} a {r['taxa']:.3f}%, PU {r['pu']:.2f}, Fin R$ {r['fin']:,.0f}", "type": "single"}

    def _find_pair(legs_pool):
        """Tenta encontrar um par reconhecido dentro das pernas."""
        tpfs = [l for l in legs_pool if INSTRUMENTS[l["instrument"]].type == "tpf"]
        dis = [l for l in legs_pool if l["instrument"] == "DI1"]
        daps = [l for l in legs_pool if l["instrument"] == "DAP"]
        dols = [l for l in legs_pool if l["instrument"] == "DOL"]

        for t in tpfs:
            for d in dis:
                if t["parsed"]["label"] == d["parsed"]["label"] and t["direction"] == d["direction"]:
                    spread = (t["tax_fin"] - d["taxa"]) * 100
                    bmk = "IPCA" if t["instrument"] == "NTN-B" else "CDI"
                    return {"type": "casada", "spread": spread, "bmk": bmk, "tpf": t, "di": d,
                            "result": f"{bmk} {spread:+.2f} bps"}

        for t in [l for l in tpfs if l["instrument"] == "NTN-B"]:
            for d in daps:
                if t["parsed"]["label"] == d["parsed"]["label"] and t["direction"] == d["direction"]:
                    spread = (t["tax_fin"] - d["taxa"]) * 100
                    return {"type": "casada", "spread": spread, "bmk": "IPCA", "tpf": t, "di": d,
                            "result": f"IPCA {spread:+.2f} bps"}

        for dol in dols:
            for d in dis:
                if dol["direction"] == d["direction"]:
                    du_ref = d["du"]
                    dc_ref = d["dc"]
                    cupom = cupom_cambial_implicito(spot, dol["taxa"], d["taxa"], du_ref, dc_ref)
                    direc = "Comprado" if dol["direction"] == "C" else "Vendido"
                    vcto_note = "" if dol["parsed"]["label"] == d["parsed"]["label"] else f" (DOL {dol['parsed']['label']}, DI {d['parsed']['label']})"
                    return {"type": "cupom_sint", "cupom": cupom, "dol": dol, "di": d,
                            "result": f"{direc} Cupom Cambial Sintetico: {cupom:.2f}% a.a.{vcto_note}"}

        frcs = [l for l in legs_pool if l["instrument"] == "FRC"]
        ddis = [l for l in legs_pool if l["instrument"] == "DDI"]

        for d in dis:
            for f in frcs:
                if d["parsed"]["label"] == f["parsed"]["label"] and d["direction"] != f["direction"]:
                    direc = "Comprado" if d["direction"] == "C" else "Vendido"
                    fwd = _dol_sintetico_fwd(spot, d["taxa"], f["taxa"], d["du"], f["dc"])
                    return {"type": "dol_sint", "di": d, "frc": f, "fwd": fwd,
                            "result": f"{direc} Dolar Sintetico (DI1+FRC): fwd ~{fwd:.2f}"}

        for d in dis:
            for dd in ddis:
                if d["parsed"]["label"] == dd["parsed"]["label"] and d["direction"] != dd["direction"]:
                    direc = "Comprado" if d["direction"] == "C" else "Vendido"
                    return {"type": "dol_sint_ddi", "di": d, "ddi": dd,
                            "result": f"{direc} Dolar Sintetico (DI1+DDI)"}

        return None

    pair = _find_pair(legs)
    if pair:
        return pair

    descs = []
    for l in legs:
        info = INSTRUMENTS[l["instrument"]]
        d = "C" if l["direction"] == "C" else "V"
        if info.conv == "price":
            descs.append(f"{d} {l['instrument']} {l['parsed']['label']} {l['taxa']:.1f}")
        else:
            descs.append(f"{d} {l['instrument']} {l['parsed']['label']} {l['taxa']:.3f}%")
    return {"result": " | ".join(descs), "type": "multi"}


def _hedge_instrument_for_tpf(tpf_inst: str) -> str:
    """Derivativo correto de hedge: DAP para NTN-B (curva real); DI1 para LTN/NTN-F (curva pre)."""
    return "DAP" if tpf_inst == "NTN-B" else "DI1"


def _curve_label_for_tpf(tpf_inst: str) -> str:
    """Curva relevante: 'real (IPCA)' para NTN-B; 'pre' para LTN/NTN-F."""
    return "real (IPCA)" if tpf_inst == "NTN-B" else "pre"


def analyze_risk_factors(legs: list[dict], strategy: dict) -> list[dict]:
    """Analisa quais fatores de risco a operacao esta exposta.

    Fatores avaliados:
    - Nivel (shift paralelo)
    - Inclinacao (steepening/flattening)
    - Curvatura (butterfly)
    - Convexidade (gamma)
    - Spread (basis entre titulo e DI/DAP)
    - Cambio (USD/BRL)
    - Cupom cambial
    - Inflacao (IPCA)
    """
    factors = []
    insts = {l["instrument"] for l in legs}
    has_cupom_tpf = any(INSTRUMENTS[l["instrument"]].cup_sem > 0 for l in legs)
    has_di = "DI1" in insts
    has_dap = "DAP" in insts
    has_dol = "DOL" in insts
    has_ntnb = "NTN-B" in insts
    same_vcto = len(legs) > 1 and all(l["parsed"]["label"] == legs[0]["parsed"]["label"] for l in legs)
    is_casada = strategy["type"] == "casada"
    is_dol_sint = strategy["type"] in ("dol_sint", "dol_sint_ddi")

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

    if len(legs) == 1:
        info = INSTRUMENTS[legs[0]["instrument"]]
        leg = legs[0]
        if info.conv == "price":
            factors.append({"fator": "Cambio (USD/BRL)", "exposto": True,
                            "desc": f"Direcional em USD/BRL — DV01 R$ {leg['dv01_total']:.0f}/ponto (R$ 50 por contrato {leg['instrument']})"})
        else:
            factors.append({"fator": "Nivel (shift paralelo)", "exposto": True,
                            "desc": f"Direcional na taxa — DV01 R$ {leg['dv01_total']:.0f} por bp na curva {info.benchmark}"})
            if has_cupom_tpf:
                factors.append({"fator": "Inclinacao", "exposto": True,
                                "desc": f"{leg['instrument']} paga cupom semestral — cada fluxo descontado por sua taxa spot, exposto a torcoes"})
                factors.append({"fator": "Curvatura (butterfly)", "exposto": True,
                                "desc": f"Distribuicao de fluxos amplifica sensibilidade a movimento da barriga da curva"})
            if has_ntnb:
                factors.append({"fator": "Inflacao (IPCA)", "exposto": True,
                                "desc": "NTN-B atualizada por IPCA via VNA — mudanca no IPCA realizado/projetado afeta PU diretamente"})
        return factors

    if is_dol_sint:
        factors.append({"fator": "Cambio (USD/BRL)", "exposto": True,
                        "desc": "DI1+FRC/DDI replica dolar forward via paridade coberta — P&L direcional ao spot USD/BRL"})
        factors.append({"fator": "Nivel (taxa pre BRL)", "exposto": False,
                        "desc": "DI1 e FRC/DDI tem mesmo DV01 com sinais opostos — fator pre cancela em 1a ordem"})
        factors.append({"fator": "Cupom Cambial", "exposto": False,
                        "desc": "Perna FRC/DDI fixa o cupom cambial embutido — exposicao residual e o spot do dolar"})
        return factors

    if is_casada and same_vcto and not has_cupom_tpf:
        factors.append({"fator": "Nivel (shift paralelo)", "exposto": False,
                        "desc": "Mesmo vencimento + zero-coupon: DV01 batido — shift paralelo cancela em 1a ordem"})
    elif is_casada and has_cupom_tpf:
        tpf_inst = next(l["instrument"] for l in legs if INSTRUMENTS[l["instrument"]].cup_sem > 0)
        hedge_inst = _hedge_instrument_for_tpf(tpf_inst)
        factors.append({"fator": "Nivel (shift paralelo)", "exposto": False,
                        "desc": f"Hedge por DV01 com {hedge_inst} cancela shift paralelo em 1a ordem (residual de convexidade)"})
    elif has_dol and has_di:
        factors.append({"fator": "Nivel (taxa pre BRL)", "exposto": False,
                        "desc": "DOL paga pre via paridade coberta; DI1 mesma direcao cancela o fator pre BRL"})
    else:
        factors.append({"fator": "Nivel (shift paralelo)", "exposto": True,
                        "desc": "Pernas em vencimentos ou benchmarks distintos — fator nivel nao se cancela"})

    if has_dol and has_di:
        factors.append({"fator": "Cupom Cambial", "exposto": True,
                        "desc": "DOL + DI1 (mesma direcao) = cupom cambial sintetico via paridade — sensivel a movimento do FRC implicito"})

    if is_casada and has_cupom_tpf:
        tpf_inst = next(l["instrument"] for l in legs if INSTRUMENTS[l["instrument"]].cup_sem > 0)
        hedge_inst = _hedge_instrument_for_tpf(tpf_inst)
        curve_lbl = _curve_label_for_tpf(tpf_inst)
        factors.append({"fator": "Inclinacao (steepening)", "exposto": True,
                        "desc": f"{tpf_inst} tem cupons em multiplos vertices da curva {curve_lbl}; {hedge_inst} cobre apenas 1 vertice"})
        factors.append({"fator": "Curvatura (butterfly)", "exposto": True,
                        "desc": f"{tpf_inst} (com cupons) vs {hedge_inst} (zero-coupon) — convexidades diferentes deixam barriga exposta"})
    elif is_casada and not has_cupom_tpf and same_vcto:
        factors.append({"fator": "Inclinacao", "exposto": False,
                        "desc": "Ambos zero-coupon no mesmo vertice — sem fluxos intermediarios para gerar exposicao a torcoes"})
        factors.append({"fator": "Curvatura", "exposto": False,
                        "desc": "Convexidades praticamente iguais (zero-coupon mesmo prazo) — butterfly nao gera P&L material"})

    if has_cupom_tpf and (has_di or has_dap):
        tpf_leg = next(l for l in legs if INSTRUMENTS[l["instrument"]].cup_sem > 0)
        deriv_leg = next(l for l in legs if l["instrument"] in ("DI1", "DAP"))
        diff = abs(tpf_leg["d_mac"] - deriv_leg["d_mac"])
        factors.append({"fator": "Convexidade (gamma)", "exposto": diff > 0.3,
                        "desc": f"D.Mac {tpf_leg['instrument']}={tpf_leg['d_mac']:.2f}a vs {deriv_leg['instrument']}={deriv_leg['d_mac']:.2f}a (diff {diff:.2f}a) — convexidade descasada gera P&L em movimentos grandes"})

    if is_casada:
        spread = strategy.get("spread", 0)
        bmk = strategy.get("bmk", "CDI")
        factors.append({"fator": "Spread (basis)", "exposto": True,
                        "desc": f"Posicao trava a operacao em {bmk} {spread:+.2f} bps — abertura/fechamento do spread move o P&L direto"})

    if has_dol and not has_di:
        factors.append({"fator": "Cambio (USD/BRL)", "exposto": True,
                        "desc": "Posicao direcional pura em DOL — sensibilidade R$ 50 por ponto por contrato"})
    elif has_dol and has_di:
        factors.append({"fator": "Cambio (USD/BRL)", "exposto": False,
                        "desc": "DOL + DI1 (mesma direcao) neutraliza cambio puro — exposicao residual e o cupom cambial implicito"})

    if has_ntnb and not has_dap:
        factors.append({"fator": "Inflacao (IPCA)", "exposto": True,
                        "desc": "NTN-B sem DAP — VNA atualizado por IPCA gera P&L direto com surpresa de inflacao"})
    elif has_ntnb and has_dap:
        factors.append({"fator": "Inflacao (IPCA)", "exposto": False,
                        "desc": "NTN-B + DAP no mesmo vertice neutraliza IPCA em 1a ordem — exposicao residual e o spread real (taxa IPCA)"})

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
