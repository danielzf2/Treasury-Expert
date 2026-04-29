import { useEffect, useState } from "react";

interface HealthData {
  online: boolean;
  sections?: number;
  documents?: number;
}

export function useHealth(intervalMs = 30_000) {
  const [health, setHealth] = useState<HealthData>({ online: false });

  useEffect(() => {
    let active = true;

    const check = async () => {
      try {
        const res = await fetch("/api/health", { signal: AbortSignal.timeout(5000) });
        if (!active) return;
        if (res.ok) {
          const data = await res.json();
          setHealth({ online: true, sections: data.sections, documents: data.documents });
        } else {
          setHealth({ online: false });
        }
      } catch {
        if (active) setHealth({ online: false });
      }
    };

    check();
    const id = setInterval(check, intervalMs);
    return () => { active = false; clearInterval(id); };
  }, [intervalMs]);

  return health;
}
