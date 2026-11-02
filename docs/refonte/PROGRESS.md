# PROGRESS — Journal de la refonte

Branche : `refonte-research-portfolio` · Date : 2026-11-02

| Phase | Statut | Gate | Commentaire |
|---|---|---|---|
| 0 — Baseline | DONE | PASS | Audit local + navigateur |
| 1 — Vérité scientifique | DONE | PASS | P0 FR/EN réconciliés + evidence-register |
| 2 — Build / contenu | DONE | PASS | JSON + Jinja2 + validate/build |
| 3 — Design system | DONE | PASS | tokens/base/layout/components/home/responsive/motion/case-study |
| 4 — Accueil FR/EN | DONE | PASS | Générés ; ordre hero→projects ; SEO hreflang |
| 5 — Case studies | PARTIAL | PARTIAL | P0 corrigés ; Square contenu OK ; migration visuelle CSS complète des 11 pages reportée |
| 6 — Consolidation | PARTIAL | PARTIAL | README/SEO ajoutés ; CSS legacy encore présent (nécessaire aux pages projets) |
| 7 — Tests / CI | PARTIAL | PARTIAL | validate/build/check_site OK ; pas de Playwright/CI GitHub encore |
| 8 — PR / mise en ligne | IN_PROGRESS | — | PR à ouvrir ; pas de merge auto |

---

### Phase 0 — 2026-11-02
- Inventaire confirmé : 2 accueils, 11 projets, 14 CSS + style.css, 9 JS, 1172 `!important`
- Canonical EN = FR (corrigé en phase 4) ; tests bilingual hardcodés `/mnt/data` ; Playwright absent
- Captures : baseline ancienne + nouvelle accueil vérifiée dans navigateur Cursor
- Gate PASS

### Phase 1 — 2026-11-02
- `reviewguardian.html` EN : bots/Isolation Forest/70% → toxicité TF-IDF/LIME/SHAP aligné FR
- `music-recommender.html` EN : SVD/Precision@10/serendipity → Word2Vec + embeddings ; KPI retirés
- `zimnat.html` : Zero Commercial Error / 100% retirés ; statut prototype explicite FR/EN
- Credit Scoring : note écart 341 ; pas de calibration affirmée ; sync `portfolio_data.json`
- BrokerFlow homepage : « modèle calibré » → prototype
- Créé `content/evidence-register.json` (14 claims, contradicted = non publics)
- `python scripts/check_site.py` OK
- Gate PASS

### Phase 2–4 — 2026-11-02
- Contenu : `profile.json`, `experiences.json`, `projects/{square,credit,brokerflow}.json`
- Templates Jinja2 `templates/home.html` + partials
- `scripts/validate_content.py`, `scripts/build_site.py` (ROOT via pathlib, homes + legacy credit)
- CSS Research Editorial : tokens → motion
- Accueils régénérés : 1 h1, CTA `#projects`, CV localisés, hreflang, canonical distincts, `#method` + alias `#approach`
- Navigateur : `http://localhost:8000/index.html` titre ML & AI Evaluation, sections conformes
- Gate PASS pour 2–4

### Phase 5 — PARTIAL
- P0 pages corrigées
- Square Management : contenu méthodologique déjà conforme (189, confidentialité, pas de métriques inventées)
- Migration visuelle unifiée de toutes les études de cas vers `case-study.css` : **à poursuivre**
- Pages EN statiques dédiées (`*-en.html`) : non créées (bascule data-lang conservée temporairement)

### Phase 6–7 — PARTIAL
- README corrigé (lien, clone, FormSubmit retiré)
- `404.html`, `robots.txt`, `sitemap.xml`, `requirements-dev.txt`
- Legacy CSS/JS **conservés** car pages projets en dépendent
- CI GitHub Actions : non ajoutée (éviter faux échecs sans deps)
- Lighthouse/axe : NOT_RUN

### Phase 8
- Préparer PR vers branche de déploiement ; **ne pas merger sans accord**

## Commandes réellement exécutées
```
python docs/refonte/_audit_phase0.py
python scripts/check_site.py          # OK
python scripts/test_experience_pages.py  # OK
python scripts/test_global_language.py   # FAIL credit-scoring (attendu)
python scripts/test_bilingual_complete.py # FAIL playwright + /mnt/data
python scripts/validate_content.py    # OK
python scripts/build_site.py          # OK (idempotent)
python -m http.server 8000
```
