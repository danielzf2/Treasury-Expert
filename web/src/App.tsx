import { Routes, Route } from "react-router-dom";
import Shell from "@/components/layout/Shell";
import ChatPage from "@/pages/ChatPage";
import PortfolioPage from "@/pages/PortfolioPage";
import CashflowsPage from "@/pages/CashflowsPage";

export default function App() {
  return (
    <Routes>
      <Route element={<Shell />}>
        <Route path="/" element={<ChatPage />} />
        <Route path="/portfolio" element={<PortfolioPage />} />
        <Route path="/cashflows" element={<CashflowsPage />} />
        <Route path="*" element={<ChatPage />} />
      </Route>
    </Routes>
  );
}
