import { useEffect, useRef, useState } from "react";
import mermaid from "mermaid";

mermaid.initialize({
  startOnLoad: false,
  theme: "neutral",
  fontFamily: "Inter, sans-serif",
  fontSize: 13,
  flowchart: { curve: "basis", padding: 16, htmlLabels: true },
  suppressErrorRendering: true,
});

let counter = 0;

export default function MermaidBlock({ code }: { code: string }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [svg, setSvg] = useState("");
  const [error, setError] = useState(false);
  const timerRef = useRef<ReturnType<typeof setTimeout>>(undefined);

  useEffect(() => {
    setSvg("");
    setError(false);

    if (timerRef.current) clearTimeout(timerRef.current);

    timerRef.current = setTimeout(() => {
      const id = `mermaid-${++counter}`;
      mermaid
        .render(id, code)
        .then(({ svg: result }) => setSvg(result))
        .catch(() => setError(true));
    }, 400);

    return () => { if (timerRef.current) clearTimeout(timerRef.current); };
  }, [code]);

  if (error) {
    return (
      <pre className="treasury-pre-fallback">
        <code>{code}</code>
      </pre>
    );
  }

  if (!svg) return null;

  return (
    <div
      ref={containerRef}
      className="treasury-mermaid"
      dangerouslySetInnerHTML={{ __html: svg }}
    />
  );
}
