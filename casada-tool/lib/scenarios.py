"""Cenarios de curva de juros e calculo de P&L por perna.

Cenarios nomeados do mercado:
- Bull/Bear Parallel: shift uniforme em todas as taxas
- Bull/Bear Steepener: curtos e longos movem em proporcoes diferentes
- Bull/Bear Flattener: idem, direcao oposta
- Positive/Negative Butterfly: barriga vs pontas
"""

from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from .instruments import INSTRUMENTS, pu, _coupon_cashflows
from .curves import flat_forward_interp, build_di_vertices, build_dap_vertices


@dataclass
class ScenarioDefinition:
    name: str
    desc: str

    def delta(self, t: float, mag: float) -> float:
        """Calcula delta em bps para um ponto da curva.

        Args:
            t: posicao normalizada na curva, -1 (curto) a +1 (longo)
            mag: magnitude em bps (positivo = direcao do cenario, negativo = oposta)
        """
        raise NotImplementedError


class BullParallel(ScenarioDefinition):
    """Todas as taxas caem uniformemente."""
    def delta(self, t, mag):
        return -mag

class BearParallel(ScenarioDefinition):
    """Todas as taxas sobem uniformemente."""
    def delta(self, t, mag):
        return mag

class BullSteepener(ScenarioDefinition):
    """Curtos caem mais que longos. Tipico: corte de Selic."""
    def delta(self, t, mag):
        return -mag + mag * ((t + 1) / 2)

class BearSteepener(ScenarioDefinition):
    """Longos sobem mais que curtos. Tipico: premio a termo, fiscal."""
    def delta(self, t, mag):
        return mag * ((t + 1) / 2)

class BullFlattener(ScenarioDefinition):
    """Longos caem mais que curtos. Tipico: recessao, risk-off."""
    def delta(self, t, mag):
        return -mag * ((t + 1) / 2)

class BearFlattener(ScenarioDefinition):
    """Curtos sobem mais que longos. Tipico: ciclo de alta da Selic."""
    def delta(self, t, mag):
        return mag - mag * ((t + 1) / 2)

class PositiveButterfly(ScenarioDefinition):
    """Barriga sobe, pontas caem. Pressao no miolo da curva.
    Mean-zero: integral de -1 a 1 = 0 (sem bias direcional)."""
    def delta(self, t, mag):
        return mag * (0.5 - 1.5 * t * t)

class NegativeButterfly(ScenarioDefinition):
    """Barriga cai, pontas sobem. Demanda pelo belly.
    Mean-zero: integral de -1 a 1 = 0 (sem bias direcional)."""
    def delta(self, t, mag):
        return mag * (1.5 * t * t - 0.5)

class CustomScenario(ScenarioDefinition):
    """Cenario customizado com 3 componentes independentes."""
    def __init__(self):
        super().__init__("Custom", "Defina paralelo, inclinacao e curvatura separadamente")
        self.parallel = 0.0
        self.slope = 0.0
        self.curvature = 0.0

    def delta(self, t, mag):
        return self.parallel + self.slope * t + self.curvature * (-(1 - t * t))


SCENARIOS: dict[str, ScenarioDefinition] = {
    "bull_par":   BullParallel("Bull Parallel", "Todas as taxas caem — flight-to-quality, corte surpresa"),
    "bear_par":   BearParallel("Bear Parallel", "Todas as taxas sobem — surpresa inflacionaria, BCB hawkish"),
    "bull_steep": BullSteepener("Bull Steepener", "Curtos caem mais que longos — corte de Selic"),
    "bear_steep": BearSteepener("Bear Steepener", "Longos sobem mais que curtos — premio a termo, fiscal"),
    "bull_flat":  BullFlattener("Bull Flattener", "Longos caem mais que curtos — recessao, risk-off"),
    "bear_flat":  BearFlattener("Bear Flattener", "Curtos sobem mais que longos — ciclo de alta"),
    "pos_fly":    PositiveButterfly("Positive Butterfly", "Barriga sobe, pontas caem"),
    "neg_fly":    NegativeButterfly("Negative Butterfly", "Barriga cai, pontas sobem"),
    "custom":     CustomScenario(),
}


# Vertices padronizados usados como ANCORAS para cenarios nao-paralelos.
# Padrao Bacen/RiskMetrics e Mercado de Renda Fixa (capitulo 17): vertices
# absolutos definem "curto" e "longo" em termos de mercado, NAO em termos
# da carteira do usuario. Isso evita o bug de uma carteira concentrada num
# unico vencimento (ex: NTN-F Jan/31 + DI1 Jan/31, ambos ~1170 DU) tratar
# todos os cashflows curtos como se fossem 'curtos' relativos uns aos outros.
#
# Curto = 1 mes (21 DU). Longo = 10 anos (2520 DU). Mid = 5 anos (~1270 DU).
# Para steepener/flattener, este eh o range em que a magnitude completa eh
# aplicada nas pontas.
SCENARIO_DU_SHORT = 21
SCENARIO_DU_LONG = 2520

# Cupom cambial (FRC, DDI) eh quotado em DC linear 360. Ancoras analogas:
# 30 DC ~= 1 mes, 3600 DC ~= 10 anos.
SCENARIO_DC_SHORT = 30
SCENARIO_DC_LONG = 3600


def calc_scenario_delta_fixed(du: int, scenario_key: str, magnitude: float,
                               custom_parallel_bps: float = 0.0,
                               custom_slope_bps: float = 0.0,
                               custom_curvature_bps: float = 0.0) -> float:
    """Versao do calc_scenario_delta com ancoras absolutas (1m a 10y).

    Use esta funcao em PRODUCAO (charts, decomposition, MtM table). A funcao
    `calc_scenario_delta` original, com du_min/du_max parametrizaveis, eh
    mantida para testes oracle e usos legados.
    """
    return calc_scenario_delta(du, SCENARIO_DU_SHORT, SCENARIO_DU_LONG,
                                scenario_key, magnitude,
                                custom_parallel_bps, custom_slope_bps, custom_curvature_bps)


def calc_scenario_delta(du: int, du_min: int, du_max: int,
                         scenario_key: str, magnitude: float,
                         custom_parallel_bps: float = 0.0,
                         custom_slope_bps: float = 0.0,
                         custom_curvature_bps: float = 0.0) -> float:
    """Calcula o choque em bps para um vertice especifico.

    Args:
        du: DU do vertice
        du_min: menor DU entre todas as pernas
        du_max: maior DU entre todas as pernas
        scenario_key: chave do cenario em SCENARIOS
        magnitude: magnitude em bps
    """
    du_mid = (du_min + du_max) / 2
    du_range = (du_max - du_min) / 2 or 1
    t = max(-1, min(1, (du - du_mid) / du_range))

    if du_min == du_max and scenario_key in ("pos_fly", "neg_fly"):
        return 0.0

    if scenario_key == "custom":
        scale = magnitude / 10 if magnitude else 0
        return scale * (custom_parallel_bps + custom_slope_bps * t + custom_curvature_bps * (0.5 - 1.5 * t * t))
    sc = SCENARIOS.get(scenario_key)
    return sc.delta(t, magnitude) if sc else 0


def _parse_leg_date(value):
    if isinstance(value, date):
        return value
    if not isinstance(value, str) or not value:
        return None
    for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


def calc_leg_pnl(leg: dict, delta_bps: float,
                 delta_fx_pct: float = 0.0,
                 delta_ipca_bps: float = 0.0,
                 delta_cupom_bps: float = 0.0) -> float:
    """Calcula P&L de uma perna para choques multi-fator.

    Fatores:
    - delta_bps: variacao na taxa pre (bps) — aplica a DI1, LTN, NTN-F
    - delta_fx_pct: variacao % no spot USD/BRL — aplica a DOL
    - delta_ipca_bps: variacao na taxa real (bps) — aplica a NTN-B, DAP
    - delta_cupom_bps: variacao no cupom cambial (bps) — aplica a DDI, FRC

    Args:
        leg: dict com instrument, tax_fin, du, dc, direction, quantity, taxa
        delta_bps: variacao em bps para taxa pre
        delta_fx_pct: variacao % no spot USD/BRL (ex: +5 = dolar sobe 5%)
        delta_ipca_bps: variacao em bps na taxa real (IPCA)
        delta_cupom_bps: variacao em bps no cupom cambial
    """
    info = INSTRUMENTS[leg["instrument"]]
    inst = leg["instrument"]

    if info.conv == "price":
        sign = 1 if leg["direction"] == "C" else -1
        delta_pts = leg["taxa"] * delta_fx_pct / 100
        return sign * delta_pts * info.mult * leg["quantity"]

    # Choque total = cenario (delta_bps) + slider especifico (aditivo).
    # Para NTN-B/DAP: cenario aplica na curva real + slider delta_ipca adicional.
    # Para DDI/FRC: cenario aplica na curva cupom + slider delta_cupom adicional.
    # Para LTN/NTN-F/DI1/LFT: cenario aplica na curva pre (sem slider adicional).
    effective_delta = delta_bps
    if inst in ("NTN-B", "DAP"):
        effective_delta = delta_bps + delta_ipca_bps
    elif inst in ("DDI", "FRC"):
        effective_delta = delta_bps + delta_cupom_bps

    new_rate = leg["tax_fin"] + effective_delta / 100
    liq = _parse_leg_date(leg.get("liq"))
    venc = leg.get("parsed", {}).get("date") if isinstance(leg.get("parsed"), dict) else None
    leg_vna = leg.get("vna")
    new_pu = pu(leg["instrument"], new_rate, leg["du"], leg["dc"], liq, venc, vna=leg_vna)
    old_pu = pu(leg["instrument"], leg["tax_fin"], leg["du"], leg["dc"], liq, venc, vna=leg_vna)
    diff = new_pu - old_pu

    if info.type == "tpf":
        sign = 1 if leg["direction"] == "C" else -1
    else:
        sign = -1 if leg["direction"] == "C" else 1

    return sign * diff * leg["quantity"]


def calc_leg_pnl_per_flow(leg: dict,
                          scenario_key: str, magnitude: float,
                          du_min: int, du_max: int,
                          spot_curve_vertices: list[tuple[int, float]],
                          custom_parallel_bps: float = 0.0,
                          custom_slope_bps: float = 0.0,
                          custom_curvature_bps: float = 0.0,
                          delta_ipca_bps: float = 0.0) -> dict | None:
    """Per-cashflow MtM usando curva spot.

    Para cada fluxo k:
        i_k = curve(du_k) + spread_credito_constante
        delta_k = scenario_delta(du_k)
        old_pv_k = FC_k / (1 + i_k/100)^(du_k/252)
        new_pv_k = FC_k / (1 + (i_k + delta_k)/100)^(du_k/252)

    Soma dos new_pv_k = novo PU. P&L_perna = sign * (new_PU - old_PU) * qty.

    Returns dict com:
      - leg_pnl: P&L total da perna
      - flows: [{label, du, old_pv, new_pv, delta_bps, pnl_flow}]

    Returns None se nao for um titulo com cupom (use calc_leg_pnl).
    """
    info = INSTRUMENTS[leg["instrument"]]
    if info.cup_sem <= 0:
        return None
    if not spot_curve_vertices:
        return None

    inst = leg["instrument"]
    use_ipca = inst in ("NTN-B",)
    base_delta_override = delta_ipca_bps if use_ipca and delta_ipca_bps != 0 else None

    liq = _parse_leg_date(leg.get("liq"))
    venc = leg.get("parsed", {}).get("date") if isinstance(leg.get("parsed"), dict) else None
    leg_vna = leg.get("vna")
    coupon_flows = _coupon_cashflows(inst, liq, venc, leg["du"])

    if not coupon_flows:
        return None

    tir = leg["tax_fin"]
    curve_at_maturity = flat_forward_interp(spot_curve_vertices, leg["du"])
    if curve_at_maturity is None:
        return None
    spread = tir - curve_at_maturity

    vna_scale = (leg_vna / 100) if (inst == "NTN-B" and leg_vna and leg_vna > 0) else 1.0

    sign = 1 if leg["direction"] == "C" else -1

    rows = []
    old_pu = 0.0
    new_pu = 0.0
    for j, (payment_date, dui, nominal) in enumerate(coupon_flows, start=1):
        spot_k = flat_forward_interp(spot_curve_vertices, dui)
        if spot_k is None:
            spot_k = curve_at_maturity
        i_k = spot_k + spread

        if base_delta_override is not None:
            delta_k = base_delta_override
        else:
            delta_k = calc_scenario_delta(
                dui, du_min, du_max, scenario_key, magnitude,
                custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
            )

        t = dui / 252
        old_pv = nominal / (1 + i_k / 100) ** t
        new_pv = nominal / (1 + (i_k + delta_k / 100) / 100) ** t

        old_pv_brl = old_pv * vna_scale * leg["quantity"]
        new_pv_brl = new_pv * vna_scale * leg["quantity"]
        pnl_flow = sign * (new_pv_brl - old_pv_brl)

        old_pu += old_pv
        new_pu += new_pv

        label = "Principal+Cupom" if j == len(coupon_flows) else f"Cupom {j}"
        rows.append({
            "label": label,
            "payment_date": payment_date,
            "du": dui,
            "old_pv": old_pv * vna_scale,
            "new_pv": new_pv * vna_scale,
            "delta_bps": delta_k,
            "pnl_flow": pnl_flow,
        })

    leg_pnl = sign * (new_pu - old_pu) * vna_scale * leg["quantity"]

    return {
        "leg_pnl": leg_pnl,
        "old_pu": old_pu * vna_scale,
        "new_pu": new_pu * vna_scale,
        "flows": rows,
        "spread_credito": spread,
    }


def get_spot_curve_for_leg(leg: dict, di1_curve: list, dap_curve: list, liq_date) -> list[tuple[int, float]]:
    """Retorna a curva spot apropriada para a perna (DAP para NTN-B, DI1 para outros TPFs)."""
    inst = leg.get("instrument")
    if inst == "NTN-B":
        return build_dap_vertices(dap_curve, liq_date) if dap_curve else []
    return build_di_vertices(di1_curve, liq_date) if di1_curve else []
