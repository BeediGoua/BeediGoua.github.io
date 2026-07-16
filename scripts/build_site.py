import os
import json

# Ensure scripts dir exists just in case
if not os.path.exists("scripts"):
    os.makedirs("scripts")

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} | Project Detail</title>
    <link rel="stylesheet" href="../assets/css/style.css" />
    <link rel="stylesheet" href="../assets/css/animations.css" />
    <link rel="stylesheet" href="../assets/css/expert-cards.css" />
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
<body class="project-detail-page">
    <div class="blob-container">
        <div class="blob blob-1"></div>
        <div class="blob blob-2"></div>
    </div>

    <nav class="back-nav">
        <a href="../index.html" class="btn-expert">
            <i data-feather="arrow-left" style="width: 18px;"></i> Retour au portfolio
        </a>
    </nav>

    <section class="project-detail-hero">
        <div class="project-header-container">
            <h1 class="project-title-xl">{title}</h1>
            <p style="font-size: 1.2rem; color: var(--text-secondary); margin-bottom: 2rem;">{subtitle}</p>
            <div class="tech-badges-top">
                {badges}
            </div>
        </div>
    </section>

    <div class="project-detail-container">
        {content}
    </div>

    <footer style="text-align: center; padding: 2rem; border-top: 1px solid var(--border); margin-top: 3rem;">
        <p style="color: var(--text-secondary);">&copy; 2026 Goua Beedi. Portfolio structuré.</p>
    </footer>

    <script src="https://unpkg.com/feather-icons"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            if (window.feather) {{ feather.replace(); }}
        }});
    </script>
</body>
</html>
"""

def generate_pages():
    try:
        with open("content/portfolio_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Data file not found.")
        return

    # Generate Credit Scoring
    cs_data = data.get("credit_scoring")
    if cs_data:
        html_blocks = []
        for block in cs_data["content"]:
            html_blocks.append(f'''
        <div class="case-study-card reveal-up">
            <h2>{block['title']}</h2>
            {block['body']}
        </div>''')
        
        full_html = TEMPLATE.format(
            title=cs_data["title"],
            subtitle=cs_data["subtitle"],
            badges=cs_data["badges"],
            content="".join(html_blocks)
        )
        
        with open(f"projects/{cs_data['id']}.html", "w", encoding="utf-8") as f:
            f.write(full_html)
            print(f"Generated {cs_data['id']}.html")

if __name__ == "__main__":
    generate_pages()
