# QA bilingue FR/EN

## Corrections appliquées

- Réparation complète de `assets/lang/fr.json` et `assets/lang/en.json` (les deux fichiers étaient invalides à cause de fragments placés avant l'objet JSON).
- Création de `assets/js/i18n-dictionaries.js` afin que les traductions fonctionnent aussi lorsque le portfolio est ouvert directement en local avec `file://`.
- Centralisation de la langue dans `assets/js/global-language.js`.
- Synchronisation de la langue entre la page principale, les expériences, les projets sélectionnés et les autres projets.
- Synchronisation des liens internes avec `?lang=fr` ou `?lang=en`.
- Synchronisation du PDF de CV avec la langue active.
- Traduction des contenus dynamiques et des éléments injectés après le chargement via `MutationObserver`.
- Synchronisation des libellés de l'accordéon Formation (`Détails/Réduire` et `Details/Collapse`).
- Traduction complète de la page principale anglaise, notamment les expériences et les projets sélectionnés.
- Traduction des métriques statiques restantes dans Credit Scoring, BrokerFlow et Retail Demand Forecasting.
- Titres d'onglet bilingues sur toutes les pages.

## Tests exécutés

- 13 pages HTML testées.
- Pour chaque page : bascule EN puis FR.
- Vérification qu'aucun bloc de la mauvaise langue ne reste visible.
- Vérification que tous les blocs de la langue active restent visibles.
- Vérification de toutes les clés `data-i18n` dans les deux dictionnaires.
- Vérification des libellés dynamiques de la Formation.
- Vérification de la syntaxe JavaScript.
- Vérification des liens locaux et des placeholders publics via `scripts/check_site.py`.

Résultat : **0 erreur bilingue détectée sur les 13 pages**.
