# 01 — Design system Research Editorial / spécification exacte

**Référence visuelle exécutable** : `REFERENCE.html`, ouvrable dans le navigateur. Cette référence décrit une **direction** ; les composants doivent être intégrés proprement dans le dépôt et validés sur les vraies pages.

## A. Identité artistique

Inspiration : couverture d'un research brief + carnet d'ingénierie + site personnel contemporain. Plus de typographie que d'icônes, plus de résultats démontrables que de badges. Sombre sans néons. Sections aérées mais pas vides. Trames, bordures et numérotation éditoriale ; jamais de cumul de blocs arrondis identiques. La photo et la singularité des projets portent l'identité.

**Exclure** : gradients purple-pink/bleu saturé, « glassmorphism » omniprésent, blobs flottants, 10 couches d'ombres, badges en ligne sur tous les titres, barres de progression des compétences, faux terminal, faux graphique avec chiffres inventés, icône compass/target/tools répétée.

## B. Tokens à coder dans `assets/css/tokens.css`

```css
:root {
  color-scheme: dark;
  --bg: #0b1220;
  --surface: #111b2b;
  --surface-raised: #162235;
  --border: #2d3b50;
  --text: #f4f7fb;
  --text-muted: #b7c3d4;
  --primary: #4866d6;
  --primary-hover: #5d78e4;
  --accent: #55d2bd;
  --link: #80b8ff;
  --max-width: 1160px;
  --reading-width: 760px;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --ease: cubic-bezier(.2,.7,.2,1);
  --duration-fast: 150ms;
  --duration-normal: 220ms;
}
```

Le thème clair reste possible mais doit avoir une palette **complète** et tester les contrastes, par exemple : `--bg:#f4f6fa`, `--surface:#fff`, `--surface-raised:#eaf0f6`, `--border:#d6dfe8`, `--text:#122037`, `--text-muted:#45566f`, `--primary:#344eae`, `--accent:#136d61`, `--link:#2759a8`. Ces valeurs sont un point de départ à contrôler dans un vrai navigateur, pas une validation automatique de conformité.

## C. Typographie et rythme

- Bricolage Grotesque (ou fallback système) : h1, h2 et parfois accroche, **pas le corps**.
- Inter (ou system-ui) : texte, navigation, tableaux, métadonnées.
- `h1` 64 px desktop, 40 px mobile (en `clamp`), densité légère et hauteur de ligne 1.04–1.12.
- Titres de sections 34 desktop, 28 mobile, sans dégradés.
- Titre de carte projet 23–25 desktop, 21 mobile.
- Body 16–17 px, hauteur de ligne 1.55–1.65.
- Métadonnées 13–14 px ; ne pas imposer de gris trop sombre.
- Paragraphes longs plafonnés à `--reading-width: 760px`; 65–75 caractères par ligne en pratique.
- Fond sans texture agressive. Préférer des séparateurs `1px` plutôt que de grosses ombres.

## D. Composition

- Conteneur `width: min(calc(100% - 48px), 1160px); margin-inline:auto`; sous 600 px, marges latérales ~16 px.
- Sections : 80 px de séparation desktop / 56 px mobile, ajustables selon densité réelle.
- Navigation desktop discrète : nom/monogramme à gauche, liens au centre/droite, contrôle FR/EN et CV accessibles.
- Hero : grille approx. 58 % texte / 42 % portrait, avec portrait moins contrasté et sans glow ; mobile = texte et CTA d'abord, portrait réduit ensuite.
- Sélection de projets : **1 grande carte flagship Square**, puis 2 cartes côte à côte Credit Scoring et BrokerFlow ; Retail en carte secondaire ou lien vers index. Ne pas afficher 4 gros blocs identiques.
- Les cartes : bordure `--border`, surface sobre, rayon ≤ 14px, pas d'ombre permanente ; hover = petite modification de bordure ou translation ≤2px.
- Expériences : liste éditoriale ou tableau asymétrique, périodes à gauche, contribution à droite. Pas de timeline verticale complexe.
- Méthode : 3 notes techniques concrètes (protocoles, compromis, erreur), sans cartes avec pictogrammes génériques.
- Formation : 2 lignes Sorbonne / ENSAI, modules effectivement suivis, dates vérifiées.
- Compétences : 4 groupes textuels avec outils sélectionnés, pas 30 logos identiques ni pourcentage de niveau arbitraire.
- Footer : contact court, email, GitHub, LinkedIn, CV FR/EN, copyright dynamique.

## E. Interactions

1. Boutons : fond primaire accessible ou contour, focus très visible, tailles cliquables généreuses, pas d'effet brillant.
2. Menus mobiles : ouverture/fermeture réelle, `aria-expanded`, touche `Escape`, focus correct, fermeture après navigation.
3. FR/EN : vrais liens, pas de modal et pas d'animation de transition masquant du texte.
4. Thème : conserver seulement s'il fonctionne réellement sur toutes les pages ; préférence persistante sans flash. Si impossible à valider pendant migration, ne pas créer un faux bouton.
5. Les cartes projet peuvent être des liens globaux, mais éviter les liens interactifs imbriqués ; l'URL doit exister.
6. Les animations doivent rester facultatives ; contenu visible même sans JS. `prefers-reduced-motion` doit désactiver mouvement non essentiel.
7. `:focus-visible` sur liens et boutons, scroll avec espace pour header fixe (`scroll-margin-top`).
8. Ne pas créer de carrousel automatique.

## F. Responsive / écrans de validation

- 360 : navigation mobile, pas de scroll horizontal, CTAs non coupés.
- 390 : portrait proportionné, paragraphes lisibles.
- 768 : formations et cartes en une colonne si nécessaire.
- 1024 : header non comprimé, largeur raisonnable.
- 1440 : composition flagship asymétrique + deux projets.
- 1920 : conteneur max 1160, pas de lignes géantes.
- Zoom 200 %, clavier seul, texte anglais long, préférences réduites.

## G. Figures et images

Créer `assets/img/projects/` (un schéma utile par projet avant de multiplier les images). Faire les schémas en SVG/HTML/CSS pour pipelines **uniquement conceptuels** ; figures quantitatives uniquement issues de vrais artefacts d'expérience. Légendes claires : données, échelle, protocole et limites. Images : `alt` utile, `width`/`height`, formats optimisés et priorité de chargement appropriée (portrait above-the-fold non lazy si LCP). Préserver l'identité réelle de la photo. `assets/img/goua.png` existe, ainsi que variantes JPG/WebP ; audit des usages avant suppression.

## H. Barre de qualité visuelle

Le site doit être reconnaissable sur capture floutée par sa hiérarchie, ses colonnes et sa typographie, non par une accumulation d'icônes. Si une section ressemble à une landing page SaaS générique, réduire les objets visuels et augmenter le contenu unique. Les preuves ne doivent jamais être reléguées sous une décoration inutile.
