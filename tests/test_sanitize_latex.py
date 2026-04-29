"""Testes para scripts/sanitize_latex.py — protege contra regressões nas regex."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from sanitize_latex import apply_transformations


def _t(inp: str) -> str:
    out, _ = apply_transformations(inp)
    return out.strip()


# ── Delimitadores $$  e $ ─────────────────────────────────────────────────────

def test_remove_double_dollar():
    assert "x + y" in _t("$$x + y$$")


def test_remove_inline_dollar():
    assert _t("$x$") == "x"


def test_preserve_currency_dollar():
    result = _t("US$ 100")
    assert "US$" in result or "US" in result
    assert "100" in result


# ── \\frac ────────────────────────────────────────────────────────────────────

def test_simple_frac():
    assert "a/b" in _t(r"\frac{a}{b}")


def test_nested_frac():
    result = _t(r"\frac{\frac{a}{b}}{c}")
    assert "a/b" in result
    assert "/c" in result


# ── \\sqrt ────────────────────────────────────────────────────────────────────

def test_sqrt():
    assert "√(x)" in _t(r"\sqrt{x}")


# ── \\sum, \\prod, \\int ─────────────────────────────────────────────────────

def test_sum_with_limits():
    result = _t(r"\sum_{i=1}^{n}")
    assert "Σ" in result
    assert "i=1" in result
    assert "n" in result


def test_prod():
    assert "∏" in _t(r"\prod")


def test_integral_with_limits():
    result = _t(r"\int_{0}^{T}")
    assert "∫" in result
    assert "0" in result
    assert "T" in result


# ── Letras gregas ─────────────────────────────────────────────────────────────

def test_greek_alpha():
    assert "α" in _t(r"\alpha")


def test_greek_beta():
    assert "β" in _t(r"\beta")


def test_greek_sigma():
    assert "σ" in _t(r"\sigma")


def test_greek_delta_upper():
    assert "Δ" in _t(r"\Delta")


def test_greek_delta_lower():
    assert "δ" in _t(r"\delta")


def test_greek_pi():
    assert "π" in _t(r"\pi")


def test_greek_lambda():
    assert "λ" in _t(r"\lambda")


# ── Operadores ────────────────────────────────────────────────────────────────

def test_times():
    assert "×" in _t(r"\times")


def test_cdot():
    assert "·" in _t(r"\cdot")


def test_div():
    assert "÷" in _t(r"\div")


def test_leq():
    assert "≤" in _t(r"\leq")


def test_geq():
    assert "≥" in _t(r"\geq")


def test_neq():
    assert "≠" in _t(r"\neq")


def test_approx():
    assert "≈" in _t(r"\approx")


# ── Setas ─────────────────────────────────────────────────────────────────────

def test_rightarrow():
    assert "⇒" in _t(r"\Rightarrow")


def test_to():
    assert "→" in _t(r"\to")


# ── Funções matemáticas ──────────────────────────────────────────────────────

def test_ln():
    assert "ln" in _t(r"\ln")


def test_exp():
    assert "exp" in _t(r"\exp")


# ── Delimitadores \\left \\right ──────────────────────────────────────────────

def test_left_right_parens():
    result = _t(r"\left( x \right)")
    assert "(" in result
    assert ")" in result
    assert "left" not in result


# ── \\text, \\mathrm, etc. ───────────────────────────────────────────────────

def test_text():
    assert _t(r"\text{mod}") == "mod"


def test_mathrm():
    assert _t(r"\mathrm{PU}") == "PU"


def test_mathbf():
    assert _t(r"\mathbf{v}") == "v"


def test_operatorname():
    assert _t(r"\operatorname{diag}") == "diag"


# ── Superscripts e subscripts ────────────────────────────────────────────────

def test_superscript_squared():
    assert "²" in _t("x^{2}")


def test_superscript_cubed():
    assert "³" in _t("x^{3}")


def test_superscript_complex():
    result = _t("x^{n+1}")
    assert "^(n+1)" in result


def test_subscript_digit():
    result = _t("x_{0}")
    assert "₀" in result


def test_subscript_i():
    result = _t("x_{i}")
    assert "ᵢ" in result


# ── Ambientes ─────────────────────────────────────────────────────────────────

def test_aligned():
    result = _t(r"\begin{aligned} x = 1 \end{aligned}")
    assert "x = 1" in result
    assert "aligned" not in result


def test_cases():
    result = _t(r"\begin{cases} a \\ b \end{cases}")
    assert "a" in result
    assert "cases" not in result


# ── Casos combinados (reais de OCR) ──────────────────────────────────────────

def test_duration_formula():
    inp = r"$$D_{\text{mod}} = \frac{D_{\text{mac}}}{1 + y}$$"
    result = _t(inp)
    assert "Dmod" in result or "mod" in result
    assert "/" in result
    assert "$$" not in result
    assert "frac" not in result


def test_pv_formula():
    inp = r"$$PV = \sum_{k=1}^{n} \frac{C_k}{(1+r)^k}$$"
    result = _t(inp)
    assert "PV" in result
    assert "Σ" in result
    assert "$$" not in result
    assert "frac" not in result


def test_partial_derivative():
    assert "∂" in _t(r"\partial")


def test_infty():
    assert "∞" in _t(r"\infty")


def test_dots():
    assert "..." in _t(r"\ldots")
    assert "..." in _t(r"\cdots")


def test_hat_bar():
    result_hat = _t(r"\hat{x}")
    assert "x" in result_hat
    result_bar = _t(r"\bar{y}")
    assert "y" in result_bar


def test_tag_removed():
    result = _t(r"x = 1 \tag{3.1}")
    assert "x = 1" in result
    assert "tag" not in result
    assert "3.1" not in result


# ── Recuperação de comandos sem backslash (runs anteriores) ──────────────────

def test_frac_no_backslash():
    result = _t("frac{a}{b}")
    assert "a/b" in result
    assert "frac" not in result


def test_mathrm_no_backslash():
    result = _t("mathrm{PV}")
    assert result.strip() == "PV"


def test_sum_no_backslash():
    result = _t("sum_{i=1}^{n}")
    assert "Σ" in result


def test_sqrt_no_backslash():
    result = _t("sqrt{x}")
    assert "√(x)" in result


# ── Espaços do OCR entre comando e braces ────────────────────────────────────

def test_frac_with_spaces():
    result = _t(r"\frac {a} {b}")
    assert "a/b" in result
    assert "frac" not in result


def test_text_with_spaces():
    result = _t(r"\text {mod}")
    assert "mod" in result
    assert "text" not in result


def test_sum_with_spaces():
    result = _t(r"\sum _ {i=1} ^ {n}")
    assert "Σ" in result


# ── Caso real: fórmula do PV com mathrm e frac aninhados ─────────────────────

def test_real_pv_formula_with_mathrm():
    inp = r"\mathrm{PV} = \frac{\mathrm{F}_{1}}{(1 + \mathrm{i}_{1})^{d_{1}}}"
    result = _t(inp)
    assert "PV" in result
    assert "/" in result
    assert "mathrm" not in result
    assert "frac" not in result


def test_real_duration_formula_with_sum():
    inp = r"D = \frac{\sum_{j=1}^{n} \frac{F_{j}}{(1+i_{j})^{d_{j}}} \times d_{j}}{PV}"
    result = _t(inp)
    assert "Σ" in result
    assert "/" in result
    assert "frac" not in result
    assert "sum" not in result
