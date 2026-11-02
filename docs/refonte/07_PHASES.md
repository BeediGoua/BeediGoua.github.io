# 07 — Ordre exécutable : 9 phases avec gates

**Ne pas utiliser un seul prompt global pour coder les 9 phases.** Phase = un lot compréhensible, un ensemble de tests, une revue de diff, un commit. `main` n'est jamais modifiée directement.

## Phase 0 — Baseline et audit [LECTURE + documentation]

**Entrées :** repo, brief, maquette, inventaire. **Actions :** `git status`, branche, `git ls-files`, dépendances CSS/JS par page, textes FR/EN, métriques, URLs, capture navigateur si possible, tests existants, robots/SEO, état GitHub Pages. Vérifier que les noms des fichiers contenus dans `03_FILE_MAP.md` correspondent au checkout local. **Sortie :** `PROGRESS.md` renseigné, captures et problèmes mesurés, priorisation P0–P3. **GATE :** aucune prétention visuelle non vérifiée; ne pas modifier code de production dans cette phase.

Commit : `docs: baseline and audit portfolio refactor`.

## Phase 1 — Réparer vérité scientifique [P0]

**Actions :** reviewguardian EN, music-recommender EN, zimnat ; comparer repositories sources. Vérifier chiffres principaux credit scoring, brokerflow, retail ; ajouter registre des preuves en mode conservateur. Ne pas récrire un projet qui n'a aucune preuve disponible; retirer les claims risquées et documenter. **Sortie :** FR/EN ne se contredisent plus sur techniques, chiffres, portée; limitations honnêtes.

**GATE :** aucune métrique nouvelle sans preuve, aucun partage privé, pages fonctionnelles, liens internes OK.

Commit : `fix(content): reconcile bilingual project claims and evidence`.

## Phase 2 — Source structurée et générateur statique

**Actions :** construire schémas de contenu source FR/EN + evidence; templates partagés; générateur Python/Jinja2; préserver URLs; ne pas casser `content/portfolio_data.json` pendant migration. Une page d'abord, puis les autres. Pas de génération de projets non audités. **Sortie :** build sur checkout propre, tests d'idempotence, tous les HTML historiques encore fonctionnels.

**GATE :** même rendu logique et faits, aucun lien cassé, contenu non dupliqué de façon incohérente.

Commit : `refactor(build): shared static templates and localized content`.

## Phase 3 — Design system / bibliothèque de composants

**Actions :** tokens, palettes, styles typographiques, composants button, container, section-heading, project-card, experience-entry, badges essentiels, lien, nav, footer; modèle de page. Ajouter une page d'inspection de composants non publiée si nécessaire. **Sortie :** styles réutilisables, rendu conforme à `REFERENCE.html`, responsive vérifié pour les composants.

**GATE :** aucun nouveau `-final.css`, pas de remplacement brutal des vieux styles encore utilisés, dark/light accessibles.

Commit : `style: introduce research editorial system`.

## Phase 4 — Accueil FR + EN

**Actions :** hero précis; projets après hero; expérience, méthode, formation, skills, contact; photo; nav. Supprimer les cards génériques; conserver toutes ancres et CTA. **Sortie :** deux pages cohérentes, toutes interactions testées, captures six largeurs.

**GATE :** aspect visuel de la maquette respecté, mobile réellement testé, aucune claim inexacte.

Commit : `feat(home): research-led bilingual landing page`.

## Phase 5 — Études de cas [ordre recommandé]

1. Square
2. Credit Scoring
3. BrokerFlow
4. Retail
5. FINZUU
6. Ville de Paris
7. HEGP Survival
8. ReviewGuardian
9. Music Recommender
10. Zimnat
11. Autres projets (index)

**Actions :** modèle commun + figures réelles/conceptuelles explicites, contexte, protocole, résultats/erreurs, limites; pages EN statiques, URLs FR conservées. Le contenu de ReviewGuardian / Music / Zimnat corrigé en phase 1 ne doit pas régresser. **GATE :** URLs, langues, contenus, alt, performance, source de preuves et captures passés pour chaque page avant la suivante.

Commits séparés possibles : `feat(case-study): square evaluation`, etc.

## Phase 6 — Consolidation frontend et documentation

**Actions :** retirer les CSS/JS non utilisés APRÈS vérification, supprimer effets décoratifs, anciens modules i18n, polices/vides; refactor README et documentation, 404/sitemap/robots/og si justifiés. **Sortie :** code lisible, styles utiles uniquement, navigation des pages maintenue.

**GATE :** re-test complet des 13 HTML historiques + nouvelles variantes EN, aucun import manquant.

Commit : `chore: remove legacy UI layers and update docs`.

## Phase 7 — QA, CI et performance

**Actions :** scripts portables, pytest et tests navigateur, axe, Lighthouse, réponses mobiles, SEO, éventuels bugs; CI stable. **Sortie :** rapport de validation reproductible et bugs résiduels.

**GATE :** toutes les assertions promises par le README sont testées ou explicitement qualifiées; pas de faux succès.

Commit : `test: enforce build, localization, accessibility and links`.

## Phase 8 — Pull request et publication [AVEC AUTORISATION]

**Actions :** comparer branch/main, documenter les changements et régressions, fournir captures et checklists. Créer PR si connecteur Git/credential permet. **Ne pas merger automatiquement** ; demander approbation de l'utilisateur. Après publication, tester les URLs publiques et corrections potentielles de cache.

**GATE :** approbation explicite + validations réelles ; aucune obligation d'attendre une fonctionnalité non prioritaire (blog, nouvelle animation, etc.).

## Format obligatoire de réponse à Cursor

À chaque phase, indiquer : **ce qui change / pourquoi / fichiers exacts / tests exécutés et sorties / captures / éléments manquants / statut du gate / proposition de commit**. Écrire la même chose dans `PROGRESS.md` pour transmettre le contexte à une nouvelle session Cursor.
