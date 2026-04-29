export const TYPE_COLORS: Record<string, string> = {
  LTN: "#0c7bb3",
  "NTN-F": "#6366f1",
  "NTN-B": "#059669",
  LFT: "#d97706",
};

export const FALLBACK_COLOR = "#94a3b8";

export function colorForType(type: string): string {
  return TYPE_COLORS[type] || FALLBACK_COLOR;
}
