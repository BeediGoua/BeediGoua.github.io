# 00 — Brief de refonte / décision produit

**Dépôt :** https://github.com/BeediGoua/BeediGoua.github.io
**Statut :** spécification à implémenter et à valider, pas affirmation de résultats déjà obtenus.

## Vision

Créer un portfolio personnel de **Data Scientist / Statistical ML / Applied AI & Evaluation**, avec une esthétique **Research Editorial**. Le site doit ressembler davantage à une sélection de travaux documentés qu'à une landing page SaaS. Le recruteur doit comprendre en 15 à 30 secondes qui est l'auteur, ce qu'il étudie, ce qu'il a réellement construit et où trouver la preuve.

## Public et scénarios

1. **Research Scientist / Applied Scientist / ML Research recruiter** : regarde d'abord spécialité, rigueur expérimentale, qualité de projets, cursus, lien CV.
2. **Research Engineer / ML Engineer manager** : vérifie code, baseline, reproductibilité, séparation des responsabilités, contraintes système.
3. **Recruteur généraliste** : scanne parcours, dates, disponibilités et contact rapidement.
4. **Pair technique** : veut comprendre hypothèses, méthode, résultats, limites et contributions personnelles.

## Promesse centrale

« J'utilise les statistiques, la conception d'expériences et l'ingénierie ML pour construire **et surtout évaluer** des systèmes fiables. » Cette proposition doit être étayée par des études de cas, non répétée sous forme de slogans. Éviter « expert », « state-of-the-art », « révolutionnaire », « production-ready » sans preuve.

## Priorités de contenu

1. Square Management — évaluation de 189 configurations RAG (préciser confidentialité et portée).
2. Credit Scoring — comparaison interprétabilité vs AUC (rapport source, sans prétention de calibration documentée).
3. BrokerFlow AI — prototype et évaluation modulaire, benchmark 50 cas (limitation explicite).
4. Retail Demand — prévision + décision, sans WAPE non validé.
5. Autres travaux : HEGP, FINZUU, Ville de Paris, ReviewGuardian, Music Recommender, Zimnat selon qualité documentaire.

## Ce qu'on doit voir au-dessus de la ligne de flottaison

- Nom identifiable et sérieux, **un seul `h1`**.
- Spécialisation claire : Statistical Machine Learning / AI Evaluation (le titre doit rester fidèle au profil).
- Mention Sorbonne MS2A et ENSAI correcte.
- Disponibilité de stage 2027 (à confirmer au moment de publication).
- Photo réelle conservée, aucune génération/remplacement de visage.
- Bouton primaire vers `#projects`, secondaire vers CV de la bonne langue.
- Un accès à GitHub, contact et changement FR/EN accessible.

## Contraintes incontournables

- Le site actuel est public sur GitHub Pages : conserver les URLs existantes.
- HTML/CSS/JS natifs ; Python/Jinja2 uniquement à la génération, pas de JS framework ni de build Node en production.
- Source de vérité : `content/source-of-truth.md`, puis références de projets lorsqu'elles sont vérifiables. Pas d'informations inventées ou d'augmentation artificielle du prestige.
- Éviter divulgation de documents confidentiels Square, LCL, Ville de Paris, HEGP ou FINZUU.
- International : FR + EN cohérents et indexables.
- WCAG 2.2 AA comme cible. Accessible clavier et préférence mouvement réduit.
- Modifications par phases, commits indépendants, tests réels. Pas de déploiement non validé.

## Non-objectifs

- Créer un chatbot pour impressionner.
- Ajouter dashboards de métriques sans données, compteur animé, 3D, parc d'icônes, animations de survol permanentes.
- Créer un blog vide ou des faux articles.
- Refondre le branding via une banque d'icônes payante.
- Optimiser les scores Lighthouse au détriment du contenu ou de l'accessibilité.
- Afficher « recherche » ou « publications » si aucun article de recherche n'est réellement public.

## Definition of success

Toutes les pages restent fonctionnelles, toutes les informations importantes sont sourcées et cohérentes, la lecture mobile/desktop est nette, le site utilise un système visuel unique, et la source ainsi que le pipeline de publication sont reproductibles. Ces critères sont détaillés dans `06_QA.md`.
