import { useMemo } from "react";
import { useQuery } from "@tanstack/react-query";
import { Trash2, CalendarDays } from "lucide-react";
import { usePortfolioStore } from "@/stores/portfolio";
import { fetchVna, fetchAnbimaBonds, type VnaResponse, type AnbimaResponse } from "@/api/client";
import { formatBRL } from "@/lib/utils";
import BondForm from "@/components/portfolio/BondForm";
import PortfolioTable from "@/components/portfolio/PortfolioTable";
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from "recharts";
import { colorForType } from "@/lib/constants";

function fmtRefDate(d: string | undefined | null): string {
  if (!d) return "—";
  const parts = d.split("-");
  if (parts.length === 3) return `${parts[2]}/${parts[1]}/${parts[0]}`;
  return d;
}

export default function PortfolioPage() {
  const bonds = usePortfolioStore((s) => s.bonds);
  const clearPortfolio = usePortfolioStore((s) => s.clearPortfolio);

  const { data: vnaData } = useQuery<VnaResponse>({
    queryKey: ["vna"],
    queryFn: fetchVna,
    staleTime: 1000 * 60 * 30,
  });

  const { data: anbimaData } = useQuery<AnbimaResponse>({
    queryKey: ["anbima-ref"],
    queryFn: () => fetchAnbimaBonds(),
    staleTime: 1000 * 60 * 30,
  });

  const anbimaRefDate = anbimaData?.reference_date;
  const vnaRefDate = vnaData?.reference_date;

  const summary = useMemo(() => {
    let totalValue = 0;
    const byType: Record<string, { count: number; value: number }> = {};

    for (const b of bonds) {
      const mv = b.market_value ?? b.notional;
      totalValue += mv;
      const entry = byType[b.type] || { count: 0, value: 0 };
      entry.count += b.quantity;
      entry.value += mv;
      byType[b.type] = entry;
    }

    const pieData = Object.entries(byType).map(([type, { value }]) => ({
      name: type,
      value,
      pct: totalValue > 0 ? (value / totalValue) * 100 : 0,
      color: colorForType(type),
    }));

    return { totalValue, byType, pieData, bondCount: bonds.length };
  }, [bonds]);

  return (
    <div className="flex h-full flex-col">
      <div className="flex h-12 shrink-0 items-center justify-between border-b border-border bg-base px-5">
        <div>
          <span className="text-[15px] font-semibold text-txt">Carteira</span>
          <span className="ml-2 text-[12px] text-txt-muted">
            {summary.bondCount} titulo{summary.bondCount !== 1 && "s"}
          </span>
        </div>
        {bonds.length > 0 && (
          <button
            onClick={() => clearPortfolio()}
            className="flex h-7 items-center gap-1.5 rounded-md border border-border px-2.5 text-[12px] font-medium text-txt-muted transition-colors hover:bg-surface hover:text-txt-secondary"
          >
            <Trash2 size={12} /> Limpar
          </button>
        )}
      </div>

      {/* Reference date banner */}
      {(anbimaRefDate || vnaRefDate) && (
        <div className="shrink-0 border-b border-border bg-surface/50 px-5 py-2 flex flex-wrap items-center gap-4">
          <div className="flex items-center gap-1.5 text-[12px]">
            <CalendarDays size={13} className="text-accent" />
            <span className="font-semibold text-txt">
              Posição em {fmtRefDate(anbimaRefDate || vnaRefDate)}
            </span>
          </div>
          {anbimaRefDate && (
            <span className="text-[11px] text-txt-muted mono">
              ANBIMA: {fmtRefDate(anbimaRefDate)}
            </span>
          )}
          {vnaRefDate && (
            <span className="text-[11px] text-txt-muted mono">
              VNA: {fmtRefDate(vnaRefDate)}
            </span>
          )}
          {vnaData?.entries && Object.keys(vnaData.entries).length > 0 && (
            <>
              <span className="text-border">|</span>
              {Object.entries(vnaData.entries).map(([type, e]) => (
                <div
                  key={type}
                  className="flex items-center gap-1.5 text-[11px] mono"
                >
                  <span className="font-semibold text-txt">{type}</span>
                  <span className="text-txt-secondary">
                    {e.vna != null
                      ? e.vna.toLocaleString("pt-BR", { minimumFractionDigits: 2, maximumFractionDigits: 6 })
                      : "—"}
                  </span>
                  {e.index_name && e.index_value != null && (
                    <>
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
            </>
          )}
        </div>
      )}

      <div className="flex-1 overflow-y-auto p-5 space-y-5">
        <BondForm />

        {bonds.length > 0 && (
          <>
            {/* Summary cards + chart */}
            <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
              {/* Patrimonio */}
              <div className="card p-5 flex flex-col justify-center">
                <div className="text-[11px] font-semibold uppercase tracking-wider text-txt-muted mb-1">
                  Patrimonio Total
                </div>
                <div className="mono text-3xl font-bold text-txt">
                  R$ {formatBRL(summary.totalValue, 2)}
                </div>
                <div className="mt-1 text-[12px] text-txt-muted">
                  {summary.bondCount} titulo{summary.bondCount !== 1 && "s"} na carteira
                </div>
              </div>

              {/* Type breakdown */}
              <div className="card p-5">
                <div className="text-[11px] font-semibold uppercase tracking-wider text-txt-muted mb-3">
                  Distribuicao por Tipo
                </div>
                <div className="space-y-2.5">
                  {summary.pieData.map(({ name, value, pct, color }) => (
                    <div key={name}>
                      <div className="flex items-baseline justify-between mb-1">
                        <div className="flex items-center gap-2">
                          <div className="h-2.5 w-2.5 rounded-sm" style={{ background: color }} />
                          <span className="text-[13px] font-medium text-txt">{name}</span>
                        </div>
                        <span className="mono text-[12px] text-txt-secondary">
                          {formatBRL(pct, 1)}%
                        </span>
                      </div>
                      <div className="h-1.5 overflow-hidden rounded-full bg-surface">
                        <div
                          className="h-full rounded-full transition-all duration-500"
                          style={{ width: `${pct}%`, background: color }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Donut chart */}
              <div className="card p-5 flex flex-col items-center justify-center">
                <div className="text-[11px] font-semibold uppercase tracking-wider text-txt-muted mb-2 self-start">
                  Composicao
                </div>
                {summary.pieData.length > 0 ? (
                  <ResponsiveContainer width="100%" height={180}>
                    <PieChart>
                      <Pie
                        data={summary.pieData}
                        cx="50%"
                        cy="50%"
                        innerRadius={50}
                        outerRadius={75}
                        dataKey="value"
                        stroke="none"
                        paddingAngle={2}
                      >
                        {summary.pieData.map((entry, i) => (
                          <Cell key={i} fill={entry.color} />
                        ))}
                      </Pie>
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
                      />
                    </PieChart>
                  </ResponsiveContainer>
                ) : (
                  <div className="py-10 text-[13px] text-txt-muted">Sem dados</div>
                )}
              </div>
            </div>

            {/* Table */}
            <PortfolioTable />
          </>
        )}
      </div>
    </div>
  );
}
