import { useState, useRef, useEffect, useCallback, useMemo } from "react";
import { ArrowUp, Loader2, RotateCcw, ChevronDown, ArrowDown, Plus } from "lucide-react";
import { chatStream, type ChatMessage, type TokenUsage } from "@/api/client";
import MessageBubble from "./MessageBubble";

interface DisplayMessage {
  id: string;
  role: "user" | "assistant" | "tool";
  content: string;
  toolName?: string;
  usage?: TokenUsage;
}

const STORAGE_KEY = "treasury-chat-history";
const MODEL_KEY = "treasury-model";
const load = (): DisplayMessage[] => { try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]"); } catch { return []; } };
const save = (msgs: DisplayMessage[]) => localStorage.setItem(STORAGE_KEY, JSON.stringify(msgs.filter((m) => m.role !== "tool").slice(-100)));

interface ModelOption {
  id: string;
  label: string;
  price: string;
  tag: string;
  family: string;
}

const MODELS: ModelOption[] = [
  { id: "gpt-5.4",      label: "GPT-5.4",      price: "$2.50 / $15.00", tag: "",            family: "GPT-5.4" },
  { id: "gpt-5.4-mini", label: "GPT-5.4 Mini", price: "$0.75 / $4.50",  tag: "",            family: "GPT-5.4" },
  { id: "gpt-5.4-nano", label: "GPT-5.4 Nano", price: "$0.20 / $1.25",  tag: "",            family: "GPT-5.4" },
  { id: "gpt-4.1-mini", label: "GPT-4.1 Mini", price: "$0.40 / $1.60",  tag: "recomendado", family: "GPT-4.1" },
  { id: "gpt-4.1",      label: "GPT-4.1",      price: "$2.00 / $8.00",  tag: "",            family: "GPT-4.1" },
  { id: "gpt-4.1-nano", label: "GPT-4.1 Nano", price: "$0.10 / $0.40",  tag: "barato",      family: "GPT-4.1" },
  { id: "gpt-4o",       label: "GPT-4o",       price: "$2.50 / $10.00", tag: "",            family: "GPT-4o" },
  { id: "gpt-4o-mini",  label: "GPT-4o Mini",  price: "$0.15 / $0.60",  tag: "barato",      family: "GPT-4o" },
];

const SUGGESTIONS = [
  "Precifique uma LTN com taxa 12,75% a.a. vencendo em 2027",
  "Calcule o DV01 de uma NTN-F 2031",
  "Explique duration modificada vs Macaulay",
  "O que é o cupom cambial e como se calcula?",
];

let msgId = Date.now();

function formatTokensShort(n: number): string {
  if (n >= 1_000_000) return `${(n / 1_000_000).toFixed(1)}M`;
  if (n >= 1000) return `${(n / 1000).toFixed(1)}k`;
  return String(n);
}

function formatCostShort(usd: number): string {
  if (usd === 0) return "$0.00";
  if (usd < 0.01) return `$${usd.toFixed(4)}`;
  return `$${usd.toFixed(3)}`;
}

export default function ChatPanel() {
  const [messages, setMessages] = useState<DisplayMessage[]>(load);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [model, setModel] = useState(() => localStorage.getItem(MODEL_KEY) || "gpt-4.1-mini");
  const [showModels, setShowModels] = useState(false);
  const [showScrollBtn, setShowScrollBtn] = useState(false);
  const inputRef = useRef<HTMLTextAreaElement>(null);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const scrollRef = useRef<HTMLDivElement>(null);
  const stickToBottom = useRef(true);
  const rafId = useRef(0);

  const doScroll = useCallback(() => {
    cancelAnimationFrame(rafId.current);
    rafId.current = requestAnimationFrame(() => {
      const el = scrollRef.current;
      if (el && stickToBottom.current) el.scrollTop = el.scrollHeight;
    });
  }, []);

  const sessionTotals = useMemo(() => {
    let tokens = 0, cost = 0;
    for (const m of messages) {
      if (m.usage) { tokens += m.usage.total_tokens; cost += m.usage.estimated_cost_usd; }
    }
    return { tokens, cost };
  }, [messages]);

  const chatTitle = useMemo(() => {
    const first = messages.find((m) => m.role === "user");
    if (!first) return "Nova conversa";
    const text = first.content.slice(0, 50);
    return text.length < first.content.length ? text + "..." : text;
  }, [messages]);

  useEffect(() => { doScroll(); }, [messages, doScroll]);
  useEffect(() => { save(messages); }, [messages]);
  useEffect(() => { localStorage.setItem(MODEL_KEY, model); }, [model]);

  useEffect(() => {
    const el = scrollRef.current;
    if (!el) return;
    const handler = () => {
      const gap = el.scrollHeight - el.scrollTop - el.clientHeight;
      stickToBottom.current = gap < 60;
      setShowScrollBtn(gap >= 60 && isLoading);
    };
    el.addEventListener("scroll", handler, { passive: true });
    return () => el.removeEventListener("scroll", handler);
  }, [isLoading]);

  useEffect(() => { if (!isLoading) setShowScrollBtn(false); }, [isLoading]);

  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) setShowModels(false);
    };
    document.addEventListener("mousedown", handler);
    return () => document.removeEventListener("mousedown", handler);
  }, []);

  const handleSend = useCallback(async (text?: string) => {
    const content = (text || input).trim();
    if (!content || isLoading) return;

    const userMsg: DisplayMessage = { id: `m-${++msgId}`, role: "user", content };
    const aId = `m-${++msgId}`;
    const assistantMsg: DisplayMessage = { id: aId, role: "assistant", content: "" };
    setMessages((p) => [...p, userMsg, assistantMsg]);
    setInput("");
    setIsLoading(true);
    stickToBottom.current = true;

    const history: ChatMessage[] = [
      ...messages.filter((m) => m.role !== "tool").map((m) => ({ role: m.role as "user" | "assistant", content: m.content })),
      { role: "user" as const, content },
    ];

    const contentBuf = { current: "" };
    const flushTimer = setInterval(() => {
      const snapshot = contentBuf.current;
      setMessages((p) => p.map((m) => m.id === aId ? { ...m, content: snapshot } : m));
    }, 60);

    const flush = () => {
      setMessages((p) => p.map((m) => m.id === aId ? { ...m, content: contentBuf.current } : m));
    };

    try {
      for await (const ev of chatStream(history, model)) {
        if (ev.type === "content" && ev.content) {
          contentBuf.current += ev.content;
        } else if (ev.type === "tool_call" && ev.tool) {
          flush();
          const tm: DisplayMessage = { id: `m-${++msgId}`, role: "tool", content: "", toolName: ev.tool };
          setMessages((p) => { const i = p.findIndex((m) => m.id === aId); if (i === -1) return [...p, tm]; const c = [...p]; c.splice(i, 0, tm); return c; });
        } else if (ev.type === "usage") {
          flush();
          const usage: TokenUsage = {
            prompt_tokens: ev.prompt_tokens ?? 0, completion_tokens: ev.completion_tokens ?? 0,
            total_tokens: ev.total_tokens ?? 0, estimated_cost_usd: ev.estimated_cost_usd ?? 0, model: ev.model ?? "",
          };
          setMessages((p) => p.map((m) => m.id === aId ? { ...m, content: contentBuf.current, usage } : m));
        }
      }
      flush();
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : "Erro desconhecido";
      flush();
      setMessages((p) => p.map((m) => m.id === aId ? { ...m, content: contentBuf.current || `Erro: ${msg}` } : m));
    } finally { clearInterval(flushTimer); setIsLoading(false); inputRef.current?.focus(); }
  }, [input, isLoading, messages, model]);

  const handleClear = () => { setMessages([]); localStorage.removeItem(STORAGE_KEY); };

  const forceScrollToBottom = () => {
    stickToBottom.current = true;
    const el = scrollRef.current;
    if (el) el.scrollTop = el.scrollHeight;
  };

  const currentModel = MODELS.find((m) => m.id === model) || MODELS[3];

  const families = useMemo(() => {
    const map = new Map<string, ModelOption[]>();
    for (const m of MODELS) { const arr = map.get(m.family) || []; arr.push(m); map.set(m.family, arr); }
    return map;
  }, []);

  return (
    <div className="flex h-full flex-col">
      {/* Chat header */}
      <div className="flex h-12 shrink-0 items-center justify-between border-b border-border bg-base px-4">
        <div className="flex items-center gap-2 min-w-0">
          <button
            onClick={handleClear}
            className="flex h-7 items-center gap-1.5 rounded-md border border-border px-2.5 text-[12px] font-medium text-txt-muted transition-colors hover:bg-surface hover:text-txt-secondary"
            title="Nova conversa"
          >
            <Plus size={13} />
            <span className="hidden sm:inline">Nova</span>
          </button>
          <span className="truncate text-[13px] font-medium text-txt-secondary">{chatTitle}</span>
        </div>

        <div className="flex items-center gap-3">
          {sessionTotals.tokens > 0 && (
            <div className="hidden sm:flex items-center gap-1.5 mono text-[11px] text-txt-muted">
              <span>{formatTokensShort(sessionTotals.tokens)} tok</span>
              <span className="text-border-light">·</span>
              <span>{formatCostShort(sessionTotals.cost)}</span>
            </div>
          )}

          {/* Model selector */}
          <div ref={dropdownRef} className="relative">
            <button
              onClick={() => setShowModels((v) => !v)}
              className="flex items-center gap-1 rounded-md border border-border px-2.5 py-1 text-[11px] font-medium text-txt-muted transition-colors hover:bg-surface hover:text-txt-secondary"
            >
              <span className="mono">{currentModel.label}</span>
              <ChevronDown size={12} />
            </button>

            {showModels && (
              <div className="absolute top-full right-0 mt-1 w-80 rounded-lg border border-border bg-base shadow-lg z-50">
                <div className="px-3 py-2 text-[10px] font-semibold uppercase tracking-wider text-txt-muted">
                  Modelo · in / out por 1M tokens (USD)
                </div>
                {Array.from(families.entries()).map(([family, models], fi) => (
                  <div key={family}>
                    {fi > 0 && <div className="mx-3 border-t border-border" />}
                    <div className="px-3 pt-2 pb-1 text-[10px] font-semibold text-txt-muted">{family}</div>
                    {models.map((m) => (
                      <button
                        key={m.id}
                        onClick={() => { setModel(m.id); setShowModels(false); }}
                        className={`flex w-full items-center gap-2 px-3 py-2 text-left transition-colors hover:bg-surface ${
                          model === m.id ? "bg-accent-light/50" : ""
                        }`}
                      >
                        <div className="flex-1">
                          <div className="flex items-center gap-2">
                            <span className="text-[13px] font-medium text-txt">{m.label}</span>
                            {m.tag && (
                              <span className={`rounded px-1.5 py-0.5 text-[9px] font-semibold uppercase ${
                                m.tag === "recomendado" ? "bg-accent/10 text-accent" : "bg-surface text-txt-muted"
                              }`}>{m.tag}</span>
                            )}
                          </div>
                          <div className="mono text-[11px] text-txt-muted">{m.price}</div>
                        </div>
                        {model === m.id && <div className="h-1.5 w-1.5 rounded-full bg-accent" />}
                      </button>
                    ))}
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Chat body */}
      <div className="treasury-scroll relative flex-1 overflow-y-auto" ref={scrollRef}>
        {messages.length === 0 ? (
          <div className="flex h-full flex-col items-center justify-center px-6">
            <div className="mb-8 text-center">
              <h2 className="text-2xl font-semibold tracking-tight text-txt">
                O que posso calcular para voce?
              </h2>
              <p className="mt-2 text-[14px] text-txt-muted">
                Precificacao ANBIMA, risco, derivativos, curvas — 90+ ferramentas de renda fixa.
              </p>
            </div>
            <div className="grid w-full max-w-xl grid-cols-2 gap-2">
              {SUGGESTIONS.map((text, i) => (
                <button key={i} onClick={() => handleSend(text)}
                  className="rounded-lg border border-border bg-base px-4 py-3 text-left text-[13px] leading-snug text-txt-secondary transition-colors hover:border-accent/40 hover:bg-accent-light/50"
                >{text}</button>
              ))}
            </div>
          </div>
        ) : (
          <div className="mx-auto max-w-5xl px-6 py-6">
            {messages.map((msg) => (
              <MessageBubble key={msg.id} role={msg.role} content={msg.content}
                toolName={msg.toolName} usage={msg.usage}
                isStreaming={isLoading && msg.role === "assistant" && msg === messages[messages.length - 1]}
              />
            ))}
          </div>
        )}

        {showScrollBtn && (
          <button onClick={forceScrollToBottom}
            className="absolute bottom-4 left-1/2 -translate-x-1/2 flex items-center gap-1.5 rounded-full border border-border bg-base px-3 py-1.5 text-[12px] font-medium text-txt-secondary shadow-md transition-colors hover:bg-surface"
          ><ArrowDown size={13} /> Seguir resposta</button>
        )}
      </div>

      {/* Input bar */}
      <div className="border-t border-border bg-base px-4 pb-4 pt-3">
        <div className="mx-auto flex max-w-5xl items-end gap-2">
          <div className="relative flex-1">
            <textarea ref={inputRef} value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); handleSend(); } }}
              placeholder="Pergunte sobre tesouraria, renda fixa, derivativos..."
              rows={1} className="input-field w-full resize-none rounded-xl py-3 pl-4 pr-12"
              style={{ maxHeight: 120 }}
              onInput={(e) => { const t = e.currentTarget; t.style.height = "auto"; t.style.height = Math.min(t.scrollHeight, 120) + "px"; }}
            />
            <button onClick={() => handleSend()} disabled={!input.trim() || isLoading}
              className="absolute bottom-2 right-2 flex h-8 w-8 items-center justify-center rounded-lg bg-accent text-txt-inverse transition-colors hover:bg-accent-hover disabled:opacity-30"
            >{isLoading ? <Loader2 size={15} className="animate-spin" /> : <ArrowUp size={15} />}</button>
          </div>
        </div>
      </div>
    </div>
  );
}
