import { formatBRL } from "@/lib/utils";
import type { PortfolioRiskResult } from "@/api/client";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from "recharts";

interface Props { data: PortfolioRiskResult; }

const BUCKET_ORDER = ["0-3M", "3-6M", "6-12M", "1-2Y", "2-5Y", "5-10Y", "10Y+"];
const BAR_COLORS = ["#3b82f6", "#6366f1", "#818cf8", "#a78bfa", "#c084fc", "#e879f9", "#f472b6"];

export default function RiskDashboard({ data }: Props) {
  const maturityData = BUCKET_ORDER
    .filter((b) => data.exposure_by_maturity_bucket[b])
    .map((bucket, i) => ({ name: bucket, value: data.exposure_by_maturity_bucket[bucket] || 0, color: BAR_COLORS[i % BAR_COLORS.length] }));

  const typeData = Object.entries(data.exposure_by_type).map(([name, value]) => ({ name, value }));

  return (
    <div className="space-y-4">
      {/* Metric Cards */}
      <div className="grid grid-cols-2 gap-3 lg:grid-cols-6">
        <MC label="Titulos" value={`R$ ${formatBRL(data.total_market_value, 2)}`} sub={`${data.bonds.length} posicoes`} />
        <MC label="DV01 Total" value={`R$ ${formatBRL(data.total_dv01, 2)}`} highlight />
        <MC label="Duration Mod." value={formatBRL(data.weighted_duration_mod, 4)} sub="anos (ponderada)" />
        <MC label="Duration ANBIMA" value={`${formatBRL(data.weighted_duration_anbima, 0)} DU`} />
        <MC label="Convexidade" value={formatBRL(data.weighted_convexity, 4)} />
        <MC label="Prazo Medio" value={`${formatBRL(data.weighted_duration_anbima / 252, 1)} anos`} sub={`${formatBRL(data.weighted_duration_anbima, 0)} DU`} />
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <div className="card p-5">
          <h4 className="label-field mb-4">Exposicao por Vencimento</h4>
          {maturityData.length > 0 ? (
            <ResponsiveContainer width="100%" height={240}>
              <BarChart data={maturityData} barCategoryGap="20%">
                <XAxis dataKey="name" tick={{ fill: "#64748b", fontSize: 11 }} axisLine={false} tickLine={false} />
                <YAxis tick={{ fill: "#64748b", fontSize: 11, fontFamily: "JetBrains Mono" }} axisLine={false} tickLine={false} width={55}
                  tickFormatter={(v: number) => `${(v / 1e6).toFixed(1)}M`} />
                <Tooltip
                  contentStyle={{ background: "#111827", border: "1px solid #1e293b", borderRadius: 8, fontSize: 13, fontFamily: "JetBrains Mono" }}
                  labelStyle={{ color: "#e2e8f0" }}
                  formatter={(v: number) => [`R$ ${formatBRL(v, 0)}`, "Exposicao"]}
                  cursor={{ fill: "rgba(255,255,255,0.02)" }} />
                <Bar dataKey="value" radius={[4, 4, 0, 0]}>
                  {maturityData.map((e, i) => <Cell key={i} fill={e.color} />)}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          ) : <p className="py-10 text-center text-txt-muted">Sem dados</p>}
        </div>

        <div className="card p-5">
          <h4 className="label-field mb-4">Distribuicao por Tipo</h4>
          <div className="space-y-5">
            {typeData.map(({ name, value }) => {
              const pct = data.total_market_value > 0 ? (value / data.total_market_value) * 100 : 0;
              return (
                <div key={name}>
                  <div className="mb-2 flex items-baseline justify-between">
                    <span className="text-[14px] font-semibold text-txt">{name}</span>
                    <span className="mono text-[14px] text-txt">R$ {formatBRL(value, 2)}
                      <span className="ml-2 text-[12px] text-txt-muted">{formatBRL(pct, 1)}%</span>
                    </span>
                  </div>
                  <div className="h-2 overflow-hidden rounded-full bg-card-hover">
                    <div className="h-full rounded-full bg-accent transition-all duration-500" style={{ width: `${pct}%` }} />
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

function MC({ label, value, sub, highlight }: { label: string; value: string; sub?: string; highlight?: boolean }) {
  return (
    <div className="card px-5 py-4">
      <div className="label-field">{label}</div>
      <div className={`mt-1 mono text-xl font-bold ${highlight ? "text-accent" : "text-txt"}`}>{value}</div>
      {sub && <div className="mt-0.5 text-[11px] text-txt-muted">{sub}</div>}
    </div>
  );
}
