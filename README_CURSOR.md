# KIT CURSOR — Refonte Research Editorial du portfolio

Ce dossier ne remplace pas le site. Il contient les **instructions, contraintes et une maquette de référence** pour que Cursor refonde `BeediGoua/BeediGoua.github.io` de manière contrôlée. Aucune page de production n'est remplacée par l'installation du kit.

## Installation (Windows + Cursor)

1. Ouvrir dans Cursor le **dossier racine du dépôt**, celui qui contient `index.html`, `index-en.html`, `projects/`, `assets/` et `scripts/`.
2. Créer une branche de travail avant toute refonte :
   ```bash
   git status
   git switch -c refonte-research-portfolio
   ```
   Si la branche existe déjà, l'ouvrir avec `git switch refonte-research-portfolio`. Si `git status` n'est pas propre, sauvegarder/committer/stasher les changements *avant* de créer la branche, sans les écraser.
3. Copier **le contenu de ce kit** à la racine du dépôt (ne pas créer un sous-dossier englobant). Résultat attendu : `AGENTS.md`, `.cursor/rules/` et `docs/refonte/` à côté de `index.html`.
4. Ouvrir `docs/refonte/REFERENCE.html` dans un navigateur avec un serveur local (le portrait sera chargé depuis `../../assets/img/goua.png` si le kit est au bon endroit). C'est une **maquette de direction artistique**, pas le site de production.
5. Dans Cursor, démarrer en mode **Plan** (sélecteur de mode, ou `Shift+Tab`) et coller **uniquement** le prompt Phase 0 de `docs/refonte/08_PROMPTS_CURSOR.md`. Les règles `.cursor/rules/*.mdc` s'appliquent automatiquement selon leur portée.
6. Valider l'audit, puis passer en **Agent** pour une phase à la fois. N'enchaîner les phases qu'après vérification des critères de sortie. Les prompts sont fournis dans `08_PROMPTS_CURSOR.md`.

## Ordre des documents

- `AGENTS.md` : contrat général court.
- `docs/refonte/00_BRIEF.md` : vision et périmètre.
- `docs/refonte/01_DESIGN_SYSTEM.md` : couleurs, typographie, responsive, interaction.
- `docs/refonte/REFERENCE.html` : maquette visuelle autonome, surtout destinée à Cursor/au navigateur.
- `docs/refonte/02_PAGE_COPY_AND_UX.md` : contenu souhaité et structure FR/EN.
- `docs/refonte/03_FILE_MAP.md` : tâches **sur les chemins existants**.
- `docs/refonte/04_SCIENTIFIC_TRUTH.md` : correction des écarts et registre de preuves.
- `docs/refonte/05_TARGET_ARCHITECTURE.md` : générateur statique et bilinguisme.
- `docs/refonte/06_QA.md` : tests obligatoires, mesures et vérification visuelle.
- `docs/refonte/07_PHASES.md` : plan par lots, gates et commits.
- `docs/refonte/08_PROMPTS_CURSOR.md` : prompts de lancement séparés, prêts à copier.
- `docs/refonte/09_REPO_BASELINE.md` : arborescence et constats sourcés du dépôt.
- `docs/refonte/PROGRESS.md` : à **mettre à jour par Cursor** à chaque étape.

## Deux précautions déterminantes

**Ne pas traiter toutes les phases en un seul prompt géant.** Cela conduit facilement à des modifications massives, des CSS de rattrapage et des tests oubliés. Une phase = une revue = un commit.

**Ne pas croire que toutes les métriques du portfolio sont validées.** Les chiffres présents dans les pages doivent être comparés aux rapports, notebooks ou dépôts sources. S'ils ne sont pas vérifiables, Cursor doit signaler le point dans `PROGRESS.md` et enlever la prétention non prouvée, pas fabriquer une preuve.

## Portée de la maquette

La maquette montre hiérarchie, mise en page, couleurs, typographie et densité. Les textes, rangs de projets, dates et chiffres qui y figurent doivent rester soumis à `content/source-of-truth.md` et aux règles de publication. Les contenus sensibles ne doivent jamais être mis en ligne.

## Si Cursor propose de tout refaire sous React / Next / Tailwind

Refuser : l'objectif retenu est un **site statique HTML/CSS/JS natifs**, avec éventuellement **Jinja2 + Python uniquement à la compilation**. GitHub Pages ne doit recevoir que des fichiers statiques. Préférer simplifier ce qui existe plutôt que changer de stack.
