import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { Shield, Loader2, TrendingDown, TrendingUp, Zap } from "lucide-react";
import { portfolioHedge, portfolioScenario, type HedgeResult, type ScenarioResult } from "@/api/client";
import { usePortfolioStore, type Bond } from "@/stores/portfolio";
import { formatBRL } from "@/lib/utils";

export default function HedgePanel() {
  const bonds = usePortfolioStore((s) => s.bonds);
  const [hedgeRate, setHedgeRate] = useState(12.0);
  const [hedgeDu, setHedgeDu] = useState(252);
  const [shockBps, setShockBps] = useState(50);

  const hedgeMut = useMutation({ mutationFn: () => portfolioHedge(payload(bonds), hedgeRate, hedgeDu) });
  const scenarioMut = useMutation({ mutationFn: () => portfolioScenario(payload(bonds), shockBps) });

  if (bonds.length === 0) return null;

  return (
    <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
      {/* Hedge */}
      <div className="card p-6">
        <h4 className="mb-4 flex items-center gap-2 text-[14px] font-semibold text-txt">
          <Shield size={16} className="text-accent" /> Calculadora de Hedge
        </h4>
        <div className="mb-4 grid grid-cols-2 gap-3">
          <div>
            <label className="label-field">Taxa DI (% a.a.)</label>
            <input type="number" step="0.01" value={hedgeRate} onChange={(e) => setHedgeRate(Number(e.target.value))} className="input-field mono" />
          </div>
          <div>
            <label className="label-field">Prazo do Hedge (DU)</label>
            <input type="number" value={hedgeDu} onChange={(e) => setHedgeDu(Number(e.target.value))} className="input-field mono" />
          </div>
        </div>
        <button onClick={() => hedgeMut.mutate()} disabled={hedgeMut.isPending} className="btn-primary w-full">
          {hedgeMut.isPending ? <Loader2 size={16} className="animate-spin" /> : "Calcular Hedge"}
        </button>

        {hedgeMut.data && (
          <div className="mt-5">
            <h5 className="label-field mb-3">Resultado do Hedge</h5>
            <div className="grid grid-cols-3 gap-3">
              <div className="card px-4 py-4 text-center">
                <div className="label-field">Contratos</div>
                <div className="mono text-2xl font-bold text-accent">{hedgeMut.data.contracts_needed}</div>
                <div className="mt-1 text-[11px] text-txt-muted">{hedgeMut.data.direction.includes("sell") ? "VENDER" : "COMPRAR"} DI1</div>
              </div>
              <div className="card px-4 py-4 text-center">
                <div className="label-field">DV01 Carteira</div>
                <div className="mono text-lg font-bold text-txt">R$ {formatBRL(hedgeMut.data.portfolio_dv01, 2)}</div>
              </div>
              <div className="card px-4 py-4 text-center">
                <div className="label-field">DV01 Residual</div>
                <div className="mono text-lg font-bold text-txt">R$ {formatBRL(hedgeMut.data.residual_dv01, 2)}</div>
              </div>
            </div>
          </div>
        )}
        {hedgeMut.error && <p className="mt-3 text-[13px] text-danger">{(hedgeMut.error as Error).message}</p>}
      </div>

      {/* Scenario */}
      <div className="card p-6">
        <h4 className="mb-4 flex items-center gap-2 text-[14px] font-semibold text-txt">
          <Zap size={16} className="text-warning" /> Simulacao de Cenario
        </h4>
        <div className="mb-4">
          <label className="label-field">Choque Paralelo (bps)</label>
          <input type="number" value={shockBps} onChange={(e) => setShockBps(Number(e.target.value))} className="input-field mono" />
          <p className="mt-1 text-[11px] text-txt-muted">Positivo = alta de taxa. Negativo = queda.</p>
        </div>
        <button onClick={() => scenarioMut.mutate()} disabled={scenarioMut.isPending} className="btn-primary w-full">
          {scenarioMut.isPending ? <Loader2 size={16} className="animate-spin" /> : "Simular"}
        </button>

        {scenarioMut.data && (
          <div className="mt-5">
            <h5 className="label-field mb-3">Resultado</h5>
            <div className="card p-5">
              <div className="flex items-center gap-3">
                {scenarioMut.data.total_pnl_2nd_order < 0
                  ? <TrendingDown size={20} className="text-danger" />
                  : <TrendingUp size={20} className="text-success" />}
                <div>
                  <div className={`mono text-2xl font-bold ${scenarioMut.data.total_pnl_2nd_order < 0 ? "text-danger" : "text-success"}`}>
                    R$ {formatBRL(scenarioMut.data.total_pnl_2nd_order, 0)}
                  </div>
                  <div className="text-[12px] text-txt-muted">
                    {scenarioMut.data.shock_bps > 0 ? "+" : ""}{scenarioMut.data.shock_bps} bps &middot; {formatBRL(scenarioMut.data.total_pnl_pct, 2)}%
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
        {scenarioMut.error && <p className="mt-3 text-[13px] text-danger">{(scenarioMut.error as Error).message}</p>}
      </div>
    </div>
  );
}

function payload(bonds: Bond[]) {
  return bonds.map((b) => ({
    id: b.id, type: b.type, notional: b.notional, quantity: b.quantity,
    rate: b.rate, settlement_date: b.settlement_date, maturity_date: b.maturity_date,
    vna: b.vna, premium_bps: b.premium_bps, current_rate: b.current_rate,
  }));
}
