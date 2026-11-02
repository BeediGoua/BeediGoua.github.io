# Instructions de projet — Portfolio Goua Beedi

Projet : `BeediGoua/BeediGoua.github.io` — refonte **Research Editorial** du portfolio Data Science / ML / AI Evaluation.

## Instructions impératives

1. Lis `docs/refonte/00_BRIEF.md`, `01_DESIGN_SYSTEM.md`, `02_PAGE_COPY_AND_UX.md`, `03_FILE_MAP.md`, `04_SCIENTIFIC_TRUTH.md`, `05_TARGET_ARCHITECTURE.md`, `06_QA.md` et `07_PHASES.md` avant d'entreprendre une refonte globale. Consulte `REFERENCE.html` pour la direction visuelle. Les règles détaillées `.cursor/rules/*.mdc` précisent les contraintes.
2. Commence par la **phase 0** (audit réel de l'arborescence, captures, tests de référence et vérification des informations). N'édite pas le site en phase 0, à l'exception des rapports d'audit. Après validation, traite UNE phase à la fois.
3. **Jamais d'écriture sur `main`, de push ou de merge automatique.** Travaille sur une branche dédiée, conserve une possibilité de retour arrière.
4. **Pas de données ni de résultats inventés.** Tout chiffre, méthode, diplôme, résultat et statut de production doit correspondre à une preuve consultable. Respecte `content/source-of-truth.md` et les restrictions de confidentialité ; n'invente pas les courbes ou statistiques manquantes.
5. Conserver GitHub Pages et HTML/CSS/JS natifs. Une génération statique Python + Jinja2 est envisageable après validation du chemin de build. Ne pas passer à un framework client lourd sans décision écrite de l'utilisateur.
6. Tous les liens publiés, chemins historiques, CV FR/EN, navigation, accessibilité clavier, responsive, changement de langue et fonctionnalités réelles doivent fonctionner après chaque migration.
7. Pas de nouvelles feuilles `*-final.css` ou `polish-vN.css` : faire une migration propre avec suppression **après vérification** des anciennes règles. Ne supprime aucun CSS/JS tant qu'une page en a besoin.
8. Implémenter une UI sobre, distinctive, éditoriale et lisible, fond sombre, peu d'icônes, des figures et preuves concrètes, pas un template SaaS / dashboard artificiel.
9. Mettre à jour `docs/refonte/PROGRESS.md` après chaque phase : fichiers modifiés, décisions, tests réellement exécutés, résultats, risques, points bloquants et prochain lot.
10. Quand une information manque, ne pas bloquer toute la refonte : garder un libellé prudent ou omettre l'affirmation et noter précisément ce qui nécessite une vérification.

## Réponse attendue à la fin de chaque phase

Résumé des changements, liste exacte des fichiers, commandes et résultats des tests, captures comparatives quand pertinentes, éléments non vérifiables, liens ou URLs préservés et commit créé (si permis). Ne jamais écrire « tous les tests passent » sans les avoir exécutés.
