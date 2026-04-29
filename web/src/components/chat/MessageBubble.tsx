import { memo } from "react";
import { cn } from "@/lib/utils";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";
import MermaidBlock from "./MermaidBlock";
import type { TokenUsage } from "@/api/client";

interface Props {
  role: "user" | "assistant" | "tool";
  content: string;
  toolName?: string;
  usage?: TokenUsage;
  isStreaming?: boolean;
}

function formatCost(usd: number): string {
  if (usd < 0.01) return `$${usd.toFixed(4)}`;
  return `$${usd.toFixed(3)}`;
}

function formatTokens(n: number): string {
  if (n >= 1000) return `${(n / 1000).toFixed(1)}k`;
  return String(n);
}

export default memo(function MessageBubble({ role, content, usage, isStreaming }: Props) {
  if (role === "tool") return null;

  const isUser = role === "user";

  return (
    <div className="py-4">
      <div className="flex gap-3">
        <div
          className={cn(
            "mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-full text-[12px] font-semibold",
            isUser ? "bg-txt text-txt-inverse" : "bg-accent/10 text-accent"
          )}
        >
          {isUser ? "V" : "T"}
        </div>

        <div className="min-w-0 flex-1 pt-0.5">
          <div className="mb-1 text-[11px] font-medium uppercase tracking-wider text-txt-muted">
            {isUser ? "Voce" : "Treasury"}
          </div>

          {isUser ? (
            <p className="text-[14px] leading-relaxed text-txt">{content}</p>
          ) : (
            <>
              <div className="treasury-prose">
                <ReactMarkdown
                  remarkPlugins={[remarkGfm, remarkMath]}
                  rehypePlugins={[rehypeKatex]}
                  components={{
                    table: ({ children, ...props }) => (
                      <div className="treasury-table-wrap">
                        <table {...props}>{children}</table>
                      </div>
                    ),
                    code: ({ children, className, ...props }) => {
                      const lang = className?.replace("language-", "");

                      if (lang === "mermaid") {
                        return <MermaidBlock code={String(children).trim()} />;
                      }

                      if (className?.includes("language-")) {
                        return (
                          <code className={className} {...props}>
                            {children}
                          </code>
                        );
                      }

                      return (
                        <code className="treasury-inline-code" {...props}>
                          {children}
                        </code>
                      );
                    },
                  }}
                >
                  {content}
                </ReactMarkdown>
                {isStreaming && <span className="treasury-streaming-dot" />}
              </div>

              {usage && !isStreaming && (
                <div className="treasury-usage">
                  <span title="Tokens de entrada (prompt)">
                    in {formatTokens(usage.prompt_tokens)}
                  </span>
                  <span className="treasury-usage-sep" />
                  <span title="Tokens de saida (resposta)">
                    out {formatTokens(usage.completion_tokens)}
                  </span>
                  <span className="treasury-usage-sep" />
                  <span title="Custo estimado (USD)">
                    {formatCost(usage.estimated_cost_usd)}
                  </span>
                  <span className="treasury-usage-sep" />
                  <span title="Modelo">{usage.model}</span>
                </div>
              )}
            </>
          )}
        </div>
      </div>
    </div>
  );
});
