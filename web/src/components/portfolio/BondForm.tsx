import { useState, useEffect, useMemo } from "react";
import { useQuery, useMutation } from "@tanstack/react-query";
import { Plus, Loader2 } from "lucide-react";
import { fetchAnbimaBonds, enrichBond, type AnbimaBond } from "@/api/client";
import { usePortfolioStore } from "@/stores/portfolio";

const BOND_TYPES = ["LTN", "NTN-F", "NTN-B", "LFT"] as const;
type InputMode = "taxa" | "pu";

function todayISO() {
  return new Date().toISOString().split("T")[0];
}

function nextBusinessDay(dateStr: string): string {
  const d = new Date(dateStr + "T12:00:00");
  d.setDate(d.getDate() + 1);
  while (d.getDay() === 0 || d.getDay() === 6) {
    d.setDate(d.getDate() + 1);
  }
  return d.toISOString().split("T")[0];
}

export default function BondForm() {
  const addBond = usePortfolioStore((s) => s.addBond);

  const [type, setType] = useState<string>("LTN");
  const [maturityKey, setMaturityKey] = useState("");
  const [inputMode, setInputMode] = useState<InputMode>("taxa");
  const [rate, setRate] = useState<number>(0);
  const [puInput, setPuInput] = useState<number>(0);
  const [purchaseDate, setPurchaseDate] = useState(todayISO());
  const [settlementDate, setSettlementDate] = useState(nextBusinessDay(todayISO()));
  const [quantity, setQuantity] = useState<number>(100);

  useEffect(() => {
    setSettlementDate(nextBusinessDay(purchaseDate));
  }, [purchaseDate]);

  const { data: anbimaData, isLoading: anbimaLoading } = useQuery({
    queryKey: ["anbima", type],
    queryFn: () => fetchAnbimaBonds(type),
    staleTime: 1000 * 60 * 30,
  });

  const maturities: AnbimaBond[] = useMemo(() => {
    if (!anbimaData?.bonds) return [];
    return [...anbimaData.bonds].sort((a, b) => a.maturity.localeCompare(b.maturity));
  }, [anbimaData]);

  const selectedBond = useMemo(
    () => maturities.find((m) => m.maturity === maturityKey),
    [maturities, maturityKey]
  );

  useEffect(() => {
    setMaturityKey("");
    setRate(0);
    setPuInput(0);
  }, [type]);

  useEffect(() => {
    if (selectedBond) {
      if (selectedBond.indicative_rate != null) setRate(selectedBond.indicative_rate);
      if (selectedBond.pu != null) setPuInput(selectedBond.pu);
    }
  }, [selectedBond]);

  const enrichMutation = useMutation({
    mutationFn: enrichBond,
    onSuccess: (result) => {
      addBond({
        type,
        notional: result.notional,
        quantity,
        rate: result.rate,
        settlement_date: settlementDate,
        maturity_date: maturityKey,
        maturity_label: selectedBond?.maturity_label ?? maturityKey,
        current_rate: result.rate,
        purchase_date: purchaseDate,
        purchase_rate: result.purchase_rate,
        purchase_pu: result.purchase_pu,
        pu: result.pu,
        dv01: result.dv01,
        duration_modified: result.duration_modified,
        duration_anbima_du: result.duration_anbima_du,
        market_value: result.market_value,
        vna_used: result.vna_used,
        reference_date: result.reference_date,
      });

      setMaturityKey("");
      setRate(0);
      setPuInput(0);
      setQuantity(100);
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!maturityKey || !settlementDate) return;

    enrichMutation.mutate({
      type,
      purchase_date: purchaseDate,
      settlement_date: settlementDate,
      maturity_date: maturityKey,
      quantity,
      input_mode: inputMode,
      rate: inputMode === "taxa" ? rate : undefined,
      pu: inputMode === "pu" ? puInput : undefined,
    });
  };

  const isLFT = type === "LFT";
  const isNTNB = type === "NTN-B";
  const submitting = enrichMutation.isPending;

  return (
    <form onSubmit={handleSubmit} className="card p-5">
      <div className="flex flex-wrap items-end gap-3">
        <div className="w-[110px]">
          <label className="label-field">Tipo</label>
          <select value={type} onChange={(e) => setType(e.target.value)} className="input-field">
            {BOND_TYPES.map((t) => <option key={t} value={t}>{t}</option>)}
          </select>
        </div>

        <div className="w-[160px]">
          <label className="label-field">Vencimento</label>
          {anbimaLoading ? (
            <div className="input-field flex items-center justify-center">
              <Loader2 size={14} className="animate-spin text-txt-muted" />
            </div>
          ) : (
            <select
              value={maturityKey}
              onChange={(e) => setMaturityKey(e.target.value)}
              className="input-field"
              required
            >
              <option value="">Selecione</option>
              {maturities.map((m) => (
                <option key={m.maturity} value={m.maturity}>{m.maturity_label}</option>
              ))}
            </select>
          )}
        </div>

        {/* Taxa / PU toggle */}
        <div className="w-[180px]">
          <div className="flex items-center gap-1 mb-1">
            <button
              type="button"
              onClick={() => setInputMode("taxa")}
              className={`rounded px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wider transition-colors ${
                inputMode === "taxa"
                  ? "bg-accent text-white"
                  : "bg-surface text-txt-muted hover:text-txt-secondary"
              }`}
            >
              Taxa
            </button>
            <button
              type="button"
              onClick={() => setInputMode("pu")}
              className={`rounded px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wider transition-colors ${
                inputMode === "pu"
                  ? "bg-accent text-white"
                  : "bg-surface text-txt-muted hover:text-txt-secondary"
              }`}
            >
              PU
            </button>
          </div>

          {inputMode === "taxa" ? (
            <input
              type="number"
              step="0.0001"
              value={rate}
              onChange={(e) => setRate(Number(e.target.value))}
              className="input-field mono"
              placeholder={isLFT ? "Ágio/Deságio %" : isNTNB ? "Taxa real %" : "Taxa %"}
            />
          ) : (
            <input
              type="number"
              step="0.000001"
              value={puInput}
              onChange={(e) => setPuInput(Number(e.target.value))}
              className="input-field mono"
              placeholder="PU"
            />
          )}
        </div>

        <div className="w-[140px]">
          <label className="label-field">Data Compra</label>
          <input
            type="date"
            value={purchaseDate}
            onChange={(e) => setPurchaseDate(e.target.value)}
            required
            className="input-field"
          />
        </div>

        <div className="w-[140px]">
          <label className="label-field">Data Liquidação</label>
          <input
            type="date"
            value={settlementDate}
            onChange={(e) => setSettlementDate(e.target.value)}
            required
            className="input-field"
          />
        </div>

        <div className="w-[90px]">
          <label className="label-field">Quantidade</label>
          <input
            type="number"
            min={1}
            value={quantity}
            onChange={(e) => setQuantity(Number(e.target.value))}
            className="input-field mono"
          />
        </div>

        <button
          type="submit"
          disabled={!maturityKey || !settlementDate || submitting}
          className="btn-primary gap-2"
        >
          {submitting ? (
            <Loader2 size={16} className="animate-spin" />
          ) : (
            <Plus size={16} />
          )}
          Adicionar
        </button>
      </div>

      {enrichMutation.isError && (
        <div className="mt-2 text-[12px] text-danger">
          {(enrichMutation.error as Error).message}
        </div>
      )}

      {selectedBond && (
        <div className="mt-3 flex flex-wrap gap-4 text-[11px] text-txt-muted mono">
          {anbimaData?.reference_date && <span>Ref: {anbimaData.reference_date}</span>}
          {selectedBond.pu != null && (
            <span>PU ANBIMA: {selectedBond.pu.toLocaleString("pt-BR", { minimumFractionDigits: 6 })}</span>
          )}
          {selectedBond.indicative_rate != null && (
            <span>Taxa Ind.: {selectedBond.indicative_rate.toLocaleString("pt-BR", { minimumFractionDigits: 4 })}%</span>
          )}
          {selectedBond.buy_rate != null && (
            <span>Compra: {selectedBond.buy_rate.toLocaleString("pt-BR", { minimumFractionDigits: 4 })}%</span>
          )}
          {selectedBond.sell_rate != null && (
            <span>Venda: {selectedBond.sell_rate.toLocaleString("pt-BR", { minimumFractionDigits: 4 })}%</span>
          )}
        </div>
      )}
    </form>
  );
}
