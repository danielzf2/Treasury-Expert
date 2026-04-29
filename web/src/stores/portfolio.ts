import { create } from "zustand";
import { persist } from "zustand/middleware";
import type { BondRequest } from "@/api/client";

export interface Bond extends BondRequest {
  id: string;
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

interface PortfolioState {
  bonds: Bond[];
  addBond: (bond: Omit<Bond, "id">) => void;
  removeBond: (id: string) => void;
  updateBond: (id: string, updates: Partial<Bond>) => void;
  clearPortfolio: () => void;
}

let nextId = Date.now();

export const usePortfolioStore = create<PortfolioState>()(
  persist(
    (set) => ({
      bonds: [],

      addBond: (bond) =>
        set((s) => ({
          bonds: [...s.bonds, { ...bond, id: `bond-${++nextId}` }],
        })),

      removeBond: (id) =>
        set((s) => ({ bonds: s.bonds.filter((b) => b.id !== id) })),

      updateBond: (id, updates) =>
        set((s) => ({
          bonds: s.bonds.map((b) => (b.id === id ? { ...b, ...updates } : b)),
        })),

      clearPortfolio: () => set({ bonds: [] }),
    }),
    { name: "treasury-portfolio" }
  )
);
