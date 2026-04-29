"""Presets do simulador (copia exata de server/api/simulator.py PRESETS).

Mantemos uma copia local pra que os testes nao dependam de mudancas no PRESETS
do simulator e expoem qualquer alteracao acidental.
"""

from __future__ import annotations

# Os 8 presets do simulador (29/04/2026)
PRESETS_INPUT = {
    "Casada LTN+DI1": [
        {"instrument": "LTN", "ticker": "F32", "direction": "C", "quantity": 2000,
         "taxa": 13.7625, "corr_type": "% na taxa", "corr_value": 0.001},
        {"instrument": "DI1", "ticker": "F32", "direction": "C", "quantity": 20,
         "taxa": 13.650, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "Venda Casada LTN+DI1": [
        {"instrument": "LTN", "ticker": "F32", "direction": "V", "quantity": 2000,
         "taxa": 13.7625, "corr_type": "% na taxa", "corr_value": 0.001},
        {"instrument": "DI1", "ticker": "F32", "direction": "V", "quantity": 20,
         "taxa": 13.650, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "Casada NTN-F+DI1": [
        {"instrument": "NTN-F", "ticker": "F31", "direction": "C", "quantity": 2000,
         "taxa": 13.80, "corr_type": "% na taxa", "corr_value": 0.001},
        {"instrument": "DI1", "ticker": "F31", "direction": "C", "quantity": 20,
         "taxa": 13.65, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "Casada NTN-B+DAP": [
        {"instrument": "NTN-B", "ticker": "N29", "direction": "C", "quantity": 2000,
         "taxa": 7.50, "corr_type": "% na taxa", "corr_value": 0.001, "vna": 4500.0},
        {"instrument": "DAP", "ticker": "N29", "direction": "C", "quantity": 20,
         "taxa": 7.40, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "DOL+DI1 (cupom sint.)": [
        {"instrument": "DOL", "ticker": "K26", "direction": "C", "quantity": 10,
         "taxa": 4976.5, "corr_type": "Nenhuma", "corr_value": 0.0},
        {"instrument": "DI1", "ticker": "K26", "direction": "C", "quantity": 10,
         "taxa": 14.60, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "DI1+FRC (dol sint.)": [
        {"instrument": "DI1", "ticker": "F28", "direction": "C", "quantity": 20,
         "taxa": 14.60, "corr_type": "R$/contrato", "corr_value": 1.30},
        {"instrument": "FRC", "ticker": "F28", "direction": "V", "quantity": 20,
         "taxa": 5.06, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "FRC direcional": [
        {"instrument": "FRC", "ticker": "F28", "direction": "C", "quantity": 20,
         "taxa": 5.06, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "LTN direcional": [
        {"instrument": "LTN", "ticker": "F32", "direction": "C", "quantity": 2000,
         "taxa": 13.76, "corr_type": "% na taxa", "corr_value": 0.001},
    ],
}

PRESET_NAMES = list(PRESETS_INPUT.keys())

# Presets que tem TPF com cupom (para testes de hedge/strip)
COUPON_PRESETS = ["Casada NTN-F+DI1", "Casada NTN-B+DAP"]

# Presets onde detect_strategy retorna 'casada' (TPF + DI/DAP mesmo vcto, mesma direcao)
CASADA_PRESETS = [
    "Casada LTN+DI1", "Venda Casada LTN+DI1",
    "Casada NTN-F+DI1", "Casada NTN-B+DAP",
]

# Presets com cupom cambial sintetico (DOL + DI1, mesma direcao)
CUPOM_SINT_PRESETS = ["DOL+DI1 (cupom sint.)"]

# Presets com dolar sintetico (DI1 + FRC, direcoes opostas)
DOL_SINT_PRESETS = ["DI1+FRC (dol sint.)"]

SINGLE_LEG_PRESETS = ["FRC direcional", "LTN direcional"]
