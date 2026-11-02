"""Build static portfolio pages from structured content + Jinja2 templates."""
from __future__ import annotations

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_projects() -> dict:
    projects = {}
    for path in sorted((ROOT / "content" / "projects").glob("*.json")):
        data = load_json(path)
        projects[data["id"]] = data
    return projects


def build_homes(env: Environment) -> None:
    profile = load_json(ROOT / "content" / "profile.json")
    experiences = load_json(ROOT / "content" / "experiences.json")["items"]
    projects = load_projects()
    template = env.get_template("home.html")

    pages = [
        {
            "lang": "fr",
            "out": ROOT / "index.html",
            "title": "Goua Beedi | Machine Learning & AI Evaluation",
            "description": "Portfolio Research Editorial de Goua Beedi — statistical ML, évaluation d'IA et études de cas sourcées.",
            "canonical": profile["site"]["fr_home"],
        },
        {
            "lang": "en",
            "out": ROOT / "index-en.html",
            "title": "Goua Beedi | Machine Learning & AI Evaluation",
            "description": "Research Editorial portfolio by Goua Beedi — statistical ML, AI evaluation and sourced case studies.",
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


def build_credit_scoring_legacy() -> None:
    """Keep legacy FR credit-scoring generation until case-study template migration."""
    data_path = ROOT / "content" / "portfolio_data.json"
    if not data_path.exists():
        return
    data = load_json(data_path).get("credit_scoring")
    if not data:
        return

    blocks = []
    for block in data["content"]:
        blocks.append(
            f"""
        <div class=\"case-study-card reveal-up\">
            <h2>{block['title']}</h2>
            {block['body']}
        </div>"""
        )

    html = f"""<!DOCTYPE html>
<html lang=\"fr\">
<head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>{data['title']} | Project Detail</title>
    <link rel=\"stylesheet\" href=\"../assets/css/style.css\" />
    <link rel=\"stylesheet\" href=\"../assets/css/animations.css\" />
    <link rel=\"stylesheet\" href=\"../assets/css/expert-cards.css\" />
    <style>
        .project-detail-hero {{ padding: 6rem 1rem 3rem; background: var(--card-bg-hero); border-bottom: 1px solid var(--border); text-align: center; }}
        .project-title-xl {{ font-size: clamp(2rem, 4vw, 3rem); font-weight: 700; color: var(--text-color); margin-bottom: 1rem; }}
        .project-detail-container {{ max-width: 900px; margin: 0 auto; padding: 2rem 1rem; }}
        .case-study-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 2rem; margin-bottom: 2rem; }}
        .case-study-card h2 {{ font-size: 1.5rem; color: var(--accent-color); margin-bottom: 1rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }}
        .case-study-card h3 {{ font-size: 1.2rem; margin-top: 1.5rem; margin-bottom: 0.5rem; color: var(--text-color); }}
        .case-study-card p, .case-study-card ul {{ margin-bottom: 1rem; color: var(--text-secondary); }}
        .case-study-card ul {{ list-style-type: disc; padding-left: 1.5rem; }}
        .tech-badges-top {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; margin-bottom: 2rem; }}
        .back-nav {{ position: fixed; top: 1rem; left: 1rem; z-index: 1000; }}
        .btn-expert {{ display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px; color: var(--text-color); font-weight: 600; cursor: pointer; text-decoration: none; }}
        .btn-expert:hover {{ border-color: var(--primary-color); }}
        th, td {{ padding: 8px; text-align: left; }}
        th {{ color: var(--text-color); }}
        td {{ color: var(--text-secondary); }}
    </style>
</head>
<body class=\"project-detail-page\">
    <div class=\"blob-container\">
        <div class=\"blob blob-1\"></div>
        <div class=\"blob blob-2\"></div>
    </div>
    <nav class=\"back-nav\">
        <a href=\"../index.html\" class=\"btn-expert\">← Retour au portfolio</a>
    </nav>
    <section class=\"project-detail-hero\">
        <div class=\"project-header-container\">
            <h1 class=\"project-title-xl\">{data['title']}</h1>
            <p style=\"font-size: 1.2rem; color: var(--text-secondary); margin-bottom: 2rem;\">{data['subtitle']}</p>
            <div class=\"tech-badges-top\">{data['badges']}</div>
        </div>
    </section>
    <div class=\"project-detail-container\">{''.join(blocks)}</div>
    <footer style=\"text-align: center; padding: 2rem; border-top: 1px solid var(--border); margin-top: 3rem;\">
        <p style=\"color: var(--text-secondary);\">&copy; 2026 Goua Beedi. Portfolio structuré.</p>
    </footer>
</body>
</html>
"""
    out = ROOT / "projects" / f"{data['id']}.html"
    out.write_text(html, encoding="utf-8", newline="\n")
    print(f"Wrote {out.relative_to(ROOT)} (legacy)")


def main() -> None:
    env = Environment(
        loader=FileSystemLoader(str(ROOT / "templates")),
        autoescape=select_autoescape(["html", "xml"]),
    )
    build_homes(env)
    build_credit_scoring_legacy()


if __name__ == "__main__":
    main()
