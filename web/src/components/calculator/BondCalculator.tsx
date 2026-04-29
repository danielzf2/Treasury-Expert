import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { Loader2, ChevronDown, ChevronUp } from "lucide-react";
import { portfolioRisk, calculate, type BondRiskResult } from "@/api/client";
import { formatBRL, formatPct } from "@/lib/utils";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

type BondType = "LTN" | "NTN-F" | "NTN-B" | "LFT";

interface FormState {
  type: BondType;
  taxa_aa: number;
  data_liquidacao: string;
  data_vencimento: string;
  vna: number;
  agio_desagio_bps: number;
  cupom_aa: number;
}

const DEFAULTS: FormState = {
  type: "LTN", taxa_aa: 12.75, data_liquidacao: "", data_vencimento: "",
  vna: 1000, agio_desagio_bps: 0, cupom_aa: 6.0,
};

const TOOL_MAP: Record<BondType, string> = {
  LTN: "precificar_ltn", "NTN-F": "precificar_ntnf",
  "NTN-B": "precificar_ntnb", LFT: "precificar_lft",
};

function buildToolParams(form: FormState): Record<string, unknown> {
  switch (form.type) {
    case "LTN": return { taxa_aa: form.taxa_aa, data_liquidacao: form.data_liquidacao, data_vencimento: form.data_vencimento };
    case "NTN-F": return { taxa_aa: form.taxa_aa, data_liquidacao: form.data_liquidacao, data_vencimento: form.data_vencimento };
    case "NTN-B": return { taxa_real_aa: form.taxa_aa, vna: form.vna, data_liquidacao: form.data_liquidacao, data_vencimento: form.data_vencimento, cupom_aa: form.cupom_aa };
    case "LFT": return { agio_desagio_bps: form.agio_desagio_bps, data_liquidacao: form.data_liquidacao, data_vencimento: form.data_vencimento, vna_selic: form.vna };
  }
}

const TYPES: BondType[] = ["LTN", "NTN-F", "NTN-B", "LFT"];

export default function BondCalculator() {
  const [form, setForm] = useState<FormState>(DEFAULTS);
  const [showDetail, setShowDetail] = useState(false);

  const riskMut = useMutation({
    mutationFn: () => portfolioRisk([{
      id: "calc", type: form.type, notional: 1_000_000, quantity: 1,
      rate: form.type === "LFT" ? form.agio_desagio_bps : form.taxa_aa,
      settlement_date: form.data_liquidacao, maturity_date: form.data_vencimento,
      vna: (form.type === "NTN-B" || form.type === "LFT") ? form.vna : undefined,
      current_rate: form.type === "LFT" ? form.agio_desagio_bps : form.taxa_aa,
    }]),
  });

  const detailMut = useMutation({
    mutationFn: () => calculate({ tool: TOOL_MAP[form.type], params: buildToolParams(form) }),
  });

  const set = <K extends keyof FormState>(k: K, v: FormState[K]) => setForm((p) => ({ ...p, [k]: v }));

  const submit = (e: React.FormEvent) => { e.preventDefault(); riskMut.mutate(); setShowDetail(false); };
  const toggleDetail = () => { if (!detailMut.data) detailMut.mutate(); setShowDetail((v) => !v); };

  const bond = riskMut.data?.bonds?.[0];

  return (
    <div className="space-y-6">
      {/* Form */}
      <div className="card p-6">
        <div className="mb-5 flex gap-2">
          {TYPES.map((t) => (
            <button key={t} type="button" onClick={() => set("type", t)}
              className={`rounded-lg px-5 py-2 text-[13px] font-semibold transition-colors ${
                form.type === t ? "bg-accent text-white" : "bg-card-hover text-txt-muted hover:text-txt-secondary"
              }`}>{t}</button>
          ))}
        </div>

        <form onSubmit={submit} className="flex flex-wrap items-end gap-4">
          <div className="min-w-[140px] flex-1">
            <label className="label-field">
              {form.type === "NTN-B" ? "Taxa Real (% a.a.)" : form.type === "LFT" ? "Agio/Desagio (bps)" : "Taxa (% a.a.)"}
            </label>
            <input type="number" step="0.01"
              value={form.type === "LFT" ? form.agio_desagio_bps : form.taxa_aa}
              onChange={(e) => form.type === "LFT" ? set("agio_desagio_bps", Number(e.target.value)) : set("taxa_aa", Number(e.target.value))}
              className="input-field mono" />
          </div>
          <div className="min-w-[150px] flex-1">
            <label className="label-field">Data Liquidacao</label>
            <input type="date" value={form.data_liquidacao} onChange={(e) => set("data_liquidacao", e.target.value)} required className="input-field" />
          </div>
          <div className="min-w-[150px] flex-1">
            <label className="label-field">Data Vencimento</label>
            <input type="date" value={form.data_vencimento} onChange={(e) => set("data_vencimento", e.target.value)} required className="input-field" />
          </div>

          {(form.type === "NTN-B" || form.type === "LFT") && (
            <div className="min-w-[140px] flex-1">
              <label className="label-field">{form.type === "NTN-B" ? "VNA (IPCA)" : "VNA Selic"}</label>
              <input type="number" step="0.000001" value={form.vna} onChange={(e) => set("vna", Number(e.target.value))} className="input-field mono" />
            </div>
          )}
          {form.type === "NTN-B" && (
            <div className="min-w-[120px] flex-1">
              <label className="label-field">Cupom (% a.a.)</label>
              <input type="number" step="0.01" value={form.cupom_aa} onChange={(e) => set("cupom_aa", Number(e.target.value))} className="input-field mono" />
            </div>
          )}

          <button type="submit" disabled={riskMut.isPending || !form.data_liquidacao || !form.data_vencimento} className="btn-primary">
            {riskMut.isPending ? <Loader2 size={16} className="animate-spin" /> : "Calcular"}
          </button>
        </form>
      </div>

      {/* Results */}
      {bond && <Results bond={bond} showDetail={showDetail} onToggle={toggleDetail} />}

      {riskMut.error && (
        <div className="card border-danger/30 p-4 text-[13px] text-danger">{(riskMut.error as Error).message}</div>
      )}

      {showDetail && (
        <div className="card overflow-hidden">
          <div className="border-b border-border px-6 py-3">
            <span className="label-field mb-0">Calculo Detalhado ANBIMA</span>
          </div>
          <div className="p-6">
            {detailMut.isPending && <Loader2 size={16} className="animate-spin text-txt-muted" />}
            {detailMut.data && (
              <div className="prose prose-invert prose-sm max-w-none prose-h2:text-sm prose-h2:mt-3 prose-h2:mb-1 prose-p:text-[13px] prose-p:text-txt-secondary prose-strong:text-txt prose-code:text-accent prose-code:text-[12px] prose-code:font-mono prose-code:before:content-none prose-code:after:content-none prose-code:bg-card-hover prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded prose-pre:bg-card prose-pre:border prose-pre:border-border prose-pre:rounded-lg prose-pre:font-mono prose-pre:text-[12px] prose-td:text-[12px] prose-td:text-txt-secondary prose-td:font-mono prose-th:text-[10px] prose-th:font-semibold prose-th:uppercase prose-th:tracking-wider prose-th:text-txt-muted">
                <ReactMarkdown remarkPlugins={[remarkGfm]}>{detailMut.data.result}</ReactMarkdown>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

function Results({ bond, showDetail, onToggle }: { bond: BondRiskResult; showDetail: boolean; onToggle: () => void }) {
  return (
    <div className="space-y-4">
      {/* PU Hero */}
      <div className="card p-6 text-center">
        <div className="label-field mb-1">Preco Unitario (PU)</div>
        <div className="mono text-4xl font-bold text-txt">{formatBRL(bond.pu, 6)}</div>
        <div className="mt-2 text-[13px] text-txt-muted">
          {bond.type} &middot; {bond.du} DU &middot; Taxa {formatPct(bond.current_rate, 2)}
        </div>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-2 gap-3 lg:grid-cols-6">
        <Metric label="Duration Macaulay" value={`${formatBRL(bond.duration_macaulay, 4)} a`} />
        <Metric label="Duration Mod" value={formatBRL(bond.duration_modified, 4)} />
        <Metric label="Duration ANBIMA" value={`${formatBRL(bond.duration_anbima_du, 0)} DU`} />
        <Metric label="Convexidade" value={formatBRL(bond.convexity, 4)} />
        <Metric label="DV01" value={`R$ ${formatBRL(bond.dv01, 2)}`} highlight />
        <Metric label="Carry / DU" value={`R$ ${formatBRL(bond.carry_1du, 2)}`} />
      </div>

      <button onClick={onToggle}
        className="flex w-full items-center justify-center gap-1.5 py-2 text-[13px] text-txt-muted hover:text-txt-secondary transition-colors">
        {showDetail ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
        {showDetail ? "Ocultar calculo detalhado" : "Ver calculo detalhado ANBIMA"}
      </button>
    </div>
  );
}

function Metric({ label, value, highlight }: { label: string; value: string; highlight?: boolean }) {
  return (
    <div className="card px-4 py-3">
      <div className="label-field">{label}</div>
      <div className={`mt-1 mono text-[16px] font-bold ${highlight ? "text-accent" : "text-txt"}`}>{value}</div>
    </div>
  );
}
