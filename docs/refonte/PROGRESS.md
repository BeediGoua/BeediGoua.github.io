# PROGRESS — Journal de la refonte

Branche : `refonte-research-portfolio` · Mis à jour : 2026-11-02

| Phase | Statut | Gate | Commentaire |
|---|---|---|---|
| 0 — Baseline | DONE | PASS | Audit initial |
| 1 — Vérité scientifique | DONE | PASS | P0 corrigés + evidence-register |
| 2 — Build / contenu | DONE | PASS | Jinja homes + case studies |
| 3 — Design system | DONE | PASS | 8 CSS actifs |
| 4 — Accueil FR/EN | DONE | PASS | Hero signature (logos, portrait, ton personnel) |
| 5 — Case studies | DONE | PASS | 11 FR + 11 EN générés |
| 6 — Consolidation | DONE | PASS | Legacy déplacé dans `assets/_legacy/` |
| 7 — Tests | DONE | PASS (partiel outils) | validate/build/check/bilingual/experience/language OK ; Playwright/Lighthouse NOT_RUN |
| 8 — PR | BLOCKED | — | Push GitHub auth / `gh` absent |

## Plan exécuté
Voir `docs/refonte/PLAN_EXECUTION.md`.

## Commandes
```
python scripts/validate_content.py
python scripts/build_site.py
python scripts/check_site.py
python scripts/test_bilingual_complete.py
python scripts/test_experience_pages.py
python scripts/test_global_language.py
```

## Livrables clés
- Accueil anti-template : nom complet, logos Sorbonne/ENSAI/MS2A, portrait, texte style ancien
- 22 pages projets unifiées (`*-en.html` ajoutées, URLs FR historiques conservées)
- CSS actifs : tokens, base, layout, components, home, case-study, responsive, motion
- Legacy archivé : `assets/_legacy/`

## Restes connus
- Push/PR à faire dès que l’auth GitHub est disponible
- Lighthouse / axe NOT_RUN
- Contenu case studies volontairement prudent (pas de KPI inventés)
