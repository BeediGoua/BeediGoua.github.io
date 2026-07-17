# QA_REPORT

## Changements appliqués
- Même système visuel conservé : CSS, typographies, couleurs, blobs, cartes et animations existants.
- Page d’accueil restructurée autour du positionnement Data Scientist, des expériences et de quatre études de cas.
- FINZUU repositionné comme expérience Data Scientist.
- Pages détaillées réécrites : Square, Ville de Paris, FINZUU, Credit Scoring, BrokerFlow, Retail Demand, HEGP.
- Chiffres LCL alignés sur le PDF fourni.
- Brier/calibration supprimés du projet LCL car non documentés.
- WAPE Retail traité comme résultat préliminaire non publié.
- Résultats BrokerFlow contextualisés comme benchmark de prototype.
- Confidentialité et limites ajoutées systématiquement.

## Contrôles automatiques
- Liens locaux indexés vérifiés par scripts/check_site.py.
- Aucun TODO ou « À confirmer » visible dans les pages publiques.
- Aucun fichier source supprimé.

## Mise à jour - pages détaillées des expériences

Les trois expériences professionnelles disposent désormais de pages bilingues FR/EN avec :
- vue d'ensemble problème / approche / valeur ;
- rôle et contributions ;
- workflow visuel responsive ;
- méthodes et technologies ;
- difficultés et réponses ;
- résultats et livrables ;
- enseignements et pistes d'amélioration ;
- confidentialité et limites.

Fichiers concernés :
- `projects/square-management.html`
- `projects/ville-de-paris.html`
- `projects/finzuu.html`
- `assets/css/experience-detail.css`
- `assets/js/experience-detail.js`

Contrôles effectués :
- vérification des liens locaux ;
- vérification de la présence des contenus français et anglais ;
- vérification de la structure HTML ;
- vérification de l'affichage responsive prévu par CSS.

## Ajustements navigation expériences - juillet 2026

- Les boutons des trois expériences professionnelles utilisent désormais le libellé uniforme « Voir les détails ».
- La barre de retour / langue / thème défile normalement avec la page.
- Après le défilement du Hero, seul un bandeau compact contenant le titre de l’expérience apparaît en haut de l’écran.
- Les badges ainsi que les cartes Organisation / Rôle / Lieu / Période restent dans le flux normal et ne sont jamais fixes.
- Vérifications exécutées : liens locaux, présence des trois pages détaillées, assets CSS/JS et syntaxe JavaScript.

## Mise à jour design - Formation et projets complémentaires
- Formation convertie en parcours alterné gauche/droite avec ligne centrale et cartes homogènes.
- Boutons Hero remplacés par CV, GitHub et LinkedIn avec icônes.
- Accents vert menthe harmonisés sur méthode, expériences, projets, repères, compétences et contact.
- Ajout de `projects/autres-projets.html` avec 3 projets complémentaires bilingues et liens GitHub.
- Ajout de `assets/css/homepage-polish.css` pour isoler les ajustements visuels.
- Validation DOM, syntaxe JavaScript, liens locaux et placeholders : OK.

## Final visual corrections
- Removed the global professional-experience timeline line and decorative dots that crossed cards.
- Rebuilt Education as a balanced responsive three-card grid to prevent overlap at desktop widths.
- Reduced unused vertical space in the homepage hero.
- Added a shared visual polish layer to experience and project detail pages.
- Fixed all secondary-project detail pages to return to `autres-projets.html`.
- Verified local links and public placeholders with `scripts/check_site.py`.
