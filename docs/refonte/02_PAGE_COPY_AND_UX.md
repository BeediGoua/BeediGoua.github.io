# 02 — Page d'accueil : structure et copy FR/EN

Ce document fixe **l'ordre, la fonction et le niveau de détail** des sections. Le texte est une proposition éditoriale à vérifier et raccorder aux données structurées, pas un résultat scientifique supplémentaire.

## Navigation

FR : `Travaux` -> `#projects` ; `Expérience` -> `#experience` ; `Méthode` -> `#method` ; `Parcours` -> `#education` ; `Contact` -> `#contact`. EN : `Work / Experience / Approach / Education / Contact`. Lien CV, lien FR/EN et bascule thème (uniquement si réellement fonctionnelle). Header sticky sobre, pas de 3 rangées de navigation.

Conserver les anciennes ancres auxquelles des liens extérieurs pourraient pointer : `#hero`, `#projects`, `#experience`, `#education`, `#skills`, `#contact`, éventuellement `#approach` comme alias discret pointant vers `#method`. Ne supprimer une ancre qu'après audit des liens.

## 01. HERO

**FR (proposition)**

Surtitre : `STATISTIQUES · MACHINE LEARNING · ÉVALUATION DE L'IA`

`h1`: `Goua Beedi`

Sous-titre principal (pas un deuxième `h1`) : `Machine Learning & AI Evaluation`

Description : `Je construis et j'évalue des modèles de machine learning, avec une attention particulière à la qualité des données, à la robustesse des résultats et aux erreurs.`

Preuve : `En master MS2A à Sorbonne Université, après ma formation d'ingénieur à l'ENSAI. Chez Square Management, j'ai étudié 189 configurations de systèmes RAG sur documents longs.`

Disponibilité : `À la recherche d'un stage en ML / Applied Research à partir d'avril 2027.` **Vérifier date et statut au moment du déploiement.**

Actions : `Explorer mes travaux` -> `#projects` ; `Télécharger mon CV` -> `assets/CV_GouaHenri_FR.pdf`; liens textuels GitHub et LinkedIn.

**EN (traduction fidèle, non différente scientifiquement)**

Eyebrow: `STATISTICS · MACHINE LEARNING · AI EVALUATION`

`h1`: `Goua Beedi`

Subheading: `Machine Learning & AI Evaluation`

Body: `I build and evaluate machine learning models, focusing on data quality, robustness, and understanding where systems fail.`

Evidence: `Currently pursuing the MS2A master's programme at Sorbonne University after engineering studies at ENSAI. At Square Management, I investigated 189 RAG configurations for long-document processing.`

Availability: `Seeking an ML / Applied Research internship starting around April 2027.`

Actions: `Explore selected work` -> `#projects`; `Download CV` -> `assets/CV_GouaHenri_EN.pdf`.

Les formulations sur diplôme ENSAI doivent correspondre au diplôme effectivement délivré ; source actuelle `content/source-of-truth.md` écrit « diplômé », à vérifier avant republication.

## 02. SELECTED WORK (IMMÉDIATEMENT APRÈS LE HERO)

Intro FR : `Une sélection de travaux où l'enjeu n'est pas seulement d'entraîner un modèle, mais de définir une évaluation crédible et de comprendre ses limites.`

Intro EN : `Selected work where the challenge is not just training a model, but designing a credible evaluation and understanding its limits.`

### Square : grande carte flagship

Type : `RAG / Retrieval / Evaluation` ; problème : `Comment les choix d'OCR, de découpage et de recherche affectent-ils la qualité d'un système sur documents longs ?` ; méthode : comparer les configurations dans un protocole documenté ; preuve publiable : `189 configurations étudiées` ; limite : `données et livrables internes non publics` ; CTA : `Lire l'étude de cas`.

### Credit Scoring : carte technique

Question : `Comment arbitrer performance de discrimination, parcimonie et interprétabilité dans un score de risque ?` ; approche : logistique vs RF/XGBoost ; résultat conditionnel : `AUC test 0,784 vs 0,800 et 0,798` seulement avec source confirmée ; limite : `pas de validation de calibration ni de production attestée`.

### BrokerFlow : carte technique

Question : `Comment garder une décision explicable et contrôlée quand modèles, règles et composants agentiques interagissent ?` ; approche : sous-systèmes séparés, fallback, cas annotés ; preuve : 50 cas du prototype si portée expliquée ; limites de taille / généralisation explicites.

### Retail : CTA / quatrième carte secondaire

Message : `Prévision probabiliste des ventes et décision de stock` ; montrer baseline + quantiles/stock uniquement si code/graphique réel ; ne pas publier le WAPE 8 % incertain.

CTA global : `Voir tous les projets` -> page `projects/autres-projets.html` et variante EN si elle existe.

## 03. EXPERIENCES

Présentation **éditoriale** (période / organisation / rôle / contribution), pas 6 cartes. Ordre **chronologique inversé selon dates réellement confirmées** : FINZUU (2026), Square (2025), Ville de Paris (2024), sauf décision volontaire justifiée de mettre Square en premier pour sa pertinence. Ne pas inverser dates sans raison.

- Square : protocole RAG, 189 configurations, évaluation ; secret métier explicite.
- FINZUU : scoring agricole explicable, données de référence, contrôles humains ; ne pas revendiquer de validation de production non prouvée.
- Ville de Paris : pipeline multi-source LAPI/SIV/SIREN et statistiques appliquées ; ne pas publier de données internes.

Chaque expérience ouvre sa page détaillée quand elle existe.

## 04. COMMENT J'ÉVALUE / HOW I EVALUATE

Remplacer les quatre cartes de principes génériques par 3 annotations étayées :

1. `Protocoles avant performance` : baselines, splits, groupes, fuites et métriques, avec renvoi à projet réel ; ne pas promettre un protocole non utilisé.
2. `Compromis vérifiables` : interprétabilité versus AUC en crédit.
3. `Analyse d'échecs` : fausses réponses RAG ou tests de fallback BrokerFlow, en utilisant seulement des exemples publiables ou des illustrations déclarées conceptuelles.

**Phrase possible FR :** `Je privilégie les résultats que l'on peut expliquer et refaire à ceux qui paraissent simplement impressionnants.`
**EN:** `I favor results that can be explained and reproduced over numbers that merely look impressive.`

Supprimer les slogans `Comprendre`, `Soigner`, `Évaluer`, `Rendre utilisable` sans exemples : ils n'aident pas à différencier le site.

## 05. PARCOURS

Deux entrées structurées : Sorbonne Université — master MS2A (année et statut vérifiés) ; ENSAI — statistiques/data science (date et statut vérifiés). Si une formation est en cours, le dire. Limiter logos à une seule représentation chacun ; ne pas mettre 3 badges de cursus sous le portrait. Mentionner des **cours réellement suivis**, pas des compétences autodidactes comme modules officiels.

## 06. EXPERTISE & TOOLS

Quatre domaines : `Statistical Learning`, `Machine Learning & Evaluation`, `LLM / Retrieval`, `ML Engineering`. 3 à 6 compétences spécifiques par domaine et 2 à 5 outils pertinents, aucun pourcentage de maîtrise. Éviter doublons entre texte et grille d'icônes. Si l'expérience en deep learning est autodidacte, être fidèle au niveau.

## 07. CONTACT / FOOTER

Une phrase humaine, courte : `Un projet de recherche appliquée ou un stage en ML ? Échangeons.` Email en `mailto:`, CV dans chaque langue, GitHub et LinkedIn. Aucun faux formulaire de contact. Footer sobre, copyright année courante sans édition manuelle.

## Principes rédactionnels transversaux

- Rédiger à la première personne lorsque la contribution personnelle est établie, sans supposer avoir créé seul des systèmes d'équipe.
- Conserver noms d'employeurs, années, métriques strictement cohérents avec `content/source-of-truth.md` et preuves.
- 1 fait fort par carte, pas 6 tags et 5 icônes.
- Traduction EN naturelle mais **strictement équivalente** sur méthodes, chiffres et portée.
- Ne pas vendre une « expertise recherche » en absence de publication ; positionner comme candidat en apprentissage et expérimentation solide.
