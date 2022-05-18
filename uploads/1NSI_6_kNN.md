---
title: "kNN"
author: "qkzk"
date: "2022/05/18"

---

# $kNN$

## L'algorithme $k$ nearest neighbors


### $kNN$ est un algorithme...

- [x] de classification
- [ ] d'optimisation
- [ ] de tri
- [ ] _Aucune des réponses ne convient_


### On considère l'exemple suivant

![knn](https://miro.medium.com/max/3544/1*mAgqYN_HLbYYXXkQdyBA6Q.png)

On fixe $k = 3$ et on utilise la distance usuelle.

Quelle catégorie sera attribuée au nouveau point ?

- [x] Catégorie 1
- [ ] Catégorie 2
- [ ] Impossible de décider avec cette valeur de $k$
- [ ] Les deux catégories


### On considère l'exemple suivant :

| Longueur | Largeur | Catégorie |
|----------|---------|-----------|
| 0.3      | 1.1     | A         |
| 0.5      | 1.2     | A         |
| 0.7      | 1.5     | B         |
| 0.8      | 1.7     | B         |

Et le nouveau point :

| Longueur   | Largeur   |
| ---------- | --------- |
| 0.4        | 1.2       |

En utilisant la distance usuelle et $k=1$, quelle catégorie attribuer à ce point ?

- [x] A
- [ ] B
- [ ] A et B
- [ ] impossible de décider

### Lorsqu'on utilise kNN on privilégie des valeurs _impaires_ de $k$. Pourquoi ?

- [x] Cela évite les ex aequo
- [ ] C'est la meilleure approche. Démontré par Von Neumann
- [ ] C'est la meilleure approche. Démontré par Linus Torvald
- [ ] C'est faux, on choisit toujours $k=2$

### Compléter l'étape manquante de l'algorithme $kNN$

1. Calculer la distance entre chaque donnée d'apprentissage et la nouvelle donnée
2. _à compléter_
3. Garder les $k$ premiers
4. La catégorie est la catégorie majoritaire de l'étape précédente

- [x] ordonner selon la distance croissante
- [ ] ordonner selon la distance décroissante
- [ ] retirer toutes les distances supérieures à $k$
- [ ] élever toutes les distances au carré

### L'inconvénient majeur de $kNN$ est :

- [x] de devoir utiliser toutes les données d'apprentissage pour chaque nouvelle donnée
- [ ] de devoir faire un tri
- [ ] d'être parmi les algorithmes d'apprentissage les plus complexes
- [ ] d'être difficile à implémenter


