#!/usr/bin/env python3
"""
sanitize_latex.py — Converte resíduos de notação LaTeX em texto legível nos arquivos .md.
Uso: python scripts/sanitize_latex.py [diretório] [--dry-run]
"""

import re
import sys
import argparse
from pathlib import Path


# ---------------------------------------------------------------------------
# Padrões reutilizáveis
# ---------------------------------------------------------------------------

# Conteúdo com até 2 níveis de braces aninhados
_N2 = r'(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*'
# Conteúdo com 1 nível de braces aninhados
_N1 = r'(?:[^{}]|\{[^{}]*\})*'

# \frac{A}{B} — com ou sem backslash, espaços opcionais do OCR
FRAC_WITH_BS = re.compile(r'\\frac\s*\{(' + _N2 + r')\}\s*\{(' + _N2 + r')\}')
FRAC_NO_BS = re.compile(r'(?<![a-zA-Z])frac\s*\{(' + _N2 + r')\}\s*\{(' + _N2 + r')\}')

LATEX_COMMANDS = {
    'frac', 'sqrt', 'sum', 'prod', 'int', 'partial', 'infty',
    'Delta', 'delta', 'alpha', 'beta', 'gamma', 'sigma', 'mu',
    'lambda', 'theta', 'pi', 'rho', 'tau', 'nu', 'varepsilon',
    'varphi', 'phi', 'omega', 'Omega', 'Pi', 'Sigma',
    'times', 'cdot', 'div', 'leq', 'geq', 'neq', 'approx',
    'Rightarrow', 'to', 'leftarrow',
    'ln', 'log', 'exp', 'sin', 'cos',
    'left', 'right',
    'text', 'mathrm', 'mathbf', 'operatorname', 'mathit', 'mathcal', 'mathbb',
    'hat', 'bar', 'tilde', 'overline', 'widehat',
    'dots', 'ldots', 'cdots', 'quad', 'qquad',
    'tag', 'pmb',
    'begin', 'end',
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

SUPERSCRIPT_MAP = {'2': '²', '3': '³'}
SUBSCRIPT_MAP = {
    '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
    '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
    'i': 'ᵢ', 'k': 'ₖ', 'n': 'ₙ',
}


def replace_superscripts(text: str) -> str:
    def repl(m):
        inner = m.group(1)
        if inner in SUPERSCRIPT_MAP:
            return SUPERSCRIPT_MAP[inner]
        if inner == 'n':
            return '^n'
        if len(inner) == 1:
            return f'^{inner}'
        return f'^({inner})'
    return re.sub(r'\^\s*\{([^{}]+)\}', repl, text)


def replace_subscripts(text: str) -> str:
    def repl(m):
        inner = m.group(1)
        if inner in SUBSCRIPT_MAP:
            return SUBSCRIPT_MAP[inner]
        if len(inner) == 1:
            return f'_{inner}'
        return f'_({inner})'
    return re.sub(r'_\s*\{([^{}]+)\}', repl, text)


def _braced_cmd(cmd: str, with_bs: bool = True) -> re.Pattern:
    """Regex para \\cmd{X} ou cmd{X} com suporte a 1 nível de aninhamento e espaços."""
    prefix = r'\\' + re.escape(cmd) if with_bs else r'(?<![a-zA-Z])' + re.escape(cmd)
    return re.compile(prefix + r'\s*\{(' + _N1 + r')\}')


# ---------------------------------------------------------------------------
# Transformações
# ---------------------------------------------------------------------------

def apply_transformations(text: str) -> tuple[str, int]:
    original = text
    count = 0

    def sub(pattern, repl, t, flags=0):
        nonlocal count
        new_t, n = re.subn(pattern, repl, t, flags=flags)
        count += n
        return new_t

    # 1. Remover delimitadores $$
    text = sub(r'\$\$', '\n', text)

    # 2. Remover $ inline preservando moeda
    text = re.sub(r'([A-Za-z])\$\s+(\d)', lambda m: m.group(1) + '\x00CUR\x00' + m.group(2), text)
    text = sub(r'\$', '', text)
    text = text.replace('\x00CUR\x00', '$ ')

    # 3. \text{X}, \mathrm{X} etc. — ANTES de tudo para reduzir aninhamento
    for cmd in ['text', 'mathrm', 'mathbf', 'operatorname', 'mathit', 'mathcal', 'mathbb']:
        pat = _braced_cmd(cmd, with_bs=True)
        prev_t = None
        while prev_t != text:
            prev_t = text
            text = sub(pat, r'\1', text)

    # 4. \sum, \prod, \int — ANTES dos subscripts (consomem _{...}^{...})
    text = sub(r'\\sum\s*_\s*\{([^{}]*)\}\s*\^\s*\{([^{}]*)\}', lambda m: f'Σ({m.group(1)} até {m.group(2)})', text)
    text = sub(r'\\sum\s*_\s*\{([^{}]*)\}', lambda m: f'Σ({m.group(1)})', text)
    text = sub(r'\\sum\b', 'Σ', text)

    text = sub(r'\\prod\s*_\s*\{([^{}]*)\}\s*\^\s*\{([^{}]*)\}', lambda m: f'∏({m.group(1)} até {m.group(2)})', text)
    text = sub(r'\\prod\b', '∏', text)

    text = sub(r'\\int\s*_\s*\{([^{}]*)\}\s*\^\s*\{([^{}]*)\}', lambda m: f'∫({m.group(1)} até {m.group(2)})', text)
    text = sub(r'\\int\b', '∫', text)

    # 5. ^{X} → superscripts
    prev = None
    while prev != text:
        prev = text
        new_t = replace_superscripts(text)
        if new_t != text:
            count += 1
        text = new_t

    # 6. _{X} → subscripts
    prev = None
    while prev != text:
        prev = text
        new_t = replace_subscripts(text)
        if new_t != text:
            count += 1
        text = new_t

    # 7. \frac{A}{B} → A/B (múltiplas passadas, depois que aninhamento foi reduzido)
    prev = None
    while prev != text:
        prev = text
        new_t, n = FRAC_WITH_BS.subn(lambda m: f"{m.group(1)}/{m.group(2)}", text)
        count += n
        text = new_t

    # 8. \sqrt{X} → √(X)
    text = sub(r'\\sqrt\s*\{([^{}]*)\}', lambda m: f'√({m.group(1)})', text)
    text = sub(r'\\sqrt\b', '√', text)

    # 9. \partial, \infty
    text = sub(r'\\partial\b', '∂', text)
    text = sub(r'\\infty\b', '∞', text)

    # 12. \Delta, \delta
    text = sub(r'\\Delta\b', 'Δ', text)
    text = sub(r'\\delta\b', 'δ', text)

    # 13. Letras gregas
    greek = [
        ('alpha', 'α'), ('beta', 'β'), ('gamma', 'γ'), ('sigma', 'σ'),
        ('mu', 'μ'), ('lambda', 'λ'), ('theta', 'θ'), ('pi', 'π'),
        ('rho', 'ρ'), ('tau', 'τ'), ('nu', 'ν'), ('varepsilon', 'ε'),
        ('varphi', 'φ'), ('phi', 'φ'), ('omega', 'ω'), ('Omega', 'Ω'),
        ('Pi', 'Π'), ('Sigma', 'Σ'),
    ]
    for cmd, sym in greek:
        text = sub(r'\\' + cmd + r'\b', sym, text)

    # 14. Operadores
    text = sub(r'\\times\b', '×', text)
    text = sub(r'\\cdot\b', '·', text)
    text = sub(r'\\div\b', '÷', text)

    # 15. Comparadores
    text = sub(r'\\leq\b', '≤', text)
    text = sub(r'\\geq\b', '≥', text)
    text = sub(r'\\neq\b', '≠', text)
    text = sub(r'\\approx\b', '≈', text)

    # 16. Setas
    text = sub(r'\\Rightarrow\b', '⇒', text)
    text = sub(r'\\to\b', '→', text)
    text = sub(r'\\leftarrow\b', '←', text)

    # 17. Funções matemáticas
    for fn in ['ln', 'log', 'exp', 'sin', 'cos']:
        text = sub(r'\\' + fn + r'\b', fn, text)

    # 18. \left( \right) etc.
    text = sub(r'\\left\s*\(', '(', text)
    text = sub(r'\\right\s*\)', ')', text)
    text = sub(r'\\left\s*\[', '[', text)
    text = sub(r'\\right\s*\]', ']', text)
    text = sub(r'\\left\s*\\?\{', '{', text)
    text = sub(r'\\right\s*\\?\}', '}', text)
    text = sub(r'\\left\s*\|', '|', text)
    text = sub(r'\\right\s*\|', '|', text)
    text = sub(r'\\left\s*\.', '', text)
    text = sub(r'\\right\s*\.', '', text)

    # 19. \hat{X}, \bar{X}, \tilde{X}, \overline{X}
    text = sub(r'\\hat\s*\{([^{}]*)\}', lambda m: m.group(1) + '\u0302', text)
    text = sub(r'\\bar\s*\{([^{}]*)\}', lambda m: m.group(1) + '\u0304', text)
    text = sub(r'\\tilde\s*\{([^{}]*)\}', lambda m: m.group(1) + '\u0303', text)
    text = sub(r'\\overline\s*\{([^{}]*)\}', lambda m: m.group(1) + '\u0304', text)
    text = sub(r'\\widehat\s*\{([^{}]*)\}', lambda m: m.group(1) + '\u0302', text)

    # 20. \dots, \ldots, \quad
    text = sub(r'\\[lc]?dots\b', '...', text)
    text = sub(r'\\quad\b', ' ', text)
    text = sub(r'\\qquad\b', '  ', text)

    # 21. \tag{N} → remover
    text = sub(r'\\tag\s*\{[^{}]*\}', '', text)

    # 22. \pmb{X} → X
    text = sub(r'\\pmb\s*\{([^{}]*)\}', r'\1', text)

    # 23. Ambientes LaTeX
    text = sub(r'\\begin\s*\{aligned\}', '', text, flags=re.DOTALL)
    text = sub(r'\\end\s*\{aligned\}', '', text, flags=re.DOTALL)
    text = sub(r'\\begin\s*\{cases\}', '', text, flags=re.DOTALL)
    text = sub(r'\\end\s*\{cases\}', '', text, flags=re.DOTALL)
    text = sub(r'\\begin\s*\{bmatrix\}', '', text, flags=re.DOTALL)
    text = sub(r'\\end\s*\{bmatrix\}', '', text, flags=re.DOTALL)
    for env in ['equation', 'align', 'gather', 'multline', 'array', 'pmatrix', 'vmatrix', 'matrix']:
        text = sub(r'\\begin\s*\{' + env + r'\*?\}', '', text)
        text = sub(r'\\end\s*\{' + env + r'\*?\}', '', text)

    # 24. \\ (quebra de linha LaTeX) → newline
    text = sub(r'\\\\', '\n', text)

    # 25. Limpar \ remanescentes — SÓ antes de letras que NÃO são comandos conhecidos
    def _safe_strip_backslash(m):
        word = m.group(1)
        if word in LATEX_COMMANDS:
            return m.group(0)
        nonlocal count
        count += 1
        return word
    text = re.sub(r'\\([A-Za-z]+)', _safe_strip_backslash, text)

    # ── PASSO DE RECUPERAÇÃO ──────────────────────────────────────────
    # Pega comandos LaTeX que perderam o \ em runs anteriores do sanitizer.
    # Só casa se NÃO forem precedidos por letra (evita falsos positivos).

    # mathrm{X}, text{X}, etc. sem backslash → X
    for cmd in ['mathrm', 'text', 'mathbf', 'operatorname', 'mathit', 'mathcal', 'mathbb', 'pmb']:
        pat = _braced_cmd(cmd, with_bs=False)
        prev_t = None
        while prev_t != text:
            prev_t = text
            text = sub(pat, r'\1', text)

    # sum_{...}^{...} sem backslash → Σ (ANTES dos subscripts)
    # Braces originais
    text = sub(r'(?<![a-zA-Z])sum\s*_\s*\{([^{}]*)\}\s*\^\s*\{([^{}]*)\}',
               lambda m: f'Σ({m.group(1)} até {m.group(2)})', text)
    text = sub(r'(?<![a-zA-Z])sum\s*_\s*\{([^{}]*)\}',
               lambda m: f'Σ({m.group(1)})', text)
    # Forma já processada por subscript/superscript: sum_(...)^(...) ou sum_(...)^x
    text = sub(r'(?<![a-zA-Z])sum_\(([^)]*)\)\^(?:\(([^)]*)\)|([a-zA-Z0-9]+))',
               lambda m: f'Σ({m.group(1)} até {m.group(2) or m.group(3)})', text)
    text = sub(r'(?<![a-zA-Z])sum_\(([^)]*)\)',
               lambda m: f'Σ({m.group(1)})', text)

    # prod, int sem backslash
    text = sub(r'(?<![a-zA-Z])prod\s*_\s*\{([^{}]*)\}\s*\^\s*\{([^{}]*)\}',
               lambda m: f'∏({m.group(1)} até {m.group(2)})', text)
    text = sub(r'(?<![a-zA-Z])int\s*_\s*\{([^{}]*)\}\s*\^\s*\{([^{}]*)\}',
               lambda m: f'∫({m.group(1)} até {m.group(2)})', text)

    # sqrt{X} sem backslash → √(X)
    text = sub(r'(?<![a-zA-Z])sqrt\s*\{([^{}]*)\}',
               lambda m: f'√({m.group(1)})', text)

    # Subscripts/superscripts órfãos que sobraram
    prev = None
    while prev != text:
        prev = text
        new_t = replace_subscripts(text)
        if new_t != text:
            count += 1
        text = new_t

    prev = None
    while prev != text:
        prev = text
        new_t = replace_superscripts(text)
        if new_t != text:
            count += 1
        text = new_t

    # frac{A}{B} sem backslash → A/B (DEPOIS de subscripts para braces estarem limpos)
    prev = None
    while prev != text:
        prev = text
        new_t, n = FRAC_NO_BS.subn(lambda m: f"{m.group(1)}/{m.group(2)}", text)
        count += n
        text = new_t

    # Limpar espaços extras que o OCR deixa antes de _ e ^
    text = sub(r'\s+_\s*\(', '_(', text)
    text = sub(r'\s+\^\s*\(', '^(', text)

    total = sum(1 for a, b in zip(original, text) if a != b) + abs(len(text) - len(original))
    return text, total


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Sanitiza resíduos LaTeX em arquivos .md')
    default_dir = str(Path(__file__).resolve().parent.parent / 'docs')
    parser.add_argument('directory', nargs='?', default=default_dir, help='Diretório raiz (default: <projeto>/docs)')
    parser.add_argument('--dry-run', action='store_true', help='Mostra o que seria alterado sem salvar')
    args = parser.parse_args()

    root = Path(args.directory)
    if not root.exists():
        print(f'Erro: diretório {root} não encontrado.', file=sys.stderr)
        sys.exit(1)

    md_files = sorted(root.rglob('*.md'))
    if not md_files:
        print(f'Nenhum arquivo .md encontrado em {root}')
        return

    total_files = 0
    total_subs = 0

    for path in md_files:
        try:
            original = path.read_text(encoding='utf-8')
        except Exception as e:
            print(f'  ERRO ao ler {path}: {e}')
            continue

        new_text, n_subs = apply_transformations(original)

        if new_text == original:
            print(f'  sem alterações  {path}')
            continue

        total_files += 1
        total_subs += n_subs

        if args.dry_run:
            print(f'  [dry-run] {path}  ({n_subs} substituições)')
        else:
            try:
                path.write_text(new_text, encoding='utf-8')
                print(f'  ✓ {path}  ({n_subs} substituições)')
            except Exception as e:
                print(f'  ERRO ao gravar {path}: {e}')

    mode = '[dry-run] ' if args.dry_run else ''
    print(f'\n{mode}Total: {total_files} arquivo(s) modificado(s), {total_subs} substituições.')


if __name__ == '__main__':
    main()
