import { NavLink } from "react-router-dom";
import { MessageSquare, Briefcase, CalendarDays, Sun, Moon } from "lucide-react";
import { cn } from "@/lib/utils";
import { useTheme } from "@/stores/theme";
import { useHealth } from "@/hooks/useHealth";

const NAV = [
  { to: "/", icon: MessageSquare, label: "Chat" },
  { to: "/portfolio", icon: Briefcase, label: "Carteira" },
  { to: "/cashflows", icon: CalendarDays, label: "Fluxos" },
];

export default function Sidebar() {
  const { theme, toggle } = useTheme();
  const health = useHealth();

  return (
    <aside className="flex w-[220px] shrink-0 flex-col border-r border-border bg-base">
      <div className="px-5 pt-5 pb-4">
        <div className="flex items-center gap-2.5">
          <div className="flex h-7 w-7 items-center justify-center rounded-md bg-accent">
            <span className="text-[13px] font-bold text-txt-inverse">T</span>
          </div>
          <div>
            <div className="text-[15px] font-semibold leading-tight tracking-tight text-txt">
              Treasury
            </div>
            <div className="text-[11px] leading-tight text-txt-muted">
              Tesouraria & Renda Fixa
            </div>
          </div>
        </div>
      </div>

      <nav className="flex flex-1 flex-col gap-0.5 px-3 pt-1">
        {NAV.map(({ to, icon: Icon, label }) => (
          <NavLink
            key={to}
            to={to}
            end={to === "/"}
            className={({ isActive }) =>
              cn(
                "flex items-center gap-2.5 rounded-lg px-3 py-2 text-[13px] font-medium transition-colors",
                isActive
                  ? "bg-accent/10 text-accent"
                  : "text-txt-secondary hover:bg-surface hover:text-txt"
              )
            }
          >
            <Icon size={15} strokeWidth={2} />
            <span>{label}</span>
          </NavLink>
        ))}
      </nav>

      <div className="border-t border-border px-4 py-3 flex flex-col gap-2.5">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className={cn(
              "h-[7px] w-[7px] rounded-full",
              health.online ? "bg-success" : "bg-danger"
            )} />
            <span className="text-[11px] font-medium text-txt-muted">
              {health.online ? "Online" : "Offline"}
            </span>
            {health.online && health.sections && (
              <span className="text-[10px] text-txt-muted">
                · {health.sections} seções
              </span>
            )}
          </div>
          <button
            onClick={toggle}
            className="flex h-7 w-7 items-center justify-center rounded-md text-txt-muted transition-colors hover:bg-surface hover:text-txt-secondary"
            title={theme === "light" ? "Modo escuro" : "Modo claro"}
          >
            {theme === "light" ? <Moon size={14} /> : <Sun size={14} />}
          </button>
        </div>
      </div>
    </aside>
  );
}
