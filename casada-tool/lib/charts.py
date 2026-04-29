"""Charts for the simulator — dark theme, full-width optimized."""

from __future__ import annotations
import plotly.graph_objects as go
from .instruments import INSTRUMENTS, _coupon_cashflows
from .scenarios import (
    calc_scenario_delta, calc_leg_pnl, calc_leg_pnl_per_flow, get_spot_curve_for_leg,
)
from .curves import (
    flat_forward_curve, flat_forward_curve_lin360,
    build_di_vertices, build_dap_vertices, build_frc_vertices,
    build_forward_curve, flat_forward_lin360, flat_forward_interp,
)


def _smart_leg_pnl(leg: dict, leg_delta: float, scenario_key: str, magnitude: float,
                   du_min: int, du_max: int,
                   spot_curve: list,
                   delta_fx_pct: float, delta_ipca_bps: float, delta_cupom_bps: float,
                   custom_p: float, custom_s: float, custom_c: float) -> float:
    """Use per-flow MtM if leg is coupon bond and curve is available; else use TIR-shift."""
    info = leg.get("info") or INSTRUMENTS.get(leg.get("instrument"))
    if info and info.cup_sem > 0 and spot_curve:
        result = calc_leg_pnl_per_flow(
            leg, scenario_key, magnitude, du_min, du_max, spot_curve,
            custom_p, custom_s, custom_c, delta_ipca_bps,
        )
        if result is not None:
            return result["leg_pnl"]
    return calc_leg_pnl(leg, leg_delta,
                        delta_fx_pct=delta_fx_pct,
                        delta_ipca_bps=delta_ipca_bps,
                        delta_cupom_bps=delta_cupom_bps)

COLORS = ["#58a6ff", "#f85149", "#3fb950", "#d29922", "#bc8cff", "#f778ba"]

_GRID = "rgba(100,100,100,0.15)"
_ZERO = "rgba(100,100,100,0.4)"
_GREEN = "#3fb950"
_RED = "#f85149"
_BLUE = "#58a6ff"
_MUTED = "#8b949e"


def _base_layout(title: str = "", height: int = 350) -> dict:
    return dict(
        template="none",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Inter, -apple-system, BlinkMacSystemFont, sans-serif",
            size=12, color="#c9d1d9"),
        title=dict(text=title, font=dict(size=13, color="#e6edf3"),
                   x=0, xanchor="left", y=0.98, yanchor="top"),
        margin=dict(l=60, r=20, t=60, b=50),
        height=height,
        legend=dict(
            orientation="h", yanchor="top", y=1.12, xanchor="left", x=0,
            font=dict(color="#c9d1d9", size=11),
            itemwidth=30, tracegroupgap=4),
    )


def _is_rate_leg(l: dict) -> bool:
    info = l.get("info")
    if not info:
        info = INSTRUMENTS.get(l.get("instrument"))
    return info is not None and info.conv != "price"


def _rate_du_range(legs: list[dict]) -> tuple[int, int]:
    rate_legs = [l for l in legs if _is_rate_leg(l)]
    if not rate_legs:
        return 0, 0
    return min(l["du"] for l in rate_legs), max(l["du"] for l in rate_legs)


def _leg_delta(l: dict, du_min: int, du_max: int,
               scenario_key: str, magnitude: float,
               custom_parallel_bps: float = 0.0,
               custom_slope_bps: float = 0.0,
               custom_curvature_bps: float = 0.0) -> float:
    if not _is_rate_leg(l):
        return 0.0
    return calc_scenario_delta(
        l["du"], du_min, du_max, scenario_key, magnitude,
        custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
    )


def _dir_label(l: dict) -> str:
    return "C" if l["direction"] == "C" else "V"


def _build_di_curve(di1_curve):
    """Converte lista de contratos B3 em (dus, rates) ordenados."""
    from lib.calendar import du_entre, default_liq_date
    from datetime import date
    data_neg = date.today()
    liq = default_liq_date(data_neg)
    pairs = []
    for c in di1_curve:
        rate = c.get("last", 0)
        if rate <= 0:
            rate = c.get("ajuste", 0)
        if rate <= 0:
            continue
        vp = c["vcto"].split("-")
        vd = date(int(vp[0]), int(vp[1]), int(vp[2]))
        du = du_entre(liq, vd)
        if du > 0:
            pairs.append((du, rate))
    pairs.sort()
    return [p[0] for p in pairs], [p[1] for p in pairs]


def _build_smooth_curve(di1_curve, du_step: int = 5):
    """Constroi curva DI suave via flat forward interpolation."""
    from lib.calendar import default_liq_date
    from datetime import date
    liq = default_liq_date(date.today())
    vertices = build_di_vertices(di1_curve, liq)
    if not vertices:
        return [], []
    smooth = flat_forward_curve(vertices, du_step)
    return [p[0] for p in smooth], [p[1] for p in smooth]


def _build_smooth_dap_curve(dap_contracts, du_step: int = 5):
    """Constroi curva DAP suave via flat forward interpolation."""
    from lib.calendar import default_liq_date
    from datetime import date
    liq = default_liq_date(date.today())
    vertices = build_dap_vertices(dap_contracts, liq)
    if not vertices:
        return [], []
    smooth = flat_forward_curve(vertices, du_step)
    return [p[0] for p in smooth], [p[1] for p in smooth]


_DAP_COLOR = "#d29922"


def chart_curva_antes_depois(legs: list[dict], scenario_key: str,
                              magnitude: float, di1_curve: list = None,
                              dap_curve: list = None,
                              custom_parallel_bps: float = 0.0,
                              custom_slope_bps: float = 0.0,
                              custom_curvature_bps: float = 0.0) -> go.Figure:
    """Curva de juros COMPLETA antes/depois do choque.

    Plota curva DI interpolada via flat forward (suave) e opcionalmente
    a curva DAP quando NTN-B esta na operacao. Pernas destacadas como pontos.
    """
    fig = go.Figure()

    rate_legs = sorted(
        [l for l in legs if _is_rate_leg(l)], key=lambda l: l["du"])

    if rate_legs:
        du_min_legs = min(l["du"] for l in rate_legs)
        du_max_legs = max(l["du"] for l in rate_legs)
    else:
        du_min_legs, du_max_legs = 0, 1000

    if di1_curve:
        try:
            smooth_dus, smooth_rates = _build_smooth_curve(di1_curve, du_step=5)

            if smooth_dus:
                fig.add_trace(go.Scatter(
                    x=smooth_dus, y=smooth_rates, mode="lines",
                    name="DI Antes",
                    line=dict(color=_MUTED, width=1.5, dash="dash"),
                    hovertemplate="DU: %{x}<br>Taxa: %{y:.3f}%<extra>Antes</extra>",
                ))

                curve_deltas = [
                    calc_scenario_delta(
                        du, du_min_legs, du_max_legs, scenario_key, magnitude,
                        custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                    )
                    for du in smooth_dus
                ]
                curve_after = [r + d / 100 for r, d in zip(smooth_rates, curve_deltas)]

                fig.add_trace(go.Scatter(
                    x=smooth_dus, y=curve_after, mode="lines",
                    name="DI Depois",
                    line=dict(color=_BLUE, width=2),
                    customdata=curve_deltas,
                    hovertemplate="DU: %{x}<br>Taxa: %{y:.3f}%<br>Delta: %{customdata:+.1f}bp<extra>Depois</extra>",
                ))

                fig.add_trace(go.Scatter(
                    x=smooth_dus + smooth_dus[::-1],
                    y=curve_after + smooth_rates[::-1],
                    fill="toself", fillcolor="rgba(88,166,255,0.06)",
                    line=dict(width=0), showlegend=False, hoverinfo="skip",
                ))
        except Exception:
            pass

    has_ntnb = any(l["instrument"] == "NTN-B" for l in legs)
    has_dap_leg = any(l["instrument"] == "DAP" for l in legs)
    if dap_curve and (has_ntnb or has_dap_leg):
        try:
            dap_dus, dap_rates = _build_smooth_dap_curve(dap_curve, du_step=5)
            if dap_dus:
                fig.add_trace(go.Scatter(
                    x=dap_dus, y=dap_rates, mode="lines",
                    name="DAP Antes",
                    line=dict(color=_DAP_COLOR, width=1.5, dash="dot"),
                    hovertemplate="DU: %{x}<br>Taxa real: %{y:.3f}%<extra>DAP Antes</extra>",
                ))

                dap_deltas = [
                    calc_scenario_delta(
                        du, du_min_legs, du_max_legs, scenario_key, magnitude,
                        custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                    )
                    for du in dap_dus
                ]
                dap_after = [r + d / 100 for r, d in zip(dap_rates, dap_deltas)]

                fig.add_trace(go.Scatter(
                    x=dap_dus, y=dap_after, mode="lines",
                    name="DAP Depois",
                    line=dict(color=_DAP_COLOR, width=2),
                    customdata=dap_deltas,
                    hovertemplate="DU: %{x}<br>Taxa real: %{y:.3f}%<br>Delta: %{customdata:+.1f}bp<extra>DAP Depois</extra>",
                ))
        except Exception:
            pass

    if rate_legs:
        _positions = ["top center", "bottom center", "top right", "bottom right",
                      "top left", "bottom left"]
        user_rate_legs = [l for l in rate_legs if not l.get("auto")]
        auto_rate_legs = [l for l in rate_legs if l.get("auto")]

        if len(auto_rate_legs) >= 3:
            auto_dus_b = [l["du"] for l in auto_rate_legs]
            auto_rates_b = [l["tax_fin"] for l in auto_rate_legs]
            auto_rates_a = []
            auto_labels = []
            auto_deltas = []
            for l in auto_rate_legs:
                d_k = calc_scenario_delta(
                    l["du"], du_min_legs, du_max_legs, scenario_key, magnitude,
                    custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                )
                auto_rates_a.append(l["tax_fin"] + d_k / 100)
                auto_labels.append(f"AUTO {l['instrument']} {l['parsed']['label']}")
                auto_deltas.append(d_k)
            hedge_inst = auto_rate_legs[0]["instrument"]
            fig.add_trace(go.Scatter(
                x=auto_dus_b, y=auto_rates_b, mode="markers",
                name=f"AUTO Hedge ({len(auto_rate_legs)} legs)",
                marker=dict(size=7, color="#d29922", symbol="diamond-open", line=dict(width=1.5, color="#d29922")),
                customdata=auto_labels,
                hovertemplate="%{customdata}<br>DU: %{x}<br>Taxa: %{y:.3f}%<extra>Antes</extra>",
                legendgroup="auto_hedge", showlegend=True,
                opacity=0.85,
            ))
            fig.add_trace(go.Scatter(
                x=auto_dus_b, y=auto_rates_a, mode="markers",
                marker=dict(size=8, color="#d29922", symbol="diamond"),
                customdata=list(zip(auto_labels, auto_deltas)),
                hovertemplate="%{customdata[0]}<br>DU: %{x}<br>Taxa: %{y:.3f}%<br>Delta: %{customdata[1]:+.1f}bp<extra>Depois</extra>",
                legendgroup="auto_hedge", showlegend=False,
            ))
            display_legs = user_rate_legs
        else:
            display_legs = rate_legs

        for i, l in enumerate(display_legs):
            info = l.get("info") or INSTRUMENTS.get(l.get("instrument"))
            is_coupon = info and info.cup_sem > 0
            delta = calc_scenario_delta(
                l["du"], du_min_legs, du_max_legs, scenario_key, magnitude,
                custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
            )
            after = l["tax_fin"] + delta / 100
            prefix = "AUTO " if l.get("auto") else ""
            lbl = f"{prefix}{_dir_label(l)} {l['instrument']} {l['parsed']['label']}"
            pos = _positions[i % len(_positions)]
            color = COLORS[i % len(COLORS)]

            fig.add_trace(go.Scatter(
                x=[l["du"]], y=[l["tax_fin"]], mode="markers",
                name=lbl,
                marker=dict(size=10, color=color, symbol="circle-open", line=dict(width=2, color=color)),
                hovertemplate=f"{lbl}<br>DU: %{{x}}<br>Taxa: %{{y:.3f}}%<extra>Antes</extra>",
                legendgroup=lbl, showlegend=True,
            ))
            fig.add_trace(go.Scatter(
                x=[l["du"]], y=[after], mode="markers+text",
                marker=dict(size=12, color=color, symbol="circle"),
                text=[f"{lbl} {delta:+.0f}bp"],
                textposition=pos, textfont=dict(size=10, color=color),
                hovertemplate=f"{lbl}<br>DU: %{{x}}<br>Taxa: %{{y:.3f}}%<br>Delta: {delta:+.1f}bp<extra>Depois</extra>",
                legendgroup=lbl, showlegend=False,
            ))

            if is_coupon and not l.get("auto"):
                cf_dict = l.get("cashflows", {})
                cashflows = cf_dict.get("flows") if isinstance(cf_dict, dict) else None
                if cashflows:
                    cf_dus = []
                    cf_rates_before = []
                    cf_rates_after = []
                    cf_labels = []
                    cf_deltas = []
                    for cf in cashflows:
                        if cf["label"].startswith("Principal"):
                            continue
                        d_k = calc_scenario_delta(
                            cf["du"], du_min_legs, du_max_legs, scenario_key, magnitude,
                            custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                        )
                        cf_dus.append(cf["du"])
                        cf_rates_before.append(l["tax_fin"])
                        cf_rates_after.append(l["tax_fin"] + d_k / 100)
                        cf_labels.append(cf["label"])
                        cf_deltas.append(d_k)
                    if cf_dus:
                        fig.add_trace(go.Scatter(
                            x=cf_dus, y=cf_rates_before, mode="markers",
                            marker=dict(size=5, color=color, symbol="diamond-open"),
                            customdata=cf_labels,
                            hovertemplate=f"{lbl} %{{customdata}}<br>DU: %{{x}}<br>Taxa: %{{y:.3f}}%<extra>Antes</extra>",
                            legendgroup=lbl, showlegend=False,
                            opacity=0.6,
                        ))
                        fig.add_trace(go.Scatter(
                            x=cf_dus, y=cf_rates_after, mode="markers",
                            marker=dict(size=6, color=color, symbol="diamond"),
                            customdata=list(zip(cf_labels, cf_deltas)),
                            hovertemplate=f"{lbl} %{{customdata[0]}}<br>DU: %{{x}}<br>Taxa: %{{y:.3f}}%<br>Delta: %{{customdata[1]:+.1f}}bp<extra>Depois</extra>",
                            legendgroup=lbl, showlegend=False,
                            opacity=0.85,
                        ))

    fig.update_layout(
        **_base_layout("Curva de Juros — Flat Forward", 450),
        xaxis=dict(title="Prazo (DU)", gridcolor=_GRID, rangemode="tozero"),
        yaxis=dict(title="Taxa (% a.a.)", tickformat=".2f", gridcolor=_GRID),
    )
    return fig


def chart_pnl_barras(legs: list[dict], scenario_key: str,
                      magnitude: float,
                      delta_fx_pct: float = 0.0,
                      delta_ipca_bps: float = 0.0,
                      delta_cupom_bps: float = 0.0,
                      custom_parallel_bps: float = 0.0,
                      custom_slope_bps: float = 0.0,
                      custom_curvature_bps: float = 0.0,
                      di1_curve: list = None,
                      dap_curve: list = None) -> go.Figure:
    du_min, du_max = _rate_du_range(legs)

    leg_pnls = []
    for l in legs:
        delta = _leg_delta(
            l, du_min, du_max, scenario_key, magnitude,
            custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
        )
        spot = get_spot_curve_for_leg(l, di1_curve or [], dap_curve or [], l.get("liq"))
        pnl = _smart_leg_pnl(
            l, delta, scenario_key, magnitude, du_min, du_max, spot,
            delta_fx_pct, delta_ipca_bps, delta_cupom_bps,
            custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
        )
        leg_pnls.append((l, pnl))

    auto_legs = [(l, p) for l, p in leg_pnls if l.get("auto")]
    user_legs_pnl = [(l, p) for l, p in leg_pnls if not l.get("auto")]

    names, pnls, colors = [], [], []

    if len(auto_legs) >= 3:
        for l, p in user_legs_pnl:
            names.append(f"{_dir_label(l)} {l['instrument']} {l['parsed']['label']}")
            pnls.append(p)
            colors.append(_GREEN if p >= 0 else _RED)
        auto_total = sum(p for _, p in auto_legs)
        first_auto = auto_legs[0][0]
        hedge_inst = first_auto["instrument"]
        names.append(f"AUTO {hedge_inst} Hedge ({len(auto_legs)} legs)")
        pnls.append(auto_total)
        colors.append("#d29922")
    else:
        for l, p in leg_pnls:
            prefix = "AUTO " if l.get("auto") else ""
            names.append(f"{prefix}{_dir_label(l)} {l['instrument']} {l['parsed']['label']}")
            pnls.append(p)
            colors.append(_GREEN if p >= 0 else _RED)

    total = sum(pnls)
    names.append("TOTAL")
    pnls.append(total)
    colors.append(_BLUE)

    fig = go.Figure(go.Bar(
        y=names, x=pnls, orientation="h",
        marker_color=colors,
        text=[f"R$ {v:+,.0f}" for v in pnls],
        textposition="outside", textfont=dict(size=11),
    ))
    fig.update_layout(
        **_base_layout("P&L por Perna (R$)", 50 + len(names) * 45),
        xaxis=dict(
            title="P&L (R$)", zeroline=True,
            zerolinecolor=_ZERO, gridcolor=_GRID),
        yaxis=dict(autorange="reversed"),
        showlegend=False,
    )
    return fig


def chart_pnl_consolidado(legs: list[dict],
                           scenario_key: str = "bear_par",
                           magnitude: float = 10.0,
                           delta_fx_pct: float = 0.0,
                           delta_ipca_bps: float = 0.0,
                           delta_cupom_bps: float = 0.0,
                           custom_parallel_bps: float = 0.0,
                           custom_slope_bps: float = 0.0,
                           custom_curvature_bps: float = 0.0,
                           di1_curve: list = None,
                           dap_curve: list = None) -> go.Figure:
    deltas_range = list(range(-20, 21))
    du_min, du_max = _rate_du_range(legs)
    spot_per_leg = [get_spot_curve_for_leg(l, di1_curve or [], dap_curve or [], l.get("liq")) for l in legs]
    total_pnl = []
    for d in deltas_range:
        t = 0.0
        for li, l in enumerate(legs):
            leg_d = _leg_delta(
                l, du_min, du_max, scenario_key, d,
                custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
            )
            t += _smart_leg_pnl(
                l, leg_d, scenario_key, d, du_min, du_max, spot_per_leg[li],
                delta_fx_pct, delta_ipca_bps, delta_cupom_bps,
                custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
            )
        total_pnl.append(t)

    colors = [_GREEN if v >= 0 else _RED for v in total_pnl]

    fig = go.Figure(go.Bar(x=deltas_range, y=total_pnl, marker_color=colors))
    fig.update_layout(
        **_base_layout("P&L Consolidado — Cenário Selecionado", 350),
        xaxis=dict(title="Delta (bps)", dtick=5, gridcolor=_GRID),
        yaxis=dict(
            title="P&L (R$)", zeroline=True,
            zerolinecolor=_ZERO, gridcolor=_GRID),
        showlegend=False,
    )
    return fig


def chart_pnl_por_perna(legs: list[dict],
                         scenario_key: str = "bear_par",
                         magnitude: float = 10.0,
                         delta_fx_pct: float = 0.0,
                         delta_ipca_bps: float = 0.0,
                         delta_cupom_bps: float = 0.0,
                         custom_parallel_bps: float = 0.0,
                         custom_slope_bps: float = 0.0,
                         custom_curvature_bps: float = 0.0,
                         di1_curve: list = None,
                         dap_curve: list = None,
                         expand_flows: bool = False) -> go.Figure:
    deltas_range = list(range(-20, 21))
    du_min, du_max = _rate_du_range(legs)
    fig = go.Figure()
    color_idx = 0

    auto_legs = [l for l in legs if l.get("auto")]
    user_legs = [l for l in legs if not l.get("auto")]
    aggregate_auto = len(auto_legs) >= 3 and not expand_flows

    for i, l in enumerate(user_legs):
        info = l.get("info") or INSTRUMENTS.get(l.get("instrument"))
        name = f"{_dir_label(l)} {l['instrument']} {l['parsed']['label']}"
        spot = get_spot_curve_for_leg(l, di1_curve or [], dap_curve or [], l.get("liq"))
        is_coupon = info and info.cup_sem > 0
        base_color = COLORS[color_idx % len(COLORS)]
        color_idx += 1

        if expand_flows and is_coupon and spot:
            cashflows = l.get("cashflows", {}).get("flows") or []
            for k_idx, cf in enumerate(cashflows):
                pnls = []
                for d in deltas_range:
                    res = calc_leg_pnl_per_flow(
                        l, scenario_key, d, du_min, du_max, spot,
                        custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                        delta_ipca_bps,
                    )
                    pnls.append(res["flows"][k_idx]["pnl_flow"] if res else 0)
                width = 2 if cf["label"].startswith("Principal") else 1
                opacity = 1.0 if cf["label"].startswith("Principal") else 0.55
                fig.add_trace(go.Scatter(
                    x=deltas_range, y=pnls, mode="lines",
                    name=f"{name} - {cf['label']}",
                    line=dict(color=base_color, width=width),
                    opacity=opacity,
                ))
        elif _is_rate_leg(l):
            pnls = []
            for d in deltas_range:
                leg_d = _leg_delta(
                    l, du_min, du_max, scenario_key, d,
                    custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                )
                pnls.append(_smart_leg_pnl(
                    l, leg_d, scenario_key, d, du_min, du_max, spot,
                    delta_fx_pct, delta_ipca_bps, delta_cupom_bps,
                    custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                ))
            fig.add_trace(go.Scatter(
                x=deltas_range, y=pnls, mode="lines", name=name,
                line=dict(color=base_color, width=2),
            ))
        else:
            pnls = [calc_leg_pnl(l, 0,
                                 delta_fx_pct=delta_fx_pct,
                                 delta_ipca_bps=delta_ipca_bps,
                                 delta_cupom_bps=delta_cupom_bps)
                    for _ in deltas_range]
            fig.add_trace(go.Scatter(
                x=deltas_range, y=pnls, mode="lines", name=name,
                line=dict(color=base_color, width=2),
            ))

    if aggregate_auto:
        hedge_inst = auto_legs[0]["instrument"]
        agg_pnls = []
        for d in deltas_range:
            tot = 0.0
            for l in auto_legs:
                spot = get_spot_curve_for_leg(l, di1_curve or [], dap_curve or [], l.get("liq"))
                leg_d = _leg_delta(
                    l, du_min, du_max, scenario_key, d,
                    custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                )
                tot += _smart_leg_pnl(
                    l, leg_d, scenario_key, d, du_min, du_max, spot,
                    delta_fx_pct, delta_ipca_bps, delta_cupom_bps,
                    custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                )
            agg_pnls.append(tot)
        fig.add_trace(go.Scatter(
            x=deltas_range, y=agg_pnls, mode="lines",
            name=f"AUTO {hedge_inst} Hedge ({len(auto_legs)} legs)",
            line=dict(color="#d29922", width=2.5, dash="dot"),
        ))
    elif auto_legs:
        for l in auto_legs:
            spot = get_spot_curve_for_leg(l, di1_curve or [], dap_curve or [], l.get("liq"))
            base_color = COLORS[color_idx % len(COLORS)]
            color_idx += 1
            pnls = []
            for d in deltas_range:
                leg_d = _leg_delta(
                    l, du_min, du_max, scenario_key, d,
                    custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                )
                pnls.append(_smart_leg_pnl(
                    l, leg_d, scenario_key, d, du_min, du_max, spot,
                    delta_fx_pct, delta_ipca_bps, delta_cupom_bps,
                    custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
                ))
            fig.add_trace(go.Scatter(
                x=deltas_range, y=pnls, mode="lines",
                name=f"AUTO {_dir_label(l)} {l['instrument']} {l['parsed']['label']}",
                line=dict(color=base_color, width=1.5, dash="dash"),
            ))

    fig.update_layout(
        **_base_layout("P&L por Perna — Cenário Selecionado", 350),
        xaxis=dict(title="Delta (bps)", dtick=5, gridcolor=_GRID),
        yaxis=dict(
            title="P&L (R$)", zeroline=True,
            zerolinecolor=_ZERO, gridcolor=_GRID),
    )
    return fig


_FRC_COLOR = "#bc8cff"
_FWD_COLOR = "#3fb950"


def chart_cupom_cambial(frc_contracts: list, delta_cupom_bps: float = 0.0,
                         legs: list[dict] = None) -> go.Figure:
    """Curva de cupom cambial (FRC) antes/depois do choque."""
    from lib.calendar import default_liq_date
    from datetime import date

    fig = go.Figure()
    liq = default_liq_date(date.today())
    vertices = build_frc_vertices(frc_contracts, liq)
    if not vertices:
        fig.update_layout(**_base_layout("Cupom Cambial — sem dados", 400))
        return fig

    smooth = flat_forward_curve_lin360(vertices, dc_step=5)
    if not smooth:
        fig.update_layout(**_base_layout("Cupom Cambial — sem dados", 400))
        return fig

    dcs_before = [p[0] for p in smooth]
    rates_before = [p[1] for p in smooth]

    fig.add_trace(go.Scatter(
        x=dcs_before, y=rates_before, mode="lines",
        name="Cupom Antes",
        line=dict(color=_MUTED, width=1.5, dash="dash"),
        hovertemplate="DC: %{x}<br>Cupom: %{y:.3f}%<extra>Antes</extra>",
    ))

    rates_after = [r + delta_cupom_bps / 100 for r in rates_before]
    fig.add_trace(go.Scatter(
        x=dcs_before, y=rates_after, mode="lines",
        name="Cupom Depois",
        line=dict(color=_FRC_COLOR, width=2),
        hovertemplate="DC: %{x}<br>Cupom: %{y:.3f}%<extra>Depois</extra>",
    ))

    fig.add_trace(go.Scatter(
        x=dcs_before + dcs_before[::-1],
        y=rates_after + rates_before[::-1],
        fill="toself", fillcolor="rgba(188,140,255,0.06)",
        line=dict(width=0), showlegend=False, hoverinfo="skip",
    ))

    vert_dcs = [v[0] for v in vertices]
    vert_rates = [v[1] for v in vertices]
    fig.add_trace(go.Scatter(
        x=vert_dcs, y=vert_rates, mode="markers",
        name="Vertices FRC",
        marker=dict(size=5, color=_FRC_COLOR, symbol="diamond"),
        hovertemplate="DC: %{x}<br>Cupom: %{y:.3f}%<extra>Vertice</extra>",
    ))

    if legs:
        cupom_legs = [l for l in legs if l["instrument"] in ("FRC", "DDI")]
        for i, l in enumerate(cupom_legs):
            lbl = f"{_dir_label(l)} {l['instrument']} {l['parsed']['label']}"
            fig.add_trace(go.Scatter(
                x=[l["dc"]], y=[l["tax_fin"]], mode="markers+text",
                name=lbl,
                marker=dict(size=10, color=_FRC_COLOR, symbol="circle"),
                text=[lbl], textposition="top center",
                textfont=dict(size=10, color=_FRC_COLOR),
                hovertemplate=f"{lbl}<br>DC: %{{x}}<br>Taxa: %{{y:.3f}}%<extra></extra>",
            ))

    fig.update_layout(
        **_base_layout("Cupom Cambial Limpo (FRC) — lin360", 400),
        xaxis=dict(title="Prazo (DC)", gridcolor=_GRID),
        yaxis=dict(title="Cupom (% a.a. lin360)", tickformat=".2f", gridcolor=_GRID),
    )
    return fig


def chart_dol_forward(di1_contracts: list, frc_contracts: list,
                       spot: float, delta_pre_bps: float = 0.0,
                       delta_cupom_bps: float = 0.0,
                       delta_fx_pct: float = 0.0,
                       legs: list[dict] = None) -> go.Figure:
    """Curva de dolar forward implicito antes/depois dos choques."""
    from lib.calendar import default_liq_date
    from datetime import date

    fig = go.Figure()
    liq = default_liq_date(date.today())
    di_verts = build_di_vertices(di1_contracts, liq)
    frc_verts = build_frc_vertices(frc_contracts, liq)

    if not di_verts or not frc_verts or spot <= 0:
        fig.update_layout(**_base_layout("Dolar Forward — sem dados", 400))
        return fig

    fwd_curve = build_forward_curve(di_verts, frc_verts, spot, liq)
    if not fwd_curve:
        fig.update_layout(**_base_layout("Dolar Forward — sem dados", 400))
        return fig

    dus = [p[0] for p in fwd_curve]
    fwds_before = [p[2] for p in fwd_curve]

    fig.add_trace(go.Scatter(
        x=dus, y=fwds_before, mode="lines",
        name="Forward Antes",
        line=dict(color=_MUTED, width=1.5, dash="dash"),
        hovertemplate="DU: %{x}<br>Fwd: R$ %{y:.4f}<extra>Antes</extra>",
    ))

    spot_after = spot * (1 + delta_fx_pct / 100)
    di_verts_after = [(du, r + delta_pre_bps / 100) for du, r in di_verts]
    frc_verts_after = [(dc, r + delta_cupom_bps / 100) for dc, r in frc_verts]
    fwd_after_curve = build_forward_curve(di_verts_after, frc_verts_after, spot_after, liq)
    fwds_after = [p[2] for p in fwd_after_curve] if fwd_after_curve else fwds_before

    fig.add_trace(go.Scatter(
        x=dus[:len(fwds_after)], y=fwds_after, mode="lines",
        name="Forward Depois",
        line=dict(color=_FWD_COLOR, width=2),
        hovertemplate="DU: %{x}<br>Fwd: R$ %{y:.4f}<extra>Depois</extra>",
    ))

    fig.add_trace(go.Scatter(
        x=dus[:len(fwds_after)] + dus[:len(fwds_after)][::-1],
        y=fwds_after + fwds_before[:len(fwds_after)][::-1],
        fill="toself", fillcolor="rgba(63,185,80,0.06)",
        line=dict(width=0), showlegend=False, hoverinfo="skip",
    ))

    fig.add_hline(y=spot, line_dash="dot", line_color=_MUTED,
                  annotation_text=f"Spot {spot:.4f}", annotation_font_color=_MUTED)

    if legs:
        dol_legs = [l for l in legs if l["instrument"] == "DOL"]
        for l in dol_legs:
            lbl = f"{_dir_label(l)} DOL {l['parsed']['label']}"
            fig.add_trace(go.Scatter(
                x=[l["du"]], y=[l["taxa"] / 1000], mode="markers+text",
                name=lbl,
                marker=dict(size=10, color=_FWD_COLOR, symbol="circle"),
                text=[lbl], textposition="top center",
                textfont=dict(size=10, color=_FWD_COLOR),
                hovertemplate=f"{lbl}<br>DU: %{{x}}<br>Cotacao: %{{y:.4f}}<extra></extra>",
            ))

    fig.update_layout(
        **_base_layout("Dolar Forward Implicito (paridade coberta)", 400),
        xaxis=dict(title="Prazo (DU)", gridcolor=_GRID),
        yaxis=dict(title="R$/USD", tickformat=".4f", gridcolor=_GRID),
    )
    return fig


def chart_taxa_real(dap_contracts: list, delta_ipca_bps: float = 0.0,
                     legs: list[dict] = None) -> go.Figure:
    """Curva DAP (taxa real IPCA) antes/depois do choque."""
    from lib.calendar import default_liq_date
    from datetime import date

    fig = go.Figure()
    liq = default_liq_date(date.today())
    vertices = build_dap_vertices(dap_contracts, liq)
    if not vertices:
        fig.update_layout(**_base_layout("Taxa Real (DAP) — sem dados", 400))
        return fig

    smooth = flat_forward_curve(vertices, du_step=5)
    if not smooth:
        fig.update_layout(**_base_layout("Taxa Real (DAP) — sem dados", 400))
        return fig

    dus = [p[0] for p in smooth]
    rates_before = [p[1] for p in smooth]

    fig.add_trace(go.Scatter(
        x=dus, y=rates_before, mode="lines",
        name="DAP Antes",
        line=dict(color=_MUTED, width=1.5, dash="dash"),
        hovertemplate="DU: %{x}<br>Taxa real: %{y:.3f}%<extra>Antes</extra>",
    ))

    rates_after = [r + delta_ipca_bps / 100 for r in rates_before]
    fig.add_trace(go.Scatter(
        x=dus, y=rates_after, mode="lines",
        name="DAP Depois",
        line=dict(color=_DAP_COLOR, width=2),
        hovertemplate="DU: %{x}<br>Taxa real: %{y:.3f}%<extra>Depois</extra>",
    ))

    fig.add_trace(go.Scatter(
        x=dus + dus[::-1],
        y=rates_after + rates_before[::-1],
        fill="toself", fillcolor="rgba(210,153,34,0.06)",
        line=dict(width=0), showlegend=False, hoverinfo="skip",
    ))

    vert_dus = [v[0] for v in vertices]
    vert_rates = [v[1] for v in vertices]
    fig.add_trace(go.Scatter(
        x=vert_dus, y=vert_rates, mode="markers",
        name="Vertices DAP",
        marker=dict(size=5, color=_DAP_COLOR, symbol="diamond"),
        hovertemplate="DU: %{x}<br>Taxa: %{y:.3f}%<extra>Vertice</extra>",
    ))

    if legs:
        ipca_legs = [l for l in legs if l["instrument"] in ("NTN-B", "DAP")]
        for l in ipca_legs:
            lbl = f"{_dir_label(l)} {l['instrument']} {l['parsed']['label']}"
            fig.add_trace(go.Scatter(
                x=[l["du"]], y=[l["tax_fin"]], mode="markers+text",
                name=lbl,
                marker=dict(size=10, color=_DAP_COLOR, symbol="circle"),
                text=[lbl], textposition="top center",
                textfont=dict(size=10, color=_DAP_COLOR),
                hovertemplate=f"{lbl}<br>DU: %{{x}}<br>Taxa: %{{y:.3f}}%<extra></extra>",
            ))

    fig.update_layout(
        **_base_layout("Taxa Real (DAP) — Cupom IPCA", 400),
        xaxis=dict(title="Prazo (DU)", gridcolor=_GRID),
        yaxis=dict(title="Taxa real (% a.a.)", tickformat=".2f", gridcolor=_GRID),
    )
    return fig


def chart_krd(flows: list) -> go.Figure:
    labels = [f.label for f in flows]
    krds = [f.krd for f in flows]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=labels, y=krds, name="KRD",
        marker_color=_BLUE,
        text=[f"{v:.3f}" for v in krds],
        textposition="outside", textfont=dict(size=10),
    ))
    fig.update_layout(
        **_base_layout("Key-Rate Duration por Fluxo", 300),
        xaxis=dict(title="Fluxo", gridcolor=_GRID),
        yaxis=dict(title="KRD (anos)", gridcolor=_GRID),
        showlegend=False,
    )
    return fig
