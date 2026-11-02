# 10 — Revue visuelle : instructions d'acceptation du rendu

Le fichier `REFERENCE.html` est une maquette statique de la direction visuelle, pas un modèle de code à copier mot pour mot. Pour accepter l'UI de production, comparer **captures réelles** plutôt que la liste des CSS.

## Ordre d'importance

1. **Lisibilité immédiate** — nom, spécialisation, formation, preuve de travail et CTA sont visibles sans effort.
2. **Signature** — vrai portrait, compositions asymétriques, hiérarchie typographique, schémas de recherche. Aucun ensemble de badges/icônes ne doit remplacer le contenu.
3. **Densité** — beaucoup d'information utile en peu d'espace sans oppression ; éviter les gros blocs presque vides.
4. **Niveau scientifique** — une étude de cas ne peut pas se contenter de 4 paragraphes marketing ; elle doit définir questions, protocole, limites, sources.
5. **Cohérence** — mêmes composants dans les pages projets, même typographie, mêmes bordures, même ordre de navigation.
6. **Comportement** — le design n'est accepté que si navigation clavier, mobile, JS désactivé et lien de langue sont raisonnablement fonctionnels.

## Comparaison à effectuer

Créer une matrice avec capture de `REFERENCE.html` et capture réelle des pages `index.html`/`index-en.html` aux largeurs 390, 768, 1440. Pour chaque écart, écrire : élément ; problème ; cause CSS/HTML ; correction dans *fichier de composants existant* ; résultat visuel. Ne PAS chercher une correspondance pixel-perfect au détriment des textes réels plus longs.

## Signaux d'échec visuel

- Hero dépassant deux écrans mobiles uniquement à cause de décorations.
- Titre principal sur dégradé coloré générique, énorme glow autour du portrait.
- Plus de badges/icônes que de phrases explicatives dans les projets.
- Cartes de même taille occupant une très grande hauteur avec peu de texte.
- Une deuxième feuille CSS « final » ajoutée pour compenser des règles précédentes.
- Deux langues qui changent la structure scientifique des études de cas.
- Graphiques « crédibles » mais fabriqués à partir de points inventés.
- Usage de filtres de projet, sliders, animations ou un faux chatbot sans besoin utilisateur.

## Résultat final recherché

Un recruteur n'a pas besoin de connaître la stack UI pour identifier le niveau de travail : il voit une personne, des travaux structurés, des modèles évalués, des limites explicitées et un code source documenté. L'esthétique reste une enveloppe cohérente au service de cela.
