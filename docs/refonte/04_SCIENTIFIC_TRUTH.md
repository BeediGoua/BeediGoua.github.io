# 04 — Audit de vérité scientifique et publication

**Principe premier :** les anciennes pages sont des hypothèses éditoriales, pas une preuve scientifique. Lire `content/source-of-truth.md`, les rapports et les dépôts sources quand ils existent. Si accès privé absent, le dire. Les chiffres ci-dessous sont des **valeurs actuellement annoncées dans le portfolio** et/ou sa source de vérité, à **contrôler**, et non certifiées indépendamment.

## Ordre de fiabilité

1. Rapport original/notebook validé/artifact de métriques public ou autorisé à la publication.
2. Code ou tests reproduisant effectivement la mesure sur le jeu annoncé.
3. README du dépôt associé, avec prudence (peut lui aussi contenir des claims promotionnelles).
4. `content/source-of-truth.md`, qui fixe les règles de prudence et la présentation actuelle.
5. Pages HTML du portfolio, à considérer comme **non fiables en cas de contradiction**.

## Écarts P0 à résoudre

### ReviewGuardian — `projects/reviewguardian.html`

FR : modération de **toxicité** des commentaires; TF-IDF, interprétabilité LIME/SHAP, API et monitoring, corpus équilibré de 7 296 avis. EN actuel : bots, campagnes coordonnées, clustering de graphes, Isolation Forest, MongoDB, `70%+ Detection Rate` synthétique. Ce sont des systèmes différents.

Action : comparer au dépôt associé et à ses fichiers, réécrire FR et EN de façon **équivalente**, ne garder que pipelines/techniques vraiment codés. Si métriques 7 296 ou autres ne sont pas traçables, les retirer de la partie publique ou indiquer explicitement leur origine. Ne PAS traduire l'ancienne version EN telle quelle.

### Music Recommender — `projects/music-recommender.html`

FR : Word2Vec, embeddings sémantiques, fusion de signaux, filtres dynamiques, Streamlit. EN actuel : collaborative filtering, SVD, Precision@10 0.78, 0.65 de sérendipité, 100% de cold start, latence <50 ms. Le README du dépôt associé annonce également des métriques divergentes (dont une précision 94,2 % et une latence 85 ms). Incompatible sans protocoles bien définis.

Action : rétablir l'architecture qui existe dans le code et aligner FR/EN. Ne pas afficher de KPI sans jeu, métrique, protocole, taille et artefact de validation. Une bonne démo sans benchmark vaut mieux qu'une fausse performance.

### Zimnat — `projects/zimnat.html`

EN actuel : dual engine Bayesian + CatBoost, garantie « Zero Commercial Error / 100% », impact commercial présenté comme réalisé. Le README du dépôt source comporte un badge « Production ». Les règles métier peuvent **interdire un produit déjà détenu** sans garantir un taux zéro d'erreur métier.

Action : distinguer invariant de filtrage testé, performance prédictive, simulation Streamlit et déploiement réel. Remplacer absolus par limites précises. Afficher « prototype/démonstrateur » si c'est le statut réel et le documenter.

## Chiffres des principaux travaux à vérifier

| Projet | Énoncé en circulation | Vérification exigée / précaution |
|---|---|---|
| Square | 189 combinaisons RAG sur documents longs | Matrice exacte des configurations et périmètre publiable ; aucun partage de données internes |
| Credit Scoring | 532 567 comptes et 143 variables, AUC test logistique 0,784 / RF 0,800 / XGBoost 0,798 | Rapport original, split, prétraitement, AUC ROC, provenance des données ; **ne pas prétendre calibration** |
| Credit Scoring | 372 381 train + 159 845 test = 532 226 | L'écart de **341** par rapport à 532 567 reste à expliquer avec le rapport ; ne pas inventer une cause |
| BrokerFlow | 50 cas annotés, AUC 0,728, Brier 0,150, seuil 0,231, 44 tests | Vérifier fichiers de résultats et protocoles. Bien distinguer modèle de crédit vs évaluation des agents ; très petit benchmark |
| Retail | Favorita, horizon 8 semaines, ADI/CV², quantiles, Newsvendor | Baselines, décomposition temporelle, tests réels ; **WAPE 8% non publié** |
| HEGP | Kaplan-Meier/Cox, données de suivi | Aucun résultat médical chiffré sans rapport et autorisation de diffusion |
| FINZUU | scoring agricole explicable, FastAPI, PostgreSQL/PostGIS | Système métier vs modèle de défaut prédictif ; pas de revendication de production validée |
| Ville de Paris | LAPI, SIV, SIREN, CO2, analyses | Pas de données personnelles/opérationnelles confidentielles ni de chiffres sans preuve |

## Structure de preuve cible

Créer `content/evidence-register.json` quand l'architecture de contenu est prête, avec par exemple :

```json
{
  "claims": [
    {
      "id": "brokerflow_auc_example",
      "project": "brokerflow",
      "label_fr": "AUC ROC",
      "label_en": "ROC AUC",
      "display_value": "0.728",
      "status": "needs_verification",
      "source_ref": null,
      "protocol_ref": null,
      "sample_context": "prototype — périmètre à vérifier",
      "public_allowed": false,
      "review_notes": "Ne pas afficher tant que source et protocole non confirmés"
    }
  ]
}
```

Ne pas confondre `verified` et `public_allowed` : une métrique vraie peut être confidentielle et donc impropre à publication. Le générateur doit **échouer explicitement** ou **ne pas afficher** un claim non autorisé ; jamais remplacer par une valeur calculée au hasard.

## Processus pour chaque page projet

1. Extraire les claims FR et EN actuelles dans un tableau.
2. Relier à dépôt source, rapport, notebook, métrique ou code.
3. Classer : `verified_public`, `verified_private`, `needs_verification`, `contradicted`, `conceptual`.
4. Écrire une description source neutre, puis la traduction.
5. Afficher seulement les claims autorisées ; ne pas transformer des tests synthétiques en mesure de production.
6. Ajouter `Protocole`, `Résultats` et `Limites` sans fausse précision. Expliquer la contribution **personnelle** et les travaux d'équipe.
7. Ajouter des figures **quantitatives** uniquement depuis les artefacts ; schéma conceptuel explicitement nommé.
8. Journaliser incertitudes et liens sources dans `PROGRESS.md`.

## Modèle de page case study

Titre/année/role/type → Contexte et question → Données et droits → Approche et alternatives → Pipeline réel → Évaluation/splits/baselines → Résultats vérifiés → Diagnostics et erreurs → Limites → Reproductibilité et statut → « Avec du recul ».

Pour une expérience professionnelle confidentielle, remplir uniquement les sections publiables et préciser clairement pourquoi certaines ne le sont pas. Ne pas utiliser de placeholders « coming soon » ou des graphiques artificiels dans la version déployée.
