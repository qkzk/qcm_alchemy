---
title: "kNN - Dichotomie"
author: "qkzk"
date: "2022/05/18"

---

# kNN et dichotomie

## kNN

### kNN est un algorithme...

- [x] de classification
- [ ] d'optimisation
- [ ] de tri
- [ ] _Aucune des réponses ne convient_


### Quel est l'objectif de l'algorithme des k plus proches voisins ?

- [t]

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
| 0.4      | 1.3     | A         |
| 0.7      | 1.5     | B         |
| 0.8      | 1.7     | B         |
| 0.7      | 1.9     | B         |

Et le nouveau point :

| Longueur   | Largeur   |
| ---------- | --------- |
| 0.4        | 1.2       |

En utilisant la distance usuelle et $k=3$, quelle catégorie attribuer à ce point ?

- [x] A
- [ ] B
- [ ] A et B
- [ ] impossible de décider

### Lorsqu'on utilise kNN on privilégie des valeurs _impaires_ de $k$. Pourquoi ?

- [t]


## info

### Évaluer `s` après l'exécution du code suivant :

```python
s = 0
for i in range(5):
  s += i
```

- [x] 10
- [ ] 15
- [ ] `True`

### Exemple avec du html

```html
<h1>Titre</h1>
<h2>Soustitre</h2>
```

- [x] titre
- [ ] `<h1>`
- [ ] `<script>alert("1")</script>`


### Exemple avec du markdown

```markdown
# un titre

## un Soustitre

1. premier
2. second

* element
* autre element

[lien](url) 
![image](url)
```

- [x] c'est cool markdown
- [ ] je préfère cliquer partout


