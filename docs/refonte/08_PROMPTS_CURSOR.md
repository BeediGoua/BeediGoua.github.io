# 08 — Prompts prêts à copier dans Cursor (un à la fois)

**Mode d'emploi :** la première fois, ouvrir le dépôt et installer tout le kit (`AGENTS.md`, `.cursor/rules`, `docs/refonte`) au bon endroit. Sélectionner **Plan** dans Cursor pour la phase 0, puis **Agent** pour les phases validées. Ne pas demander l'implémentation des phases 0 à 8 dans une seule conversation. Pour une nouvelle session, demander d'abord la lecture de `PROGRESS.md`.

## PROMPT PHASE 0 — COPIER EN PREMIER

```text
Tu travailles sur mon dépôt BeediGoua/BeediGoua.github.io. Tu dois préparer sa refonte Research Editorial. Lis AGENTS.md et tous les fichiers docs/refonte/00_*.md à 09_*.md pertinents, puis ouvre docs/refonte/REFERENCE.html dans le navigateur. Prends docs/refonte/09_REPO_BASELINE.md comme un instantané historique, et confirme la structure réelle de MON checkout.

D'abord vérifie git status, branche courante, fichiers modifiés et configuration GitHub Pages. Ne modifie jamais main et ne détruis aucun travail existant. Si je ne suis pas sur une branche dédiée, crée ou propose la branche refonte-research-portfolio. Inspections obligatoires :
(1) inventaire des 2 accueils, 11 pages projets, 14 CSS assets + style.css racine et 9 JS ; dépendances et code mort ;
(2) contradictions FR/EN, méthodes/métriques, preuves réellement disponibles dans les dépôts de projets et content/source-of-truth.md ;
(3) ordre des sections et liens/ancres, navigation, CV ;
(4) captures navigateur à 360/390/768/1024/1440/1920 et console si disponible ;
(5) score Lighthouse réel si disponible, sinon NOT_RUN ;
(6) état des tests existants, SEO/hreflang, accessibilité.

Ne modifie AUCUN fichier de production pendant cette phase. Renseigne docs/refonte/PROGRESS.md avec une baseline honnête : constats vérifiés, risques, captures, commandes réellement lancées, erreurs et propositions de lots précis. Produit un plan avec critères de sortie et diff minimal pour la phase 1. Arrête-toi à l'audit. Ne réalise pas les phases suivantes sans mon feu vert.
```

## PROMPT PHASE 1 — FIABILITÉ SCIENTIFIQUE

```text
Reprends docs/refonte/PROGRESS.md et les règles du kit. Exécute UNIQUEMENT la phase 1 du plan : réconcilier ReviewGuardian, Music Recommender et Zimnat FR/EN avec la réalité des dépôts sources, supprimer les claims/métriques contradictoires ou sans preuve, et auditer Credit Scoring, BrokerFlow et Retail conformément à docs/refonte/04_SCIENTIFIC_TRUTH.md. Respecte content/source-of-truth.md et toutes restrictions de confidentialité. Ne change pas le design global. Pour chaque affirmation modifiée, note la source ou la raison de retrait. Ne crée aucun KPI ni graphique. Conserve URLs, liens, HTML valide, changement de langue et fonctionnalités. Exécute les tests ciblés ; mets à jour PROGRESS.md. Produis un diff lisible et un commit sur la branche de refonte, jamais main. Arrête-toi après cette phase.
```

## PROMPT PHASE 2 — STRUCTURER LE CONTENU ET LE BUILD

```text
Lis 05_TARGET_ARCHITECTURE.md, 03_FILE_MAP.md et le journal. Implémente uniquement la phase 2 : une source de contenu FR/EN cohérente, un registre de preuves conservateur et un générateur Python/Jinja2 de pages HTML statiques, sans React ni framework client. Fais une migration progressive : une page d'abord pour valider les modèles, puis les autres. Ne supprime pas les URLs originales ni les fichiers legacy encore nécessaires. Le rendu doit rester stable pendant cette phase, pas de redesign prématuré. Implémente validation des contenus, build déterministe, liens localisés, tests de build et scripts portables. Documente installation et commandes réelles, exécute les tests et mets à jour PROGRESS.md. Stoppe avant la phase 3.
```

## PROMPT PHASE 3 — DESIGN SYSTEM, SANS REFAIRE LES PAGES ENCORE

```text
Lis 01_DESIGN_SYSTEM.md et ouvre docs/refonte/REFERENCE.html pour observer les choix visuels. Implémente la phase 3 seulement : tokens dark/light accessibles, base typographique, grille, boutons, nav, carte projet, ligne d'expérience, section heading, composants des études de cas. Crée la vraie architecture CSS (pas une nouvelle couche *-final.css), tout en gardant temporairement les styles historiques où des pages en dépendent. Pas de changements massifs de contenu. Prépare une vue de démonstration si nécessaire, compare les composants à la maquette aux six largeurs de test, vérifie contrastes et focus/reduced-motion. Mets à jour PROGRESS.md et commit si gate PASS. Arrête-toi.
```

## PROMPT PHASE 4 — REFONTE DES DEUX ACCUEILS

```text
Lis 02_PAGE_COPY_AND_UX.md, 01_DESIGN_SYSTEM.md et la maquette REFERENCE.html. Reconstruis index.html et index-en.html avec exactement cet ordre : hero -> selected work (Square flagship, Credit Scoring, BrokerFlow, Retail secondaire) -> experience -> evidence-based methodology -> education -> expertise -> contact. Préserve les identités/photos, projets et CV, les anciennes ancres, des liens FR/EN qui fonctionnent sans JS, et des métadonnées propres. Utilise uniquement des composants/tokens de la phase 3. Pas de faux KPI, de cartes génériques « compréhension/soin/évaluation », de glow, de dégradés multiples ou d'animations décoratives. Vérifie 360, 390, 768, 1024, 1440, 1920, zoom 200%, navigation clavier, console, boutons CV et tous les liens. Rapport avec captures avant/après, mise à jour PROGRESS.md, commit. Ne touche pas encore à la migration de toutes les études de cas.
```

## PROMPT PHASE 5 — ÉTUDES DE CAS

```text
Lis 04_SCIENTIFIC_TRUTH.md et 03_FILE_MAP.md. Conçois le template commun des études de cas puis migre les pages dans l'ordre indiqué en 07_PHASES.md. Pour chaque page : question, données, approche, alternatives, pipeline réel, protocole, résultats vérifiés, analyse d'erreurs, limites, reproductibilité et contribution personnelle, uniquement quand les sources le permettent. Crée des figures conceptuelles explicitement étiquetées ou de vrais graphiques générés depuis des données autorisées. Ne fabrique aucune courbe, score ou effet métier. Harmonise FR/EN, SEO, menus, liens, URL FR historique. Termine et teste chaque page avant la suivante, mets à jour PROGRESS.md et commits séparés. Ne commence pas la consolidation générale avant que les pages publiques fonctionnent.
```

## PROMPT PHASE 6 — RETIRER LE LEGACY ET FINITION

```text
Exécute uniquement la phase 6 de 07_PHASES.md. Analyse avec preuve quels CSS/JS sont désormais inutilisés ; supprime progressivement les couches de overrides, i18n JS legacy, code mort, animations et icônes décoratives. Ne retire un fichier qu'après vérification de toutes ses importations. Optimise images/portrait, ajoute metas SEO, og:image, sitemap.xml, robots.txt, 404.html si adaptés à l'hébergement. Mets README.md à jour avec les chemins réels, installation, build et tests ; n'invente pas de formulaire ni de fonctionnalités. Tous les liens, anciennes URL et les langues doivent rester valides. Compare les captures et exécute le test de non-régression. Mise à jour PROGRESS.md + commit. Arrête-toi.
```

## PROMPT PHASE 7 — QUALITY GATE FINAL

```text
Lis 06_QA.md. Implémente les tests nécessaires (Python, Playwright et/ou outils disponibles), une CI réaliste, des contrôles statiques du build, liens, ancrages, assets, langue, claims, thème, accessibilité et responsive. Exécute réellement les tests. Réalise captures aux six tailles, vérifie erreurs navigateur et Lighthouse/axe si disponibles ; marque NOT_RUN lorsque l'outil manque. Corrige les régressions sans ajouter de CSS de dernière minute ; refactorise la cause. Crée un rapport final dans docs/refonte/PROGRESS.md avec scores MESURÉS, environnement, commandes, limites et comparaison à baseline. Ne merge pas dans main. Stoppe pour revue.
```

## PROMPT PHASE 8 — PR ET DÉPLOIEMENT, APRÈS REVUE

```text
Avant tout déploiement, dresse le bilan exact branche vs main : fichiers modifiés, captures avant/après, résultats de tests, données non publiées, points incertains, URLs conservées. Prépare une pull request propre et détaillée si mon accès Git le permet. Ne merge pas automatiquement ; attends mon approbation explicite. Après accord, vérifie que la publication GitHub Pages garde les URL historiques et que les pages publiques, CV, navigation FR/EN, SEO et mobile fonctionnent. Toute anomalie est documentée et corrigée sur une branche dédiée.
```

## PROMPT POUR UNE NOUVELLE CONVERSATION CURSOR

```text
Reprends la refonte de mon portfolio. Commence par lire AGENTS.md et docs/refonte/PROGRESS.md, puis les règles et fichiers de spécification correspondant à la prochaine phase inachevée. Vérifie git status et branche, résume ce qui est réellement implémenté et testé, les risques restants et le prochain lot minimal. Ne recommence pas un redesign depuis zéro et ne fais pas plusieurs phases à la fois. N'invente aucune métrique. Demande-moi de valider le passage à la phase suivante si les gates ne sont pas remplis.
```

## PROMPT DE REVUE VISUELLE (APRÈS PHASE 4 OU 5)

```text
Compare le rendu réel local aux objectifs de docs/refonte/REFERENCE.html et 01_DESIGN_SYSTEM.md, à 360/390/768/1024/1440/1920. Prends captures avant/après, identifie précisément défauts de hiérarchie, alignement, contraste, densité, responsive, états de focus, boutons non visibles ou animations trop présentes. Propose et exécute des corrections dans les fichiers CSS/composants déjà définis; ne crée pas de nouvelle feuille de overrides. Ne change pas les chiffres, dates, faits ou contenus scientifiques pendant cette revue. Rapporte preuves des améliorations, sans déclarer les objectifs atteints sans captures/tests.
```
