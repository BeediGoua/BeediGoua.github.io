# QA - Formation premium et déduplication des logos

Modifications appliquées :

- cartes Formation fermées rendues plus compactes ;
- timeline centrale affinée et connecteurs ajoutés ;
- point actif renforcé visuellement ;
- bouton Détails/Réduire avec chevron ;
- panneau ouvert mieux séparé, plus compact et lisible ;
- enseignements présentés sous forme de tags ;
- une seule carte Formation ouverte à la fois ;
- adaptation mobile conservée ;
- suppression des logos techniques dupliqués dans les pages principales et détaillées ;
- règle CSS de sécurité contre les images consécutives en double.

Contrôles exécutés :

- `python scripts/check_site.py` : OK
- `python scripts/test_experience_pages.py` : OK
- `node --check assets/js/education-accordion.js` : OK
- 63 éléments dupliqués retirés dans 10 pages détaillées.
