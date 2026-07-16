from pathlib import Path
from html.parser import HTMLParser
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
EXPECTED = {
    "projects/square-management.html": ["Vue d’ensemble", "Workflow technique", "Résultats et livrables"],
    "projects/ville-de-paris.html": ["Vue d’ensemble", "Workflow technique", "Résultats et livrables"],
    "projects/finzuu.html": ["Vue d’ensemble", "Workflow technique", "Résultats et livrables"],
}

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            data = dict(attrs)
            if data.get("href"):
                self.hrefs.append(data["href"])

errors = []
index_text = INDEX.read_text(encoding="utf-8")
parser = Links()
parser.feed(index_text)

for relative, markers in EXPECTED.items():
    if relative not in parser.hrefs:
        errors.append(f"Missing experience button in index.html: {relative}")
    page = ROOT / relative
    if not page.exists():
        errors.append(f"Missing page: {relative}")
        continue
    text = page.read_text(encoding="utf-8")
    if "experience-detail.css" not in text or "experience-detail.js" not in text:
        errors.append(f"Missing experience assets in {relative}")
    for marker in markers:
        if marker not in text:
            errors.append(f"Missing content '{marker}' in {relative}")

css = (ROOT / "assets/css/experience-detail.css").read_text(encoding="utf-8")
if ".project-detail-page .reveal-up" not in css or "opacity: 1" not in css:
    errors.append("Missing no-animation visibility fallback")

if errors:
    print("FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("OK: experience buttons, pages, detailed content, assets and visibility fallback verified")
