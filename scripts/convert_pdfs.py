import argparse
import os
import base64
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
try:
    from mistralai import Mistral
except ImportError:
    from mistralai.client import Mistral

ROOT_DIR = Path(__file__).resolve().parent.parent
SANITIZE_SCRIPT = ROOT_DIR / "scripts" / "sanitize_latex.py"


def get_client() -> Mistral:
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise RuntimeError("Set MISTRAL_API_KEY before running this script.")
    return Mistral(api_key=api_key)


def slugify(name: str) -> str:
    return (
        name.lower()
        .replace("á", "a")
        .replace("à", "a")
        .replace("â", "a")
        .replace("ã", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ô", "o")
        .replace("õ", "o")
        .replace("ú", "u")
        .replace("ç", "c")
        .replace(" ", "-")
    )


def build_output_path(pdf_relative_path: str, category: str) -> str:
    pdf_path = Path(pdf_relative_path)
    output_name = f"{slugify(pdf_path.stem)}.md"
    return str(Path("docs") / category / output_name)


def convert_pdf(pdf_relative_path: str, output_relative_path: str, overwrite: bool = False, category: str = "books"):
    client = get_client()
    pdf_path = ROOT_DIR / pdf_relative_path
    output_path = ROOT_DIR / output_relative_path
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.exists() and not overwrite:
        print(f"[SKIP] {output_relative_path} already exists")
        return

    print(f"[CONVERTING] {pdf_relative_path} ...")
    size_mb = pdf_path.stat().st_size / (1024 * 1024)
    print(f"  Size: {size_mb:.1f} MB")

    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    pdf_b64 = base64.standard_b64encode(pdf_bytes).decode("utf-8")

    response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "document_url",
            "document_url": f"data:application/pdf;base64,{pdf_b64}",
        },
        include_image_base64=False,
    )

    pages = response.pages
    print(f"  Pages processed: {len(pages)}")

    content_parts = []
    for page in pages:
        content_parts.append(page.markdown)

    title = output_path.stem.replace("-", " ").title()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    frontmatter = "\n".join(
        [
            "---",
            f'title: "{title}"',
            f'source_pdf: "{pdf_relative_path}"',
            'converter: "mistral-ocr-latest"',
            f'date_converted: "{now}"',
            f'pages: {len(pages)}',
            f'category: "{category}"',
            'sanitized: false',
            'reviewed: false',
            "---",
            "",
        ]
    )
    full_markdown = frontmatter + "\n\n---\n\n".join(content_parts)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_markdown)

    print(f"  [OK] Saved to {output_relative_path}")

    if SANITIZE_SCRIPT.exists():
        print(f"  [SANITIZE] Running sanitize_latex on {output_relative_path} ...")
        result = subprocess.run(
            [sys.executable, str(SANITIZE_SCRIPT), str(output_path.parent)],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print(f"  [SANITIZE OK] {result.stdout.strip().splitlines()[-1] if result.stdout.strip() else 'done'}")
            _update_frontmatter_flag(output_path, "sanitized", "true")
        else:
            print(f"  [SANITIZE WARN] {result.stderr.strip()}")


def _update_frontmatter_flag(path: Path, key: str, value: str):
    text = path.read_text(encoding="utf-8")
    import re
    text = re.sub(rf"^{key}:\s*\S+", f"{key}: {value}", text, count=1, flags=re.MULTILINE)
    path.write_text(text, encoding="utf-8")


def parse_args():
    parser = argparse.ArgumentParser(description="Convert a PDF to markdown with Mistral OCR.")
    parser.add_argument("pdf", help="Path to the source PDF, relative to the project root.")
    parser.add_argument(
        "--category",
        choices=["books", "methodologies"],
        default="books",
        help="Destination docs category.",
    )
    parser.add_argument(
        "--output",
        help="Optional output markdown path relative to the project root.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite output file if it already exists.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    output_relative_path = args.output or build_output_path(args.pdf, args.category)

    try:
        convert_pdf(args.pdf, output_relative_path, overwrite=args.overwrite, category=args.category)
    except Exception as e:
        print(f"[ERROR] {args.pdf}: {e}")
        raise
