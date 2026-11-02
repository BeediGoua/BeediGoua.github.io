"""Build static portfolio pages from structured content + Jinja2 templates."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from case_study_data import pages as case_pages  # noqa: E402


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_projects() -> dict:
    projects = {}
    for path in sorted((ROOT / "content" / "projects").glob("*.json")):
        data = load_json(path)
        projects[data["id"]] = data
    return projects


def env() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(ROOT / "templates")),
        autoescape=select_autoescape(["html", "xml"]),
    )


def build_homes(jinja: Environment) -> None:
    profile = load_json(ROOT / "content" / "profile.json")
    experiences = load_json(ROOT / "content" / "experiences.json")["items"]
    projects = load_projects()
    template = jinja.get_template("home.html")

    pages = [
        {
            "lang": "fr",
            "out": ROOT / "index.html",
            "title": "Goua Beedi | Data Scientist",
            "description": "Portfolio de Goua Beedi, Data Scientist : scoring crédit, évaluation de systèmes RAG, données multi-sources et statistiques appliquées.",
            "canonical": profile["site"]["fr_home"],
        },
        {
            "lang": "en",
            "out": ROOT / "index-en.html",
            "title": "Goua Beedi | Data Scientist",
            "description": "Portfolio of Goua Beedi, Data Scientist: credit scoring, RAG system evaluation, multi-source data and applied statistics.",
            "canonical": profile["site"]["en_home"],
        },
    ]

    for page in pages:
        html = template.render(
            lang=page["lang"],
            title=page["title"],
            description=page["description"],
            canonical=page["canonical"],
            profile=profile,
            t=profile["text"][page["lang"]],
            experiences=experiences,
            projects=projects,
        )
        page["out"].write_text(html, encoding="utf-8", newline="\n")
        print(f"Wrote {page['out'].relative_to(ROOT)}")


def build_case_studies(jinja: Environment) -> None:
    template = jinja.get_template("case-study.html")
    for item in case_pages():
        for lang, out_key, canon_key, alt_fr, alt_en in (
            ("fr", "out_fr", "canonical_fr", item["canonical_fr"], item["canonical_en"]),
            ("en", "out_en", "canonical_en", item["canonical_fr"], item["canonical_en"]),
        ):
            payload = item[lang]
            out = ROOT / item[out_key]
            html = template.render(
                lang=lang,
                title=payload["title"],
                description=payload["description"],
                canonical=item[canon_key],
                alternate_fr=alt_fr,
                alternate_en=alt_en,
                home_url="../index.html" if lang == "fr" else "../index-en.html",
                lang_switch_href=Path(item["out_en" if lang == "fr" else "out_fr"]).name,
                back_href=payload["back"],
                kicker=payload["kicker"],
                heading=payload["heading"],
                subtitle=payload["subtitle"],
                meta=payload.get("meta") or [],
                links=payload.get("links") or [],
                sections=payload.get("sections") or [],
                limitations=payload.get("limitations") or "",
            )
            out.write_text(html, encoding="utf-8", newline="\n")
            print(f"Wrote {out.relative_to(ROOT)}")


def write_sitemap() -> None:
    urls = [
        "https://beedigoua.github.io/",
        "https://beedigoua.github.io/index-en.html",
    ]
    for item in case_pages():
        urls.append(item["canonical_fr"])
        urls.append(item["canonical_en"])
    body = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        body.append(f"  <url><loc>{url}</loc></url>")
    body.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(body) + "\n", encoding="utf-8", newline="\n")
    print("Wrote sitemap.xml")


def main() -> None:
    jinja = env()
    build_homes(jinja)
    build_case_studies(jinja)
    write_sitemap()


if __name__ == "__main__":
    main()
