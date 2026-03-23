# Analyse des pages projet (version alignée au repo)

## Objectif
Stabiliser l’affichage des pages secondaires (projets) et supprimer les zones perçues comme inachevées.

---

## 1) État réel du code aujourd’hui

### Ce qui est déjà correct
- Les 3 pages projet chargent bien le script central :
  - `projects/zimnat.html`
  - `projects/music-recommender.html`
  - `projects/reviewguardian.html`
- Le script central `assets/js/project-script.js` gère :
  - thème (lecture `localStorage.theme` + classe `body.light-theme`),
  - reveal au scroll,
  - sticky header,
  - i18n.
- Le script est maintenant robuste si Feather CDN échoue (appel protégé via `safeFeatherReplace`).

### Ce qui est maintenant corrigé
- Les placeholders visuels ont été remplacés sur les 3 pages projet :
   - `projects/zimnat.html`
   - `projects/music-recommender.html`
   - `projects/reviewguardian.html`
- Un composant visuel final a été ajouté dans `assets/css/project-detail.css` :
   - `.project-visual`
   - `.project-screenshot`

---

## 2) Diagnostic du “fond blanc”

Le fond blanc visible peut venir de 3 sources différentes :

1. **Le composant HTML/CSS placeholder**
   - Corrigeable côté code.

2. **Le wrapper du visuel**
   - Si une couleur fixe est utilisée (`#fff`), le mode sombre sera incohérent.

3. **Le screenshot lui-même**
   - Si l’image exportée contient un fond blanc, ce blanc restera visible même avec un bon thème.

Conclusion : il faut traiter à la fois le composant et le média.

---

## 3) Règles de thème à respecter

Le projet utilise actuellement le modèle :
- classe `body.light-theme` (et non `data-theme="dark"`).

Donc pour les nouveaux composants visuels :
- utiliser des variables existantes (`--card-bg`, `--glass-border`, `--text-color`, etc.),
- éviter toute couleur codée en dur pour le fond et le texte.

À éviter :
- `background: white;`
- `color: black;`
- `border: 1px solid #ddd;`

---

## 4) Plan d’action recommandé

### Priorité haute
1. Remplacer les images temporaires (`hero-bg.jpg`) par des captures réelles par projet.
2. Vérifier la qualité des images (fond, lisibilité, ratio 16:9).
3. Conserver le composant visuel final centralisé dans `assets/css/project-detail.css`.

### Priorité moyenne
4. Conserver `.visual-placeholder-lg` uniquement comme fallback interne, moins dominant visuellement.
5. Ajouter une micro-zone de preuve (KPI) sous le visuel pour renforcer la crédibilité produit.

---

## 5) Critères de validation

- Mode sombre/clair cohérent sur les 3 pages projet.
- Aucune erreur JS bloquante dans la console.
- Aucun bloc placeholder texte visible en production.
- Affichage propre mobile/tablette/desktop.
- Déploiement vérifié sans cache (navigation privée + hard refresh).

---

## 6) Verdict

- Le socle technique (script central + thème) est en place.
- Le principal chantier restant est **UX/contenu visuel** (remplacer les images temporaires par des captures projet).
- Le socle technique est prêt : thème, robustesse JS et composant visuel sont en place.
