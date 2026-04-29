const BASE = "/api";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail || `HTTP ${res.status}`);
  }
  return res.json();
}

// ── Calculate ────────────────────────────────────────────────────────────────

export interface CalculateRequest {
  tool: string;
  params: Record<string, unknown>;
}

export interface CalculateResponse {
  tool: string;
  result: string;
}

export async function calculate(req: CalculateRequest): Promise<CalculateResponse> {
  return request("/calculate", { method: "POST", body: JSON.stringify(req) });
}

export interface ToolMetadata {
  description: string;
  parameters: {
    type: string;
    properties: Record<string, { type: string; default?: unknown }>;
    required: string[];
  };
}

export async function listTools(): Promise<{ count: number; tools: Record<string, ToolMetadata> }> {
  return request("/tools");
}

// ── ANBIMA ────────────────────────────────────────────────────────────────────

export interface AnbimaBond {
  type: string;
  maturity: string;
  maturity_label: string;
  selic_code: string;
  emission_date: string;
  indicative_rate: number | null;
  pu: number | null;
  buy_rate: number | null;
  sell_rate: number | null;
  std_dev: number | null;
  criterion: string;
}

export interface AnbimaResponse {
  reference_date: string;
  bonds: AnbimaBond[];
}

export async function fetchAnbimaBonds(type?: string): Promise<AnbimaResponse> {
  const path = type ? `/anbima/titulos/${encodeURIComponent(type)}` : "/anbima/titulos";
  return request(path);
}

export interface VnaEntry {
  selic_code: string;
  reference_date: string;
  vna: number | null;
  index_name?: string;
  index_value?: number | null;
  index_projected?: boolean;
  index_raw?: string;
  valid_from?: string;
}

export interface VnaResponse {
  reference_date: string;
  vna: Record<string, number>;
  entries: Record<string, VnaEntry>;
}

export async function fetchVna(): Promise<VnaResponse> {
  return request("/anbima/vna");
}

// ── Portfolio ────────────────────────────────────────────────────────────────

export interface EnrichBondRequest {
  type: string;
  purchase_date?: string;
  settlement_date: string;
  maturity_date: string;
  quantity: number;
  input_mode: "taxa" | "pu";
  rate?: number;
  pu?: number;
  vna?: number;
}

export interface EnrichedBond {
  purchase_rate: number;
  purchase_pu: number;
  pu: number;
  rate: number;
  dv01: number;
  duration_modified: number;
  duration_anbima_du: number;
  duration_macaulay: number;
  convexity: number;
  market_value: number;
  du: number;
  notional: number;
  vna_used: number | null;
  reference_date: string | null;
}

export async function enrichBond(req: EnrichBondRequest): Promise<EnrichedBond> {
  return request("/portfolio/enrich-bond", {
    method: "POST",
    body: JSON.stringify(req),
  });
}

export interface BondRequest {
  id: string;
  type: string;
  notional: number;
  quantity: number;
  rate: number;
  settlement_date: string;
  maturity_date: string;
  maturity_label?: string;
  vna?: number;
  premium_bps?: number;
  current_rate?: number;
  purchase_date?: string;
  purchase_rate?: number;
  purchase_pu?: number;
  pu?: number;
  dv01?: number;
  duration_modified?: number;
  duration_anbima_du?: number;
  market_value?: number;
  vna_used?: number | null;
  reference_date?: string | null;
}

export interface BondRiskResult {
  id: string;
  type: string;
  pu: number;
  market_value: number;
  du: number;
  duration_macaulay: number;
  duration_modified: number;
  duration_anbima_du: number;
  convexity: number;
  dv01: number;
  carry_1du: number;
  notional: number;
  quantity: number;
  rate: number;
  current_rate: number;
}

export interface PortfolioRiskResult {
  bonds: BondRiskResult[];
  total_dv01: number;
  total_market_value: number;
  weighted_duration_mod: number;
  weighted_duration_anbima: number;
  weighted_convexity: number;
  exposure_by_type: Record<string, number>;
  exposure_by_maturity_bucket: Record<string, number>;
}

export async function portfolioRisk(bonds: BondRequest[]): Promise<PortfolioRiskResult> {
  return request("/portfolio/risk", { method: "POST", body: JSON.stringify({ bonds }) });
}

export interface HedgeResult {
  portfolio_dv01: number;
  hedge_dv01_per_contract: number;
  contracts_needed: number;
  contracts_raw: number;
  residual_dv01: number;
  direction: string;
  hedge_maturity_du: number;
}

export async function portfolioHedge(
  bonds: BondRequest[],
  hedge_rate_aa: number,
  hedge_du: number,
  contract_face = 100_000
): Promise<HedgeResult> {
  return request("/portfolio/hedge", {
    method: "POST",
    body: JSON.stringify({ bonds, hedge_rate_aa, hedge_du, contract_face }),
  });
}

export interface ScenarioResult {
  shock_bps: number;
  bonds: Array<{
    id: string;
    type: string;
    market_value: number;
    pnl_1st_order: number;
    pnl_2nd_order: number;
    pnl_pct: number;
  }>;
  total_pnl_1st_order: number;
  total_pnl_2nd_order: number;
  total_market_value: number;
  total_pnl_pct: number;
}

export async function portfolioScenario(bonds: BondRequest[], shock_bps: number): Promise<ScenarioResult> {
  return request("/portfolio/scenario", {
    method: "POST",
    body: JSON.stringify({ bonds, shock_bps }),
  });
}

// ── Cashflows ─────────────────────────────────────────────────────────────────

export interface CashflowItem {
  date: string;
  date_label: string;
  month_key: string;
  bond_id: string;
  bond_type: string;
  maturity_label: string;
  event: string;
  amount: number;
}

export interface CashflowSummary {
  total_flows: number;
  total_amount: number;
  next_flow_date: string | null;
  next_flow_date_label: string | null;
  next_flow_amount: number | null;
}

export interface CashflowsResponse {
  flows: CashflowItem[];
  summary: CashflowSummary;
}

export async function portfolioCashflows(bonds: BondRequest[]): Promise<CashflowsResponse> {
  return request("/portfolio/cashflows", { method: "POST", body: JSON.stringify({ bonds }) });
}

// ── Chat ─────────────────────────────────────────────────────────────────────

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export interface TokenUsage {
  prompt_tokens: number;
  completion_tokens: number;
  total_tokens: number;
  estimated_cost_usd: number;
  model: string;
}

export interface ChatStreamEvent {
  type: "content" | "tool_call" | "tool_result" | "usage" | "done";
  content?: string;
  tool?: string;
  result?: string;
  prompt_tokens?: number;
  completion_tokens?: number;
  total_tokens?: number;
  estimated_cost_usd?: number;
  model?: string;
}

export async function* chatStream(messages: ChatMessage[], model?: string): AsyncGenerator<ChatStreamEvent> {
  const res = await fetch(`${BASE}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ messages, stream: true, model: model || undefined }),
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail || `HTTP ${res.status}`);
  }

  const reader = res.body!.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop() || "";

    for (const line of lines) {
      if (line.startsWith("data: ")) {
        try {
          const event: ChatStreamEvent = JSON.parse(line.slice(6));
          yield event;
        } catch {
          // skip malformed events
        }
      }
    }
  }
}
