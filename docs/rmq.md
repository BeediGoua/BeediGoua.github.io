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
- Les zones visuelles intermédiaires ont été supprimées sur les 3 pages projet.
- Le flux est simplifié : **The Challenge → The Technical Solution**.
- Les anciens placeholders sont neutralisés côté CSS pour éviter un retour accidentel.

---

## 2) Diagnostic du “fond blanc”

Le fond blanc visible peut venir de 3 sources différentes :

1. **Le composant HTML/CSS placeholder**
   - Corrigeable côté code.

2. **Les surfaces du schéma en thème clair**
   - Certaines variables peuvent rendre des blocs trop lumineux en light mode.

Conclusion : il faut traiter à la fois les blocs supprimés et les variables du schéma.

---

## 3) Règles de thème à respecter

Le projet utilise actuellement le modèle :
- classe `body.light-theme` (et non `data-theme="dark"`).

Donc pour les sections restantes (notamment le schéma) :
- utiliser les variables existantes,
- éviter toute couleur codée en dur pour le fond et le texte.

À éviter :
- `background: white;`
- `color: black;`
- `border: 1px solid #ddd;`

---

## 4) Plan d’action recommandé

### Priorité haute
1. Conserver le flux sans image sur les pages projet.
2. Vérifier que les blocs de schéma restent lisibles en thème clair et sombre.
3. Ne pas réintroduire de placeholder visuel en production.

### Priorité moyenne
4. Ajuster finement les variables light-theme si certaines surfaces paraissent encore trop blanches.
5. Ajouter une micro-zone de preuve (KPI) sous le schéma pour renforcer la crédibilité produit.

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
- Le socle technique est prêt : thème, robustesse JS, et suppression des zones placeholder.
- Le chantier restant est l’ajustement visuel fin du schéma en light theme.
