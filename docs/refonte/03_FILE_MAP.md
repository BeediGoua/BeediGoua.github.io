# 03 — Fichiers existants → changements attendus

**Inventaire vérifié dans `main` au 1er novembre 2026.** Ce document ne présume pas que des changements ultérieurs n'ont pas eu lieu. Toujours re-scanner le dépôt avant édition. **Migrer sans supprimer avant contrôle de tous les usages.**

## A. Pages d'accueil

| Fichier réel | Intervention exacte | Critères de sortie |
|---|---|---|
| `index.html` | Refondre hero, projets remontés après hero, expérience en lignes, méthode basée sur preuves, formation simplifiée, skills rationalisées, footer ; conserver ancres et liens | 1 `h1`, CTA `#projects`, CV FR, nav et mobile OK, pas de section vide |
| `index-en.html` | Même structure **strictement parallèle**, mêmes travaux et données, texte EN naturel | CV EN, metas EN, même ordre et métriques, canonical EN |

**Structure actuelle vérifiée :** `hero`, `approach`, `education`, `experience`, `projects`, `skills`, `contact`. Les deux accueils chargent actuellement 9 CSS et six scripts externes/locaux (dont Feather CDN). Réorganiser **une fois le nouveau DOM et les ancres testés** ; `#approach` peut devenir alias de la nouvelle section `#method`.

## B. Pages projets existantes, chacune à migrer

| Chemin réel | Travail de contenu + visuel |
|---|---|
| `projects/square-management.html` | Premier « case study » premium : question scientifique, 189 configurations RAG, facteurs réellement testés, protocole, diagramme, résultats publics permis, limites/confidentialité ; FR et EN équivalents |
| `projects/credit-scoring.html` | Transformer le vieux rendu généré FR-only : même navigation, EN généré, tableau AUC sourcé, bilan des effectifs, méthodes de split, limites de calibration, pas de faux ROC |
| `projects/brokerflow.html` | Architecture réelle modèle/règles/agents/fallback, benchmark 50 cas, seuil/metrics sourcés, tests, décisions et limites explicites |
| `projects/retail-demand-forecasting.html` | ADI/CV², horizon 8 semaines si sourcé, baselines et séparation temporelle, distribution/quantiles & Newsvendor, WAPE 8% exclu jusqu'à validation |
| `projects/analyse-survie.html` | Définition censure/événement, KM/Cox seulement comme méthodes effectivement utilisées ; résultats et graphiques uniquement sourcés et publics |
| `projects/finzuu.html` | Rôle, architecture métier, sources, hypothèses, scoring explicable, contrôle humain, statut non-production clairement déclaré |
| `projects/ville-de-paris.html` | Sources LAPI/SIV/SIREN, jointures et contrôles, limites confidentialité, représentation *conceptuelle* du pipeline, pas de chiffres inventés |
| `projects/reviewguardian.html` | **P0** : remplacer entièrement le contenu EN contradictoire (bots/graphe/fraude) par traduction fidèle du vrai projet de modération de toxicité ; audit du dépôt source |
| `projects/music-recommender.html` | **P0** : remplacer contenu EN SVD/precision/serendipity/latence inventoriés par méthode effectivement implémentée et évaluée ; contrôler README source |
| `projects/zimnat.html` | **P0** : enlever claims absolues `Zero Commercial Error`, `100%`, production non établie, préciser règle d'exclusion vs performance statistique |
| `projects/autres-projets.html` | Index de tous les travaux non mis en avant : liste claire, statut, domaine, résumé, vrais liens, locale harmonisée |

**Important :** ne pas renommer/supprimer les 11 URLs FR. Si des variantes `*-en.html` sont ajoutées, ne pas transformer automatiquement les anciennes URLs en EN ; conserver des liens directs et canonicals cohérents. Les pages historiques avec `?lang=en` doivent rester utilisables pendant la période de migration, sans contenu EN erroné.

## C. CSS — fichiers exacts présents

| Existant | Action de migration / destination |
|---|---|
| `assets/css/style.css` | Décomposer reset, tokens historiques, grille et composants vers `tokens.css`, `base.css`, `layout.css`, `components.css`, `home.css` et `case-study.css`. Audit des spécificités avant élimination |
| `assets/css/animations.css` | Garder animations nécessaires dans `motion.css`, avec reduced-motion |
| `assets/css/content-refinement.css` | Migrer styles éditoriaux réellement utilisés vers `components.css`/`case-study.css` |
| `assets/css/detail-polish.css` | Fusionner en `case-study.css` après tests de toutes les pages |
| `assets/css/editorial-data-theme.css` | Reprendre l'intention sobre; intégrer les choix de palette/typographie dans les tokens et composants, pas en overlay |
| `assets/css/experience-detail.css` | Conserver styles réellement nécessaires aux expériences dans `case-study.css` |
| `assets/css/expert-cards.css` | Unifier cartes projets & métriques dans `components.css` |
| `assets/css/global-language.css` | Supprimer uniquement une fois les liens de locale statiques partout |
| `assets/css/homepage-polish.css` | Migrer le layout d'accueil utile dans `home.css`; retirer les correctifs |
| `assets/css/project-case-study.css` | Fusionner avec `case-study.css` |
| `assets/css/project-detail.css` | Fusionner avec `case-study.css` |
| `assets/css/responsive-final.css` | Refaire les breakpoints cohérents dans `responsive.css`; éliminer causes de débordement plutôt que `overflow-x:clip` uniquement |
| `assets/css/unified-icons-metrics.css` | Migrer les composants réellement référencés (sinon retirer) |
| `assets/css/visual-system-v3.css` | Reprendre les composants retenus, retirer gradients/glows et collisions |
| `style.css` (à la racine) | Vérifier s'il est référencé; garder temporairement si utile, retirer seulement après audit |

**Objectif :** 8 fichiers finaux pertinents, pas 8 couches additionnelles. `!important` uniquement pour exception justifiée, jamais comme stratégie principale. Tester les 11 pages projets ainsi que 2 accueils, surtout styles historiques chargés différemment.

## D. JavaScript — fichiers exacts présents

| Existant | Action prévue |
|---|---|
| `assets/js/script.js` | Identifier nav, thème, scroll, écouteurs et code mort ; scinder en `main.js`, `navigation.js`, `theme.js` seulement si cela simplifie réellement |
| `assets/js/animations.js` | Réduire/retirer les animations décoratives, maintenir contenu visible sans JS |
| `assets/js/education-accordion.js` | Préférer `details/summary` si pertinent et accessible, sinon garder un accordéon testé |
| `assets/js/experience-detail.js` | Migrer interactions communes de case study dans `case-study.js` |
| `assets/js/project-case-study.js` | Migrer interactions nécessaires ; attention aux pages FR/EN |
| `assets/js/project-script.js` | Auditer pages qui le chargent, retirer seulement quand remplacé |
| `assets/js/legacy-project-detail.js` | Auditer éléments utilisés ; supprimer code mort après tests |
| `assets/js/global-language.js` | Remplacer les mutations/reloads par liens FR/EN natifs ; garder temporairement compatibilité ancien `?lang=` |
| `assets/js/i18n-dictionaries.js` | Fusionner faits et traductions dans données structurées, après contrôle des divergences |
| `assets/lang/fr.json`, `assets/lang/en.json` | Auditer couverture et doublons ; ne pas supprimer tant qu'une page les utilise |

## E. Contenu, scripts, docs

| Existant | Travail |
|---|---|
| `content/source-of-truth.md` | Conserver/compléter. Prioritaire sur toute phrase marketing générée |
| `content/portfolio_data.json` | Source actuelle pour Credit Scoring ; **ne pas la casser avant remplacement du générateur** |
| `scripts/build_site.py` | Génère actuellement Credit Scoring en FR ; remplacer graduellement par génération statique commune depuis `templates/` + contenus FR/EN ; build déterministe et chemins portables |
| `scripts/check_site.py` | Étendre à toutes les pages, assets, ancres, documents localisés, IDs et erreurs, plus tests externes séparés |
| `scripts/test_bilingual_complete.py` | Corriger chemin absolu d'environnement, traductions et vérification de faits |
| `scripts/test_experience_pages.py` | Adapter au DOM de la refonte, pas supprimer le contrôle |
| `scripts/test_global_language.py` | Remplacer/adapter selon modèle final FR/EN |
| `README.md` | Corriger mauvais lien live, ancien repo clone `BeediGoua-portfolio.git`, stack/polices, faux formulaire FormSubmit, scripts de build et tests |
| `requirements.txt` | Actuellement pas de dépendances déclarées ; distinguer runtime statique et `requirements-dev.txt` (Jinja2, pytest, Playwright si utilisés) |
| `.gitignore` | S'assurer que caches Python, captures temporaires, .venv, .pytest_cache ne sont pas versionnés ; garder les HTML statiques publiés |
| `.nojekyll` | Conserver pour publication GitHub Pages si nécessaire |
| `docs/QA_*.md` | Conserver comme historique, créer rapport **courant** `docs/refonte/PROGRESS.md` et QA final, ne pas croire les anciens audits comme preuve actuelle |
| `.vscode/settings.json` | Éviter d'écraser les préférences locales |

## F. Assets existants / nouvelles cibles

- CVs exacts : `assets/CV_GouaHenri_FR.pdf`, `assets/CV_GouaHenri_EN.pdf`. Tester ouverture et existence, ne pas renommer.
- Portraits existants : `assets/img/goua.png`, `.jpg`, `.webp`, `goua1.jpg` ; usage du hero actuel : `goua.png`. Comparer fichiers/poids/qualité et conserver variante préférée + fallback avant nettoyage.
- Logos actuels `assets/img/brands/` : `FINZUU.png`, `MS2A.png`, `SQUARE1.png`, `ensai.png`, `goua_beedi_icon_dark.png`, `goua_beedi_icon_light.png`, `sorbonne.png`, `square.png`, `ville_paris.png`, `ville_paris1.png`. Ne pas supprimer sur simple similarité de nom ; usages/a11y à vérifier.
- Favicon et Apple touch icon existent : améliorer seulement si incohérents.
- Ajouter images de projets à `assets/img/projects/` uniquement depuis des données réelles ou schémas *conceptuels* explicitement indiqués ; ajouter image OG si droits vérifiés.

## G. Fichiers à créer après validation de phase

`templates/base.html`, `templates/home.html`, `templates/case-study.html`, `templates/partials/*`, `content/profile.json`, `content/experiences.json`, `content/projects/*.json`, `content/evidence-register.json`, `assets/css/tokens.css`, `base.css`, `layout.css`, `components.css`, `home.css`, `case-study.css`, `responsive.css`, `motion.css`, `assets/js/main.js`, `navigation.js`, `theme.js`, `case-study.js`, `scripts/validate_content.py`, `tests/*`, `.github/workflows/ci.yml`, `404.html`, `sitemap.xml`, `robots.txt`, `docs/DESIGN_SYSTEM.md`, `docs/CONTENT_POLICY.md`.

Ne pas tout créer immédiatement ; construire uniquement ce qui est utilisé par le lot actif. Mettre à jour références de fichiers, packaging et générateur dans la même étape, et vérifier un build propre avant la suppression des fichiers historiques.
