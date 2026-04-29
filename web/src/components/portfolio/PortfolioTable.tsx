import { useState, useMemo } from "react";
import { ChevronRight, ChevronDown, Trash2 } from "lucide-react";
import { usePortfolioStore, type Bond } from "@/stores/portfolio";
import { formatBRL, formatPct } from "@/lib/utils";

const TH =
  "px-3 py-3 text-[11px] font-semibold uppercase tracking-wider text-txt-muted whitespace-nowrap";

interface BondPosition {
  key: string;
  type: string;
  maturity_date: string;
  maturity_label: string;
  lots: Bond[];
  total_quantity: number;
  avg_purchase_pu: number;
  avg_purchase_rate: number;
  pu_mtm: number;
  rate_mtm: number;
  dv01: number;
  duration_anbima_du: number;
  market_value: number;
  vna_used: number | null;
  reference_date: string | null;
}

function fmtNum(v: number | undefined | null, decimals: number): string {
  if (v == null) return "—";
  return v.toLocaleString("pt-BR", {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
}

function fmtDate(d: string | undefined | null): string {
  if (!d) return "—";
  const parts = d.split("-");
  if (parts.length === 3) return `${parts[2]}/${parts[1]}/${parts[0]}`;
  return d;
}

function buildPositions(bonds: Bond[]): BondPosition[] {
  const map = new Map<string, Bond[]>();

  for (const b of bonds) {
    const key = `${b.type}:${b.maturity_date}`;
    const list = map.get(key) || [];
    list.push(b);
    map.set(key, list);
  }

  const positions: BondPosition[] = [];

  for (const [key, lots] of map) {
    const totalQty = lots.reduce((s, l) => s + l.quantity, 0);

    let sumPuQty = 0;
    let sumRatePuQty = 0;
    let sumPuQtyDenom = 0;

    for (const l of lots) {
      const pu = l.purchase_pu ?? l.pu ?? 0;
      const w = pu * l.quantity;
      sumPuQty += w;
      sumRatePuQty += (l.purchase_rate ?? l.rate) * w;
      sumPuQtyDenom += w;
    }

    const avgPu = totalQty > 0 ? sumPuQty / totalQty : 0;
    const avgRate = sumPuQtyDenom > 0 ? sumRatePuQty / sumPuQtyDenom : 0;

    const ref = lots[0];
    const puMtm = ref.pu ?? 0;
    const rateMtm = ref.rate ?? 0;
    const dv01PerUnit = ref.dv01 != null && ref.quantity > 0 ? ref.dv01 / ref.quantity : 0;
    const mvPerUnit = ref.market_value != null && ref.quantity > 0 ? ref.market_value / ref.quantity : 0;

    positions.push({
      key,
      type: ref.type,
      maturity_date: ref.maturity_date,
      maturity_label: ref.maturity_label || ref.maturity_date,
      lots,
      total_quantity: totalQty,
      avg_purchase_pu: avgPu,
      avg_purchase_rate: avgRate,
      pu_mtm: puMtm,
      rate_mtm: rateMtm,
      dv01: dv01PerUnit * totalQty,
      duration_anbima_du: ref.duration_anbima_du ?? 0,
      market_value: mvPerUnit * totalQty,
      vna_used: ref.vna_used ?? null,
      reference_date: ref.reference_date ?? null,
    });
  }

  return positions.sort((a, b) => {
    const tc = a.type.localeCompare(b.type);
    if (tc !== 0) return tc;
    return a.maturity_date.localeCompare(b.maturity_date);
  });
}

export default function PortfolioTable() {
  const bonds = usePortfolioStore((s) => s.bonds);
  const removeBond = usePortfolioStore((s) => s.removeBond);
  const [expanded, setExpanded] = useState<Set<string>>(new Set());

  const positions = useMemo(() => buildPositions(bonds), [bonds]);

  if (positions.length === 0) return null;

  const toggle = (key: string) => {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });
  };

  return (
    <div className="card overflow-x-auto">
      <table className="w-full text-left text-[13px]">
        <thead>
          <tr className="border-b border-border">
            <th className="px-2 py-3 w-8" />
            <th className={`${TH} pl-1`}>Título</th>
            <th className={TH}>Vencimento</th>
            <th className={`${TH} text-right`}>PU Médio</th>
            <th className={`${TH} text-right`}>Taxa Média</th>
            <th className={`${TH} text-right`}>PU MtM</th>
            <th className={`${TH} text-right`}>Taxa MtM</th>
            <th className={`${TH} text-right`}>DV01</th>
            <th className={`${TH} text-right`}>Duration</th>
            <th className={`${TH} text-right`}>Qtd</th>
            <th className={`${TH} text-right`}>Valor MtM</th>
            <th className={`${TH} text-right`}>VNA</th>
            <th className="px-3 py-3 w-10" />
          </tr>
        </thead>
        <tbody>
          {positions.map((pos) => {
            const isOpen = expanded.has(pos.key);
            const hasMultiple = pos.lots.length > 1;

            return (
              <PositionRows
                key={pos.key}
                position={pos}
                isOpen={isOpen}
                hasMultiple={hasMultiple}
                onToggle={() => toggle(pos.key)}
                onRemoveLot={removeBond}
              />
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

function PositionRows({
  position: pos,
  isOpen,
  hasMultiple,
  onToggle,
  onRemoveLot,
}: {
  position: BondPosition;
  isOpen: boolean;
  hasMultiple: boolean;
  onToggle: () => void;
  onRemoveLot: (id: string) => void;
}) {
  return (
    <>
      {/* Aggregate row */}
      <tr className="border-b border-border/50 text-txt-secondary hover:bg-card-hover/50 transition-colors">
        <td className="px-2 py-2.5 text-center">
          {hasMultiple ? (
            <button
              onClick={onToggle}
              className="rounded p-0.5 text-txt-muted hover:text-txt transition-colors"
            >
              {isOpen ? <ChevronDown size={14} /> : <ChevronRight size={14} />}
            </button>
          ) : null}
        </td>
        <td className="pl-1 px-3 py-2.5 font-medium text-txt">{pos.type}</td>
        <td className="px-3 py-2.5">{pos.maturity_label}</td>
        <td className="px-3 py-2.5 text-right mono">{fmtNum(pos.avg_purchase_pu, 6)}</td>
        <td className="px-3 py-2.5 text-right mono">{formatPct(pos.avg_purchase_rate, 4)}</td>
        <td className="px-3 py-2.5 text-right mono">{fmtNum(pos.pu_mtm, 6)}</td>
        <td className="px-3 py-2.5 text-right mono">{formatPct(pos.rate_mtm, 4)}</td>
        <td className="px-3 py-2.5 text-right mono">{fmtNum(pos.dv01, 2)}</td>
        <td className="px-3 py-2.5 text-right mono">
          {pos.duration_anbima_du > 0 ? fmtNum(pos.duration_anbima_du, 0) + " du" : "—"}
        </td>
        <td className="px-3 py-2.5 text-right mono">{formatBRL(pos.total_quantity, 0)}</td>
        <td className="px-3 py-2.5 text-right mono font-medium text-txt">
          R$ {fmtNum(pos.market_value, 2)}
        </td>
        <td className="px-3 py-2.5 text-right mono text-[12px]">
          {pos.vna_used != null ? fmtNum(pos.vna_used, 2) : "—"}
        </td>
        <td className="px-3 py-2.5">
          {!hasMultiple && (
            <button
              onClick={() => onRemoveLot(pos.lots[0].id)}
              className="rounded p-1 text-txt-muted hover:text-danger transition-colors"
            >
              <Trash2 size={14} />
            </button>
          )}
        </td>
      </tr>

      {/* Expanded lot rows */}
      {isOpen &&
        hasMultiple &&
        pos.lots.map((lot) => (
          <tr
            key={lot.id}
            className="border-b border-border/30 bg-surface/30 text-txt-muted text-[12px]"
          >
            <td />
            <td className="pl-1 px-3 py-2 text-txt-muted italic" colSpan={2}>
              {fmtDate(lot.purchase_date)} → {fmtDate(lot.settlement_date)}
            </td>
            <td className="px-3 py-2 text-right mono">
              {fmtNum(lot.purchase_pu ?? lot.pu, 6)}
            </td>
            <td className="px-3 py-2 text-right mono">
              {formatPct(lot.purchase_rate ?? lot.rate, 4)}
            </td>
            <td className="px-3 py-2 text-right mono text-txt-muted/50" colSpan={2} />
            <td className="px-3 py-2 text-right mono" colSpan={2} />
            <td className="px-3 py-2 text-right mono">{formatBRL(lot.quantity, 0)}</td>
            <td className="px-3 py-2 text-right mono">
              R$ {fmtNum((lot.purchase_pu ?? lot.pu ?? 0) * lot.quantity, 2)}
            </td>
            <td />
            <td className="px-3 py-2">
              <button
                onClick={() => onRemoveLot(lot.id)}
                className="rounded p-1 text-txt-muted hover:text-danger transition-colors"
              >
                <Trash2 size={13} />
              </button>
            </td>
          </tr>
        ))}
    </>
  );
}
