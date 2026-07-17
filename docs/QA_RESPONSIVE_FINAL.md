# QA responsive final

## Pages modifiées
- `index.html`
- `index-en.html`
- `assets/css/responsive-final.css`

## Breakpoints testés
- 390 × 844 (téléphone)
- 430 × 932 (grand téléphone)
- 768 × 1024 (tablette portrait)
- 1024 × 900 (tablette paysage / petit laptop)
- 1440 × 1000 (ordinateur)

## Résultats de largeur
Pour chaque largeur testée :
- `document.documentElement.scrollWidth === clientWidth`
- aucun débordement horizontal global
- Hero, cartes récapitulatives, formation, expériences et projets restent dans le viewport

## Changements responsive principaux
- navigation mobile transformée en barre compacte avec menu hamburger correctement aligné ;
- Hero mobile redessiné avec texte avant portrait et portrait réduit ;
- logos et boutons adaptés à chaque largeur ;
- cartes « Ma démarche » et récapitulatives empilées sur téléphone ;
- timeline Formation neutralisée sur tablette/téléphone au profit de cartes pleine largeur ;
- expériences forcées en pleine largeur, sans héritage de timeline desktop ;
- projets et compétences adaptés en une colonne sur téléphone ;
- tablette dédiée : Hero en deux colonnes, cartes récapitulatives en deux colonnes, formation en liste simple ;
- desktop conservé avec mise en page large et aérée.

## Tests fonctionnels exécutés
- `python3 scripts/check_site.py` : OK
- `python3 scripts/test_global_language.py` : OK
- `python3 scripts/test_experience_pages.py` : OK
- `python3 scripts/build_site.py` : OK

## Remarque
`scripts/test_bilingual_complete.py` contient un chemin absolu vers un ancien dossier local (`/mnt/data/portfolio_langfix/portfolio_work`) et ne peut donc pas être exécuté tel quel dans un autre environnement. Les tests bilingues actifs de `test_global_language.py` passent correctement.
