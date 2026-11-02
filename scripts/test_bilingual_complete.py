"""Lightweight bilingual structural checks (portable, no Playwright required)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ROOT / "index.html",
    ROOT / "index-en.html",
    ROOT / "projects" / "square-management.html",
    ROOT / "projects" / "square-management-en.html",
    ROOT / "projects" / "reviewguardian.html",
    ROOT / "projects" / "reviewguardian-en.html",
    ROOT / "projects" / "music-recommender.html",
    ROOT / "projects" / "music-recommender-en.html",
    ROOT / "projects" / "zimnat.html",
    ROOT / "projects" / "zimnat-en.html",
]

FORBIDDEN = [
    ("projects/reviewguardian-en.html", ["Isolation Forest", "70%+ Detection", "MongoDB Storage"]),
    ("projects/music-recommender-en.html", ["Precision@10 Score: 0.78", "Serendipity Score: 0.65", "Matrix Factorization (SVD)"]),
    ("projects/zimnat-en.html", ["Zero Commercial Error"]),
]


def main() -> int:
    errors: list[str] = []
    for path in REQUIRED:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")

    fr = (ROOT / "index.html").read_text(encoding="utf-8")
    en = (ROOT / "index-en.html").read_text(encoding="utf-8")
    if 'lang="fr"' not in fr:
        errors.append("index.html missing lang=fr")
    if 'lang="en"' not in en:
        errors.append("index-en.html missing lang=en")
    if "beedigoua.github.io/index-en.html" not in fr:
        errors.append("index.html missing EN hreflang/home link target")
    if fr.count("<h1") != 1 or en.count("<h1") != 1:
        errors.append("home pages must have exactly one h1")

    for rel, needles in FORBIDDEN:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for needle in needles:
            if needle in text:
                errors.append(f"{rel} still contains forbidden claim: {needle}")

    if errors:
        print("FAIL")
        for err in errors:
            print(" -", err)
        return 1

    print("OK: bilingual structure and P0 claim checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
