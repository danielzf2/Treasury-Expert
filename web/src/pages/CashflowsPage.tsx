import { useMemo } from "react";
import { useQuery } from "@tanstack/react-query";
import { Loader2, CalendarDays, DollarSign, Hash } from "lucide-react";
import { portfolioCashflows, fetchVna, type CashflowItem, type VnaResponse } from "@/api/client";
import { usePortfolioStore } from "@/stores/portfolio";
import { formatBRL } from "@/lib/utils";
import { colorForType, TYPE_COLORS } from "@/lib/constants";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Legend,
} from "recharts";

export default function CashflowsPage() {
  const bonds = usePortfolioStore((s) => s.bonds);

  const { data: vnaData } = useQuery<VnaResponse>({
    queryKey: ["vna"],
    queryFn: fetchVna,
    staleTime: 1000 * 60 * 30,
  });

  const { data, isLoading, error } = useQuery({
    queryKey: ["cashflows", bonds.map((b) => b.id).join(",")],
    queryFn: () =>
      portfolioCashflows(
        bonds.map((b) => ({
          id: b.id, type: b.type, notional: b.notional, quantity: b.quantity,
          rate: b.rate, settlement_date: b.settlement_date, maturity_date: b.maturity_date,
          vna: b.vna, premium_bps: b.premium_bps, current_rate: b.current_rate,
        }))
      ),
    enabled: bonds.length > 0,
    staleTime: 1000 * 60 * 5,
  });

  const bondTypes = useMemo(() => {
    const types = new Set<string>();
    if (data?.flows) data.flows.forEach((f) => types.add(f.bond_type));
    return Array.from(types).sort();
  }, [data]);

  const chartData = useMemo(() => {
    if (!data?.flows) return [];
    const byMonth = new Map<string, Record<string, number> & { month: string }>();
    for (const f of data.flows) {
      let entry = byMonth.get(f.month_key);
      if (!entry) {
        entry = { month: f.date_label } as Record<string, number> & { month: string };
        byMonth.set(f.month_key, entry);
      }
      entry[f.bond_type] = (entry[f.bond_type] as number || 0) + f.amount;
    }
    return Array.from(byMonth.entries())
      .sort(([a], [b]) => a.localeCompare(b))
      .map(([, v]) => v);
  }, [data]);

  if (bonds.length === 0) {
    return (
      <div className="flex h-full flex-col">
        <div className="flex h-12 shrink-0 items-center border-b border-border bg-base px-5">
          <span className="text-[15px] font-semibold text-txt">Fluxos de Caixa</span>
        </div>
        <div className="flex flex-1 items-center justify-center">
          <div className="text-center">
            <CalendarDays size={40} className="mx-auto mb-3 text-txt-muted" />
            <p className="text-[14px] text-txt-muted">Nenhum titulo na carteira.</p>
            <p className="text-[13px] text-txt-muted mt-1">Adicione titulos na aba <strong className="text-txt">Carteira</strong> para ver os fluxos.</p>
          </div>
        </div>
      </div>
    );
  }

  const summary = data?.summary;

  return (
    <div className="flex h-full flex-col">
      <div className="shrink-0 border-b border-border bg-base px-5 py-3">
        <div className="flex items-center">
          <span className="text-[15px] font-semibold text-txt">Fluxos de Caixa</span>
          {summary && (
            <span className="ml-2 text-[12px] text-txt-muted">
              {summary.total_flows} evento{summary.total_flows !== 1 && "s"}
            </span>
          )}
        </div>

        {vnaData?.entries && Object.keys(vnaData.entries).length > 0 && (
          <div className="mt-2 flex flex-wrap items-center gap-3">
            <span className="text-[10px] font-semibold uppercase tracking-wider text-txt-muted">
              Ref. {vnaData.reference_date}
            </span>
            {Object.entries(vnaData.entries).map(([type, e]) => (
              <div
                key={type}
                className="flex items-center gap-1.5 rounded-md bg-surface px-2.5 py-1 text-[11px] mono"
              >
                <span className="font-semibold text-txt">{type}</span>
                <span className="text-txt-secondary">
                  {e.vna != null
                    ? e.vna.toLocaleString("pt-BR", { minimumFractionDigits: 2, maximumFractionDigits: 6 })
                    : "—"}
                </span>
                {e.index_name && e.index_value != null && (
                  <>
                    <span className="text-border">|</span>
                    <span className="text-txt-muted">{e.index_name}</span>
                    <span className={e.index_projected ? "text-accent" : "text-txt-secondary"}>
                      {e.index_value.toLocaleString("pt-BR", { minimumFractionDigits: 2 })}%
                    </span>
                    {e.index_projected && (
                      <span className="text-[9px] text-accent font-medium">proj.</span>
                    )}
                  </>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="flex-1 overflow-y-auto p-5 space-y-5">
        {isLoading && (
          <div className="flex items-center justify-center py-20">
            <Loader2 size={20} className="animate-spin text-txt-muted" />
          </div>
        )}

        {error && (
          <div className="card border-danger/20 px-5 py-4 text-[13px] text-danger">
            {(error as Error).message}
          </div>
        )}

        {summary && (
          <>
            {/* Summary cards */}
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
              <SummaryCard
                icon={<CalendarDays size={16} />}
                label="Proximo Recebimento"
                value={summary.next_flow_date_label ?? "—"}
                sub={summary.next_flow_amount != null ? `R$ ${formatBRL(summary.next_flow_amount, 2)}` : undefined}
              />
              <SummaryCard
                icon={<DollarSign size={16} />}
                label="Total de Fluxos Futuros"
                value={`R$ ${formatBRL(summary.total_amount, 2)}`}
                highlight
              />
              <SummaryCard
                icon={<Hash size={16} />}
                label="Eventos"
                value={String(summary.total_flows)}
                sub={`${bondTypes.length} tipo${bondTypes.length !== 1 ? "s" : ""} de titulo`}
              />
            </div>

            {/* Timeline chart */}
            {chartData.length > 0 && (
              <div className="card p-5">
                <div className="text-[11px] font-semibold uppercase tracking-wider text-txt-muted mb-4">
                  Timeline de Recebimentos
                </div>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={chartData} barCategoryGap="15%">
                    <XAxis
                      dataKey="month"
                      tick={{ fill: "var(--t-txt-muted)", fontSize: 11 }}
                      axisLine={false}
                      tickLine={false}
                      interval={chartData.length > 20 ? Math.floor(chartData.length / 12) : 0}
                      angle={chartData.length > 12 ? -45 : 0}
                      textAnchor={chartData.length > 12 ? "end" : "middle"}
                      height={chartData.length > 12 ? 60 : 30}
                    />
                    <YAxis
                      tick={{ fill: "var(--t-txt-muted)", fontSize: 11, fontFamily: "JetBrains Mono" }}
                      axisLine={false}
                      tickLine={false}
                      width={70}
                      tickFormatter={(v: number) => {
                        if (v >= 1_000_000) return `${(v / 1_000_000).toFixed(1)}M`;
                        if (v >= 1000) return `${(v / 1000).toFixed(0)}k`;
                        return String(v);
                      }}
                    />
                    <Tooltip
                      contentStyle={{
                        background: "var(--t-card)",
                        border: "1px solid var(--t-border)",
                        borderRadius: 8,
                        fontSize: 12,
                        fontFamily: "JetBrains Mono",
                      }}
                      formatter={(v: number, name: string) => [
                        `R$ ${formatBRL(v, 2)}`,
                        name,
                      ]}
                      cursor={{ fill: "rgba(12, 123, 179, 0.05)" }}
                    />
                    <Legend
                      wrapperStyle={{ fontSize: 12 }}
                      iconType="square"
                      iconSize={10}
                    />
                    {bondTypes.map((type) => (
                      <Bar
                        key={type}
                        dataKey={type}
                        stackId="flows"
                        fill={colorForType(type)}
                        radius={[0, 0, 0, 0]}
                      />
                    ))}
                  </BarChart>
                </ResponsiveContainer>
              </div>
            )}

            {/* Detail table */}
            {data.flows.length > 0 && (
              <div className="card overflow-x-auto">
                <table className="w-full text-left text-[13px]">
                  <thead>
                    <tr className="border-b border-border">
                      <TH>Data</TH>
                      <TH>Tipo</TH>
                      <TH>Vencimento</TH>
                      <TH>Evento</TH>
                      <TH className="text-right">Valor (R$)</TH>
                    </tr>
                  </thead>
                  <tbody>
                    {data.flows.map((f, i) => (
                      <tr
                        key={`${f.bond_id}-${f.date}-${i}`}
                        className="border-b border-border/50 text-txt-secondary hover:bg-card-hover/50 transition-colors"
                      >
                        <td className="px-4 py-2.5">{f.date_label}</td>
                        <td className="px-4 py-2.5">
                          <span className="inline-flex items-center gap-1.5">
                            <span
                              className="inline-block h-2 w-2 rounded-sm"
                              style={{ background: colorForType(f.bond_type) }}
                            />
                            <span className="font-medium text-txt">{f.bond_type}</span>
                          </span>
                        </td>
                        <td className="px-4 py-2.5">{f.maturity_label}</td>
                        <td className="px-4 py-2.5">
                          <span
                            className={`inline-block rounded px-2 py-0.5 text-[11px] font-medium ${
                              f.event.includes("principal")
                                ? "bg-accent/10 text-accent"
                                : "bg-surface text-txt-muted"
                            }`}
                          >
                            {f.event}
                          </span>
                        </td>
                        <td className="px-4 py-2.5 text-right mono font-medium text-txt">
                          {formatBRL(f.amount, 2)}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}

function SummaryCard({
  icon, label, value, sub, highlight,
}: {
  icon: React.ReactNode;
  label: string;
  value: string;
  sub?: string;
  highlight?: boolean;
}) {
  return (
    <div className="card p-5">
      <div className="flex items-center gap-2 text-txt-muted mb-2">
        {icon}
        <span className="text-[11px] font-semibold uppercase tracking-wider">{label}</span>
      </div>
      <div className={`mono text-2xl font-bold ${highlight ? "text-accent" : "text-txt"}`}>
        {value}
      </div>
      {sub && <div className="mt-1 text-[12px] text-txt-muted">{sub}</div>}
    </div>
  );
}

function TH({ children, className = "" }: { children: React.ReactNode; className?: string }) {
  return (
    <th className={`px-4 py-3 text-[11px] font-semibold uppercase tracking-wider text-txt-muted whitespace-nowrap ${className}`}>
      {children}
    </th>
  );
}
