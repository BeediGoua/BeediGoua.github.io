# 05 — Architecture cible : simple, statique, bilingue, reproductible

## Décision

Maintenir GitHub Pages et du HTML/CSS/JS **généré statiquement**. Pas de React/Next/Tailwind par défaut. Utiliser Python + Jinja2 au moment du build si cela supprime réellement la duplication ; les pages générées restent commitées dans le dépôt et peuvent être servies sans Python par GitHub Pages. Évaluer si quelques composants partagés et scripts Python de génération suffisent avant de multiplier les abstractions.

## Structure cible indicative

```text
index.html                 # FR, canonique / ; conservé
index-en.html              # EN ; conservé
projects/                 # Les 11 URLs historiques sont conservées
  credit-scoring.html      # FR ; conservé
  credit-scoring-en.html   # EN ; à générer après migration
  ...-en.html              # Idem pour toutes les études de cas, si nécessaire
content/
  source-of-truth.md       # GARDE-FOU EXISTANT
  portfolio_data.json     # SOURCE LEGACY À MIGRER, PAS À EFFACER TÔT
  profile.json
  experiences.json
  projects/*.json
  evidence-register.json
templates/
  base.html
  home.html
  case-study.html
  partials/header.html
  partials/footer.html
  partials/project-card.html
assets/css/
  tokens.css
  base.css
  layout.css
  components.css
  home.css
  case-study.css
  responsive.css
  motion.css
assets/js/
  main.js
  navigation.js
  theme.js
  case-study.js
scripts/
  build_site.py
  validate_content.py
  check_site.py
tests/
  test_content.py
  test_links.py
  test_i18n.py
  test_navigation.py
  test_responsive.py
.github/workflows/ci.yml
README.md
requirements-dev.txt
.nojekyll
```

**Ce n'est pas une liste de fichiers à créer immédiatement** : elle fixe la destination de migration. Un fichier supprimable seulement lorsqu'il n'est référencé par aucun HTML/script et que les tests ont été exécutés.

## Système de contenu

### 1. Identité personnelle

`profile.json` pourrait porter `name`, `headline.fr/en`, `intro.fr/en`, `availability.fr/en`, `cv.fr/en`, `github`, `linkedin`, `email`, `education[]`. Ne jamais laisser l'agent remplir les champs de faits non présents dans source de vérité à partir d'une inférence.

### 2. Projets

`content/projects/<slug>.json` :

```json
{
  "id": "square-management",
  "category": "RAG / Evaluation",
  "featured_rank": 1,
  "public_url_fr": "/projects/square-management.html",
  "public_url_en": "/projects/square-management-en.html",
  "text": {
    "fr": {"title": "Évaluation de systèmes RAG", "question": "...", "methods": "...", "limitations": "..."},
    "en": {"title": "RAG System Evaluation", "question": "...", "methods": "...", "limitations": "..."}
  },
  "claim_ids": ["square_189_configs"]
}
```

Valeurs `...` = exemple de **schéma**, pas contenu à publier. Validator doit refuser les champs requis manquants. `public_url_en` doit être générée et testée avant insertion dans la navigation.

### 3. Métriques

`evidence-register.json`: toute valeur expérimentale affichée est reliée à `id`, `source_ref`, `protocol_ref`, `status`, `public_allowed`, éventuellement `display_value` et `sample_context`. Une valeur sans source ne doit pas être incluse dans le rendu public. Si les données sont confidentielles, afficher une conclusion qualitative autorisée plutôt que la donnée.

## Build recommandé

1. `scripts/validate_content.py` : schéma, clés FR/EN, URLs uniques, champs manquants, correspondance claims à evidence register, claims publiables.
2. `scripts/build_site.py` : résolution `ROOT = Path(__file__).resolve().parents[1]`, chargement JSON, construction contexte puis rendu Jinja2.
3. Écrire `index.html`, `index-en.html`, projets FR et EN ; conserver les anciennes URLs. Le HTML doit être stable au second build (idempotence).
4. `scripts/check_site.py` : tous les liens et ancres, assets, page metadata, `hreflang`, IDs, CV, éventuellement exclusions de fichiers temporaires.
5. Tests navigateur + captures.
6. CI construit, teste puis vérifie que les fichiers générés sont cohérents avec le dépôt : si on commit le HTML, `git diff --exit-code -- index.html index-en.html projects` après build peut aider, mais seulement si le générateur est déterministe.

**Sémantique** : `Jinja2` ne tourne pas dans GitHub Pages ; installation et génération faites localement ou dans CI avant publication. Les noms de templates et schémas peuvent être adaptés pour réduire la complexité si Cursor justifie la décision dans `PROGRESS.md`.

## Migration du bilinguisme, sans casser les URLs

**Actuellement** : `index.html` et `index-en.html` coexistent avec `assets/lang/fr.json`, `assets/lang/en.json`, `assets/js/global-language.js`, `assets/js/i18n-dictionaries.js`, et des blocs internes `data-lang` sur les projets. Il existe donc plusieurs sources concurrentes de texte.

**Cible** : pages statiques distinctes qui s'échangent par vrais liens dans l'en-tête, avec une source `text.fr/en` partagée par projet. FR/EN doivent présenter les mêmes métriques, algorithmes et conclusions. À la bascule, conserver la même page de projet quand une variante EN existe ; sinon montrer un lien valide vers l'index EN, sans inventer une traduction. Gérer les liens anciens `?lang=fr/en` temporairement si besoin.

En-tête de **chaque** page :

- `<html lang="fr">` ou `en` conformément au contenu réellement visible.
- `<title>` et description spécifiques et localisés.
- `canonical` vers l'URL canonique de la page (pas la même URL pour FR et EN).
- deux `alternate hreflang=fr/en` réciproques si les deux versions existent.
- Open Graph correspondant à la page/langue et image vérifiée.
- navigations internes et CV correspondants.

Exemples canonicals : FR home `https://beedigoua.github.io/`, EN home `https://beedigoua.github.io/index-en.html`; FR Credit `https://beedigoua.github.io/projects/credit-scoring.html`, EN Credit `https://beedigoua.github.io/projects/credit-scoring-en.html` si la page EN existe réellement.

## Navigation et gestion des thèmes

Préférer de vrais liens sans JS et une navigation mobile accessible. Un seul mécanisme de thème `data-theme` ou classe racine, tokens complets par thème, `localStorage` gardé dans `try/catch`, fallback `prefers-color-scheme` seulement si décision UX, pas de flash initial. **Pas de faux bouton.**

## Organisation CSS

`tokens` → `base` → `layout` → `components` → `home/case-study` → `responsive` → `motion`. Éviter l'importation multiple d'un même fichier et remplacer les spécificités excessives par classes de composants. Protéger le CSS existant pendant migration. Limiter la création de fichiers aux besoins réels.

## CI et déploiement

Conserver la source GitHub Pages actuelle jusqu'à vérification du pipeline. Tester d'abord dans une branche/PR. Ne pas remplacer immédiatement la configuration Pages par une GitHub Action si elle publie déjà les HTML de `main`. Une fois tous les contrôles validés, choisir explicitement un flux : publication depuis branche ou déploiement GitHub Actions. Dans les deux cas, conserver `.nojekyll` si la configuration l'exige.
