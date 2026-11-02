# Plan d’exécution — finir la refonte

## Objectif
Terminer le kit Research Editorial **sans look vibe-coding** : signature personnelle (photo, logos, ton), preuves sourcées, URLs historiques intactes.

## Étape A — Accueil signature (anti-template)
### A1. Contenu
- Garder le paragraphe hero style ancien (déjà fait)
- Titres de sections moins jargon / plus humains
- Réduire les disclaimers trop visibles hors études de cas
### A2. Visuel hero
- Composition asymétrique texte + portrait (pas carte générique flottante)
- Réintroduire logos Sorbonne / ENSAI / MS2A discrètement
- Remplacer monogramme `GB.` par identité plus personnelle si utile
- CTA primaire `#projects`, secondaire CV
### A3. Sections
- Selected work : flagship Square + 2 cartes (déjà) — densifier typo, moins de chrome
- Expériences en lignes éditoriales
- Méthode : 3 points concrets, phrases plus naturelles
### A4. Vérif
- 360 / 768 / 1440 + clavier + FR/EN

## Étape B — Études de cas (11 URLs)
### B1. Infra
- `templates/case-study.html` + `assets/css/case-study.css` enrichi
- Schéma JSON par projet sous `content/projects/`
- Génération FR (URL historique) ; EN via `data-lang` ou `-en.html` si stable
### B2. Lot 1
- square-management, credit-scoring, brokerflow, retail-demand-forecasting
### B3. Lot 2
- finzuu, ville-de-paris, analyse-survie
### B4. Lot 3
- reviewguardian, music-recommender, zimnat, autres-projets
### B5. Gate chaque page
- claims = evidence-register ; limites ; liens ; mobile

## Étape C — Consolidation
### C1. Audit imports CSS/JS
### C2. Retirer legacy non référencé (après preuve)
### C3. README / CONTENT_POLICY courte si besoin

## Étape D — QA
### D1. validate_content + build idempotent + check_site
### D2. Corriger test_bilingual path portable
### D3. Captures navigateur + console
### D4. CI minimale seulement si stable (sinon documenter NOT_RUN)

## Étape E — Livraison
### E1. PROGRESS.md final
### E2. Commit(s) sur `refonte-research-portfolio`
### E3. Push / PR si auth disponible — **pas de merge main**
