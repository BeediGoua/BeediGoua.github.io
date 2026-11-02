# Portfolio — Goua Beedi

Site statique GitHub Pages : portfolio **Research Editorial** (Data Science / Statistical ML / AI Evaluation).

**Live :** [https://beedigoua.github.io/](https://beedigoua.github.io/) · [English](https://beedigoua.github.io/index-en.html)

## Stack

- HTML / CSS / JS natifs (pas de React / Next / Tailwind en production)
- Génération optionnelle Python + Jinja2 (`scripts/build_site.py`)
- Hébergement GitHub Pages (`.nojekyll` conservé)

## Développement local

```bash
git clone https://github.com/BeediGoua/BeediGoua.github.io.git
cd BeediGoua.github.io
python -m http.server 8000
```

Ouvrir `http://localhost:8000/`.

### Build depuis le contenu structuré

```bash
pip install -r requirements-dev.txt
python scripts/validate_content.py
python scripts/build_site.py
python scripts/check_site.py
```

Sources : `content/profile.json`, `content/experiences.json`, `content/projects/*.json`, `content/evidence-register.json`, `content/source-of-truth.md`.

## Structure utile

```
index.html / index-en.html   # Accueils FR / EN (générés)
projects/                    # Études de cas (URLs historiques conservées)
assets/css/tokens.css …      # Design system Research Editorial
content/                     # Source de vérité structurée
templates/                   # Jinja2
docs/refonte/                # Cahier des charges + PROGRESS.md
```

## Contact

- LinkedIn : [goua-beedi-henri](https://www.linkedin.com/in/goua-beedi-henri-a152bb1b2/)
- GitHub : [BeediGoua](https://github.com/BeediGoua)
- Email : gouabeedi@gmail.com
- CV : `assets/CV_GouaHenri_FR.pdf` · `assets/CV_GouaHenri_EN.pdf`
