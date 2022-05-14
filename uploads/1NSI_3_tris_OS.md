---
title: "NSI Première - tris et algorithmes séquentiels"
author: "qkzk"
date: "2021/12/31"
theme: "metropolis"
geometry: "margin=1.5cm"
header-includes:
- \usepackage{fancyhdr}
- \usepackage[T1]{fontenc}
- \pagestyle{fancy}
- \fancyhead[CO,CE]{NSI Première exemple de QCM}
- \fancyfoot[LE,RO]{\thepage}
- \thispagestyle{fancy}
- \usepackage{tcolorbox}
- \newtcolorbox{myquote}{colback=teal!10!white, colframe=teal!55!black}
- \renewenvironment{Shaded}{\begin{myquote}}{\end{myquote}}

---


## Tris 

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :

```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```

- [x] 0 et `len(tableau)`
- [ ] 0 et `len(tableau) + 1`
- [ ] 1 et `len(tableau)`
- [ ] 1 et `len(tableau) + 1`

### Quelle valeur retourne la fonction "mystere" suivante ?

```python
def mystere(liste):
     valeur_de_retour = True
     indice = 0
     while indice < len(liste) - 1 :
          if liste[indice] > liste[indice + 1]:
               valeur_de_retour = False
          indice = indice + 1
     return valeur_de_retour
```

- [x] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément

### Soit le programme de tri suivant :

```python
def tri(lst):
    for i in range(1,len(lst)):
        valeur = lst[i]
        j = i
        while j>0 and lst[j-1]>valeur:
            lst[j]=lst[j-1]
            j = j-1
        lst[j]=valeur_a_inserer
```

De quel type de tri s'agit-il ?

- [x] Tri par insertion
- [ ] Tri fusion
- [ ] Tri par sélection
- [ ] Tri à bulles

### Soit un tableau à trier: `[56, 22, 14, 5, 35]`. Quel algorithme a trié ce tableau ?

Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |



- [x] algorithme par insertion
- [ ] algorithme par sélection
- [ ] algorithme séquentiel
- [ ] algorithme préférentiel

## Parcours séquentiels

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?

- [x] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.

### On considère la fonction suivante.

```python
def mystere(tab):
    booleen = True
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            booleen = False
    return booleen
```

Que renvoie l'appel `mystere([1, 2, 7, 3, 10])` ?


- [x] `False`
- [ ] `True`
- [ ] `[1, 2, 3, 7, 10]`
- [ ] On ne peut pas savoir

### Quelle est la valeur de c à la fin de l'exécution du code suivant :

```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```

- [x] 3
- [ ] 0
- [ ] 2
- [ ] 10



