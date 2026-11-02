"""Check FR/EN static language switching links exist on key pages."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHECKS = [
    ("index.html", "index-en.html"),
    ("index-en.html", "index.html"),
    ("projects/credit-scoring.html", "credit-scoring-en.html"),
    ("projects/square-management.html", "square-management-en.html"),
]


def main() -> int:
    errors: list[str] = []
    for page, target in CHECKS:
        path = ROOT / page
        text = path.read_text(encoding="utf-8")
        if target not in text:
            errors.append(f"{page}: missing link to {target}")
    if errors:
        print("FAIL")
        for err in errors:
            print(" -", err)
        return 1
    print("OK: static FR/EN language links present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
