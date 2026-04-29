import BondCalculator from "@/components/calculator/BondCalculator";

export default function CalculatorPage() {
  return (
    <div className="flex h-full flex-col overflow-y-auto">
      <div className="page-header">
        <h1 className="page-title">Calculadora de Titulos</h1>
        <p className="page-subtitle">
          Precificacao ANBIMA com truncamentos e arredondamentos oficiais
        </p>
      </div>
      <div className="flex-1 p-6">
        <BondCalculator />
      </div>
    </div>
  );
}
