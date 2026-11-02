"""Smoke tests for migrated experience / case-study pages."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    "projects/square-management.html",
    "projects/finzuu.html",
    "projects/ville-de-paris.html",
    "projects/credit-scoring.html",
    "projects/brokerflow.html",
]


def main() -> int:
    errors: list[str] = []
    for rel in PAGES:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if 'href="../assets/css/case-study.css"' not in text and "case-study.css" not in text:
            errors.append(f"{rel}: case-study.css not linked")
        if "<h1" not in text:
            errors.append(f"{rel}: missing h1")
        if "Limites" not in text and "Limitations" not in text:
            # autres index may not have limitations; these pages should
            if "autres-projets" not in rel:
                errors.append(f"{rel}: missing limitations section")

    css = ROOT / "assets/css/case-study.css"
    if not css.exists():
        errors.append("missing assets/css/case-study.css")

    if errors:
        print("FAIL")
        for err in errors:
            print(" -", err)
        return 1

    print("OK: experience/case-study pages, detailed content, assets verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
