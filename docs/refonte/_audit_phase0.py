"""Phase 0 audit helper — read-only. Run from repo root."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def links(html: str, attr: str, ext: str) -> list[str]:
    return re.findall(rf'{attr}=["\']([^"\']+\.{ext})["\']', html, flags=re.I)


def main() -> None:
    print("ROOT", ROOT)
    print("=== HOME PAGES ===")
    for page in ["index.html", "index-en.html"]:
        p = ROOT / page
        t = p.read_text(encoding="utf-8", errors="replace")
        lang = re.search(r'<html[^>]*lang=["\']([^"\']+)', t)
        h1 = len(re.findall(r"<h1\b", t, flags=re.I))
        canon = re.search(
            r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)|href=["\']([^"\']+)["\'][^>]*rel=["\']canonical',
            t,
            flags=re.I,
        )
        ids = re.findall(r'id=["\']([^"\']+)["\']', t)
        section_ids = [i for i in ids if i in {
            "hero", "approach", "method", "education", "experience",
            "projects", "skills", "contact", "main", "main-content",
        }]
        print(f"\n{page}")
        print("  lang:", lang.group(1) if lang else None)
        print("  h1:", h1)
        print("  canonical:", (canon.group(1) or canon.group(2)) if canon else None)
        print("  css:", links(t, "href", "css"))
        print("  js:", links(t, "src", "js"))
        print("  section_ids:", section_ids)
        for needle in ["CV_GouaHenri", "mailto:", "github.com", "linkedin", "feather"]:
            print(f"  has[{needle}]:", needle.lower() in t.lower() or needle in t)

    print("\n=== PROJECTS CSS/JS LOAD ===")
    for p in sorted((ROOT / "projects").glob("*.html")):
        t = p.read_text(encoding="utf-8", errors="replace")
        print(p.name, "css=", len(links(t, "href", "css")), "js=", len(links(t, "src", "js")),
              "data-lang=", t.count("data-lang="), "bytes=", p.stat().st_size)

    print("\n=== ASSETS EXISTENCE ===")
    for rel in [
        "assets/CV_GouaHenri_FR.pdf",
        "assets/CV_GouaHenri_EN.pdf",
        "assets/img/goua.png",
        "assets/img/goua.jpg",
        "assets/img/goua.webp",
        "style.css",
        "content/source-of-truth.md",
        "content/portfolio_data.json",
        ".nojekyll",
        ".github/workflows",
    ]:
        path = ROOT / rel
        print(f"  {rel}: {'OK' if path.exists() else 'MISSING'}",
              f"({path.stat().st_size if path.is_file() else 'dir' if path.exists() else '-'})")

    css_files = list((ROOT / "assets/css").glob("*.css"))
    important = 0
    for f in css_files:
        important += f.read_text(encoding="utf-8", errors="replace").count("!important")
    print(f"\nCSS files: {len(css_files)} + root style.css={ (ROOT/'style.css').exists() }")
    print(f"!important count: {important}")
    print(f"JS files: {len(list((ROOT/'assets/js').glob('*.js')))}")

    # Key claim probes
    print("\n=== CLAIM PROBES ===")
    probes = {
        "reviewguardian.html": ["toxic", "bot", "Isolation Forest", "7 296", "7296", "70%"],
        "music-recommender.html": ["Word2Vec", "SVD", "Precision@10", "0.78", "Serendipity"],
        "zimnat.html": ["Zero Commercial", "100%", "CatBoost", "Bayesian", "Production"],
        "credit-scoring.html": ["0.784", "0,784", "532", "calibr"],
        "brokerflow.html": ["0.728", "50", "Brier", "0.231"],
        "retail-demand-forecasting.html": ["WAPE", "8%", "Newsvendor", "Favorita"],
        "square-management.html": ["189"],
    }
    for name, keys in probes.items():
        t = (ROOT / "projects" / name).read_text(encoding="utf-8", errors="replace")
        hits = {k: t.lower().count(k.lower()) for k in keys}
        print(name, hits)

    # README issues
    readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
    print("\n=== README FLAGS ===")
    for k in ["FormSubmit", "BeediGoua-portfolio", "beedigoua.github.io", "Inter", "Poppins"]:
        print(f"  {k}:", k in readme)


if __name__ == "__main__":
    main()
