# 09 — Inventaire initial du dépôt, vérifié via GitHub

Date de référence : **2026-11-01**. GitHub `main` lors de l'inspection : commit `98c2e8b2eee48c5a8a0ab14594e4d764d40dadde`. **Re-vérifier localement avant tout changement**, car la branche peut avoir avancé.

## Entrées du dépôt

- Entrées HTML racine : `index.html`, `index-en.html`.
- Pages `projects/` : `analyse-survie.html`, `autres-projets.html`, `brokerflow.html`, `credit-scoring.html`, `finzuu.html`, `music-recommender.html`, `retail-demand-forecasting.html`, `reviewguardian.html`, `square-management.html`, `ville-de-paris.html`, `zimnat.html`.
- 14 fichiers dans `assets/css/` + `style.css` racine. Les pages d'accueil chargent simultanément neuf CSS : `style.css`, `animations.css`, `expert-cards.css`, `content-refinement.css`, `homepage-polish.css`, `global-language.css`, `visual-system-v3.css`, `responsive-final.css`, `editorial-data-theme.css` (tous sous `assets/css`).
- Neuf JavaScript dans `assets/js/` : `animations.js`, `education-accordion.js`, `experience-detail.js`, `global-language.js`, `i18n-dictionaries.js`, `legacy-project-detail.js`, `project-case-study.js`, `project-script.js`, `script.js`.
- CV locaux : `assets/CV_GouaHenri_FR.pdf`, `assets/CV_GouaHenri_EN.pdf`.
- Contenus : `content/source-of-truth.md`, `content/portfolio_data.json`.
- Scripts : `scripts/build_site.py`, `scripts/check_site.py`, `scripts/test_bilingual_complete.py`, `scripts/test_experience_pages.py`, `scripts/test_global_language.py`.
- README courant : mauvais lien Markdown vers la démo, mauvais repo de clonage, contact FormSubmit mentionné alors que l'accueil affiche un mailto, descriptions des polices obsolètes.
- Générateur courant : `build_site.py` ne produit essentiellement que Credit Scoring FR à partir de `portfolio_data.json`. La page Credit Scoring contient des styles inline et un titre `| Project Detail`.
- `global-language.js` combine langage stocké, paramètres URL, mutation DOM et réécriture de liens. Les pages de projets ont souvent des blocs `data-lang`, créant une seconde logique.
- Les pages EN ReviewGuardian / Music Recommender et Zimnat contiennent des descriptions/impacts non fiables ou contradictoires avec FR.
- Baseline d'ancres sur l'accueil : `hero`, `approach`, `education`, `experience`, `projects`, `skills`, `contact`.
- Les pages d'accueil comportent des métadonnées SEO ; la page EN utilise le même canonical que FR au moment de l'inspection.
- Le fichier `requirements.txt` indique qu'aucune dépendance Python n'est nécessaire, cohérent avec le site statique actuel.
- Aucun `.github/workflows/` présent dans l'arborescence inspectée.

## Ce qui n'a PAS été démontré par cet inventaire

Aucune capture visuelle du site publié, aucun Lighthouse, aucun audit axe, aucune preuve de performance ou de comportement mobile n'ont été réalisés lors de cette inspection par API. Cursor doit vérifier ces points dans un vrai navigateur avant d'affirmer une amélioration.

## Point de vigilance technique

Les audits précédents ont compté 1 172 occurrences de `!important` dans les feuilles `assets/css/`, valeur indicative de dette CSS **sur cet état du dépôt**. Ce n'est pas un score de qualité absolu ni une mesure de poids transféré. Réduire la dette en supprimant les conflits, pas en supprimant arbitrairement toutes les occurrences.

## Sources de référence dans le repo

- `content/source-of-truth.md` : règles de publication, limites et statistiques déclarées.
- `content/portfolio_data.json` : contenu Credit Scoring actuel, y compris chiffres et protocole narratif qui nécessitent revue scientifique.
- `README.md` : à corriger, ne pas considérer comme source unique de vérité.
