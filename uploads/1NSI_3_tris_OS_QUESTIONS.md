
---
theme: "metropolis"
geometry: "margin=1.5cm"
header-includes:
- \usepackage{fancyhdr} 
- \pagestyle{fancy} 
- \fancyhead[C]{ Première - tris et algorithmes séquentiels }
- \fancyhead[LE,LO,RE,RO]{} 
- \fancyfoot[C]{ } 
- \thispagestyle{fancy} 
- \usepackage{tcolorbox} 
- \newtcolorbox{myquote}{colback=teal!10!white, colframe=teal!55!black}
- \renewenvironment{Shaded}{\begin{myquote}}{\end{myquote}}

---

## Parcours séquentiels

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.

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




- [ ] <code>False</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>
- [ ] On ne peut pas savoir

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 3
- [ ] 0
- [ ] 10

## Tris 

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



- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

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



- [ ] Tri par insertion
- [ ] Tri fusion
- [ ] Tri par sélection
- [ ] Tri à bulles

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme séquentiel
- [ ] algorithme par sélection
- [ ] algorithme par insertion
- [ ] algorithme préférentiel



\newpage

## Tris 

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



- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>

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



- [ ] Tri à bulles
- [ ] Tri par insertion
- [ ] Tri fusion
- [ ] Tri par sélection

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme préférentiel
- [ ] algorithme par sélection
- [ ] algorithme séquentiel
- [ ] algorithme par insertion

## Parcours séquentiels

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] On ne peut pas savoir
- [ ] <code>True</code>
- [ ] <code>False</code>

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 10
- [ ] 2
- [ ] 0
- [ ] 3

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.



\newpage

## Parcours séquentiels

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




- [ ] <code>True</code>
- [ ] On ne peut pas savoir
- [ ] <code>False</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 3
- [ ] 0
- [ ] 10

## Tris 

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



- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau)</code>

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



- [ ] Tri à bulles
- [ ] Tri par insertion
- [ ] Tri par sélection
- [ ] Tri fusion

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme préférentiel
- [ ] algorithme par sélection
- [ ] algorithme par insertion
- [ ] algorithme séquentiel



\newpage

## Parcours séquentiels

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




- [ ] <code>False</code>
- [ ] On ne peut pas savoir
- [ ] <code>True</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 10
- [ ] 3
- [ ] 0

## Tris 

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



- [ ] Tri par sélection
- [ ] Tri par insertion
- [ ] Tri fusion
- [ ] Tri à bulles

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



- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par sélection
- [ ] algorithme séquentiel
- [ ] algorithme par insertion
- [ ] algorithme préférentiel

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>



\newpage

## Parcours séquentiels

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




- [ ] <code>True</code>
- [ ] On ne peut pas savoir
- [ ] <code>False</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 0
- [ ] 3
- [ ] 10

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.

## Tris 

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



- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

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



- [ ] Tri à bulles
- [ ] Tri par insertion
- [ ] Tri fusion
- [ ] Tri par sélection

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme séquentiel
- [ ] algorithme préférentiel
- [ ] algorithme par insertion
- [ ] algorithme par sélection

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau)</code>



\newpage

## Tris 

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



- [ ] Tri à bulles
- [ ] Tri par insertion
- [ ] Tri fusion
- [ ] Tri par sélection

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



- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme séquentiel
- [ ] algorithme par insertion
- [ ] algorithme préférentiel
- [ ] algorithme par sélection

## Parcours séquentiels

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>
- [ ] On ne peut pas savoir
- [ ] <code>False</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 3
- [ ] 2
- [ ] 10
- [ ] 0



\newpage

## Parcours séquentiels

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 3
- [ ] 0
- [ ] 10

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




- [ ] On ne peut pas savoir
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>False</code>
- [ ] <code>True</code>

## Tris 

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



- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par sélection
- [ ] algorithme séquentiel
- [ ] algorithme préférentiel
- [ ] algorithme par insertion

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



- [ ] Tri par insertion
- [ ] Tri fusion
- [ ] Tri à bulles
- [ ] Tri par sélection

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>



\newpage

## Tris 

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



- [ ] Tri par insertion
- [ ] Tri par sélection
- [ ] Tri à bulles
- [ ] Tri fusion

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau) + 1</code>

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par insertion
- [ ] algorithme par sélection
- [ ] algorithme préférentiel
- [ ] algorithme séquentiel

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



- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

## Parcours séquentiels

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] On ne peut pas savoir
- [ ] <code>True</code>
- [ ] <code>False</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 0
- [ ] 10
- [ ] 3



\newpage

## Parcours séquentiels

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>
- [ ] On ne peut pas savoir
- [ ] <code>False</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 3
- [ ] 2
- [ ] 0
- [ ] 10

## Tris 

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par sélection
- [ ] algorithme par insertion
- [ ] algorithme séquentiel
- [ ] algorithme préférentiel

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



- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau)</code>

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



- [ ] Tri fusion
- [ ] Tri à bulles
- [ ] Tri par insertion
- [ ] Tri par sélection



\newpage

## Parcours séquentiels

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 3
- [ ] 10
- [ ] 2
- [ ] 0

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>False</code>
- [ ] <code>True</code>
- [ ] On ne peut pas savoir

## Tris 

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme séquentiel
- [ ] algorithme par sélection
- [ ] algorithme préférentiel
- [ ] algorithme par insertion

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



- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>

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



- [ ] Tri fusion
- [ ] Tri par sélection
- [ ] Tri à bulles
- [ ] Tri par insertion



\newpage

## Parcours séquentiels

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>
- [ ] <code>False</code>
- [ ] On ne peut pas savoir

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 3
- [ ] 2
- [ ] 0
- [ ] 10

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.

## Tris 

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



- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau) + 1</code>

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



- [ ] Tri par sélection
- [ ] Tri fusion
- [ ] Tri à bulles
- [ ] Tri par insertion

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme séquentiel
- [ ] algorithme par sélection
- [ ] algorithme préférentiel
- [ ] algorithme par insertion



\newpage

## Parcours séquentiels

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 10
- [ ] 3
- [ ] 0

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




- [ ] <code>False</code>
- [ ] <code>True</code>
- [ ] On ne peut pas savoir
- [ ] <code>[1, 2, 3, 7, 10]</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.

## Tris 

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



- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée

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



- [ ] Tri à bulles
- [ ] Tri par sélection
- [ ] Tri par insertion
- [ ] Tri fusion

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme préférentiel
- [ ] algorithme séquentiel
- [ ] algorithme par sélection
- [ ] algorithme par insertion



\newpage

## Tris 

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



- [ ] Tri par sélection
- [ ] Tri fusion
- [ ] Tri par insertion
- [ ] Tri à bulles

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>

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



- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par sélection
- [ ] algorithme séquentiel
- [ ] algorithme préférentiel
- [ ] algorithme par insertion

## Parcours séquentiels

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




- [ ] <code>True</code>
- [ ] <code>False</code>
- [ ] On ne peut pas savoir
- [ ] <code>[1, 2, 3, 7, 10]</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 3
- [ ] 0
- [ ] 2
- [ ] 10



\newpage

## Tris 

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



- [ ] Tri à bulles
- [ ] Tri fusion
- [ ] Tri par insertion
- [ ] Tri par sélection

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par insertion
- [ ] algorithme séquentiel
- [ ] algorithme par sélection
- [ ] algorithme préférentiel

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>

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



- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] La valeur du plus grand élément de la liste passée en paramètre

## Parcours séquentiels

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 0
- [ ] 10
- [ ] 2
- [ ] 3

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.

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




- [ ] <code>False</code>
- [ ] On ne peut pas savoir
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>



\newpage

## Parcours séquentiels

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




- [ ] <code>True</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>False</code>
- [ ] On ne peut pas savoir

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 0
- [ ] 3
- [ ] 10

## Tris 

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



- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre

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



- [ ] Tri par sélection
- [ ] Tri à bulles
- [ ] Tri fusion
- [ ] Tri par insertion

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme préférentiel
- [ ] algorithme par sélection
- [ ] algorithme par insertion
- [ ] algorithme séquentiel

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>



\newpage

## Parcours séquentiels

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
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




- [ ] <code>False</code>
- [ ] On ne peut pas savoir
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 0
- [ ] 3
- [ ] 10
- [ ] 2

## Tris 

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



- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

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



- [ ] Tri par insertion
- [ ] Tri à bulles
- [ ] Tri par sélection
- [ ] Tri fusion

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par insertion
- [ ] algorithme par sélection
- [ ] algorithme préférentiel
- [ ] algorithme séquentiel

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>



\newpage

## Tris 

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



- [ ] Tri fusion
- [ ] Tri par insertion
- [ ] Tri à bulles
- [ ] Tri par sélection

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau) + 1</code>

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par sélection
- [ ] algorithme séquentiel
- [ ] algorithme préférentiel
- [ ] algorithme par insertion

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



- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée

## Parcours séquentiels

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 10
- [ ] 0
- [ ] 2
- [ ] 3

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>
- [ ] <code>False</code>
- [ ] On ne peut pas savoir



\newpage

## Parcours séquentiels

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>False</code>
- [ ] <code>True</code>
- [ ] On ne peut pas savoir

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 10
- [ ] 0
- [ ] 3

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.

## Tris 

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>

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



- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

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



- [ ] Tri par insertion
- [ ] Tri à bulles
- [ ] Tri par sélection
- [ ] Tri fusion

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par insertion
- [ ] algorithme préférentiel
- [ ] algorithme par sélection
- [ ] algorithme séquentiel



\newpage

## Parcours séquentiels

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




- [ ] On ne peut pas savoir
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>
- [ ] <code>False</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 10
- [ ] 0
- [ ] 2
- [ ] 3

## Tris 

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme préférentiel
- [ ] algorithme par sélection
- [ ] algorithme séquentiel
- [ ] algorithme par insertion

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



- [ ] Tri fusion
- [ ] Tri à bulles
- [ ] Tri par insertion
- [ ] Tri par sélection

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



- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau) + 1</code>



\newpage

## Parcours séquentiels

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




- [ ] <code>True</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] On ne peut pas savoir
- [ ] <code>False</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 0
- [ ] 10
- [ ] 2
- [ ] 3

## Tris 

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme séquentiel
- [ ] algorithme par sélection
- [ ] algorithme par insertion
- [ ] algorithme préférentiel

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



- [ ] Tri par insertion
- [ ] Tri par sélection
- [ ] Tri fusion
- [ ] Tri à bulles

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau)</code>

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



- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée



\newpage

## Parcours séquentiels

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 3
- [ ] 2
- [ ] 10
- [ ] 0

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




- [ ] <code>False</code>
- [ ] On ne peut pas savoir
- [ ] <code>True</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.

## Tris 

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme préférentiel
- [ ] algorithme par insertion
- [ ] algorithme par sélection
- [ ] algorithme séquentiel

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



- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
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



- [ ] Tri à bulles
- [ ] Tri par sélection
- [ ] Tri par insertion
- [ ] Tri fusion

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>



\newpage

## Parcours séquentiels

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 0
- [ ] 3
- [ ] 10
- [ ] 2

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




- [ ] <code>False</code>
- [ ] On ne peut pas savoir
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.

## Tris 

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>

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



- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus grand élément de la liste passée en paramètre
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



- [ ] Tri par sélection
- [ ] Tri par insertion
- [ ] Tri fusion
- [ ] Tri à bulles

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme séquentiel
- [ ] algorithme préférentiel
- [ ] algorithme par insertion
- [ ] algorithme par sélection



\newpage

## Parcours séquentiels

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 0
- [ ] 10
- [ ] 3
- [ ] 2

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




- [ ] <code>True</code>
- [ ] <code>False</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] On ne peut pas savoir

## Tris 

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par insertion
- [ ] algorithme préférentiel
- [ ] algorithme séquentiel
- [ ] algorithme par sélection

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



- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée

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



- [ ] Tri à bulles
- [ ] Tri par insertion
- [ ] Tri fusion
- [ ] Tri par sélection



\newpage

## Parcours séquentiels

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 10
- [ ] 3
- [ ] 0

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>
- [ ] <code>False</code>
- [ ] On ne peut pas savoir

## Tris 

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme séquentiel
- [ ] algorithme par insertion
- [ ] algorithme préférentiel
- [ ] algorithme par sélection

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>

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



- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

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



- [ ] Tri par sélection
- [ ] Tri à bulles
- [ ] Tri par insertion
- [ ] Tri fusion



\newpage

## Tris 

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par sélection
- [ ] algorithme séquentiel
- [ ] algorithme par insertion
- [ ] algorithme préférentiel

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



- [ ] Tri fusion
- [ ] Tri à bulles
- [ ] Tri par sélection
- [ ] Tri par insertion

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>

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



- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

## Parcours séquentiels

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>
- [ ] On ne peut pas savoir
- [ ] <code>False</code>

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 0
- [ ] 3
- [ ] 10
- [ ] 2

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.



\newpage

## Tris 

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par sélection
- [ ] algorithme par insertion
- [ ] algorithme séquentiel
- [ ] algorithme préférentiel

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



- [ ] Tri par sélection
- [ ] Tri fusion
- [ ] Tri à bulles
- [ ] Tri par insertion

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



- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] La valeur du plus grand élément de la liste passée en paramètre

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau)</code>

## Parcours séquentiels

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.

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




- [ ] On ne peut pas savoir
- [ ] <code>True</code>
- [ ] <code>False</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 3
- [ ] 0
- [ ] 10



\newpage

## Tris 

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme séquentiel
- [ ] algorithme préférentiel
- [ ] algorithme par sélection
- [ ] algorithme par insertion

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



- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] La valeur du plus grand élément de la liste passée en paramètre

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>

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



- [ ] Tri à bulles
- [ ] Tri fusion
- [ ] Tri par sélection
- [ ] Tri par insertion

## Parcours séquentiels

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 10
- [ ] 3
- [ ] 0

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.

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




- [ ] <code>False</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] On ne peut pas savoir
- [ ] <code>True</code>



\newpage

## Tris 

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau) + 1</code>

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



- [ ] Tri par sélection
- [ ] Tri par insertion
- [ ] Tri à bulles
- [ ] Tri fusion

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



- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus grand élément de la liste passée en paramètre

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme préférentiel
- [ ] algorithme par sélection
- [ ] algorithme par insertion
- [ ] algorithme séquentiel

## Parcours séquentiels

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>False</code>
- [ ] On ne peut pas savoir
- [ ] <code>True</code>

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 3
- [ ] 0
- [ ] 2
- [ ] 10

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.



\newpage

## Tris 

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



- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau)</code>

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme préférentiel
- [ ] algorithme séquentiel
- [ ] algorithme par sélection
- [ ] algorithme par insertion

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



- [ ] Tri par sélection
- [ ] Tri fusion
- [ ] Tri par insertion
- [ ] Tri à bulles

## Parcours séquentiels

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 0
- [ ] 2
- [ ] 3
- [ ] 10

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
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




- [ ] <code>False</code>
- [ ] On ne peut pas savoir
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>True</code>



\newpage

## Parcours séquentiels

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




- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>False</code>
- [ ] On ne peut pas savoir
- [ ] <code>True</code>

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 2
- [ ] 3
- [ ] 0
- [ ] 10

## Tris 

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par sélection
- [ ] algorithme par insertion
- [ ] algorithme préférentiel
- [ ] algorithme séquentiel

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



- [ ] Tri par sélection
- [ ] Tri fusion
- [ ] Tri par insertion
- [ ] Tri à bulles

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>

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



- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre



\newpage

## Tris 

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



- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] La valeur du plus petit élément de la liste passée en paramètre.

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



- [ ] Tri fusion
- [ ] Tri par insertion
- [ ] Tri par sélection
- [ ] Tri à bulles

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 0 et <code>len(tableau) + 1</code>

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme par sélection
- [ ] algorithme préférentiel
- [ ] algorithme séquentiel
- [ ] algorithme par insertion

## Parcours séquentiels

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 3
- [ ] 2
- [ ] 10
- [ ] 0

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




- [ ] On ne peut pas savoir
- [ ] <code>True</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>False</code>



\newpage

## Parcours séquentiels

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




- [ ] On ne peut pas savoir
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] <code>False</code>
- [ ] <code>True</code>

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 0
- [ ] 10
- [ ] 3
- [ ] 2

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] On ne peut pas savoir, tout dépend de l'endroit où est le maximum.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.

## Tris 

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



- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme préférentiel
- [ ] algorithme séquentiel
- [ ] algorithme par sélection
- [ ] algorithme par insertion

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



- [ ] Tri par sélection
- [ ] Tri par insertion
- [ ] Tri à bulles
- [ ] Tri fusion

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>



\newpage

## Parcours séquentiels

### Un algorithme cherche la valeur maximale d'une liste non triée de taille n. Combien de temps mettra cet algorithme sur une liste de taille 2n ?




- [ ] Le même temps que sur la liste de taille n si le maximum est dans la première moitié de la liste.
- [ ] On a ajouté n valeurs, l'algorithme mettra donc n fois plus de temps que sur la liste de taille n.
- [ ] Le temps sera simplement doublé par rapport au temps mis sur la liste de taille n.
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




- [ ] <code>True</code>
- [ ] <code>[1, 2, 3, 7, 10]</code>
- [ ] On ne peut pas savoir
- [ ] <code>False</code>

### Quelle est la valeur de c à la fin de l'exécution du code suivant :


```python
L = [1,2,3,4,1,2,3,4,0,2]
c = 0
for k in L:
    if k == L[1]:
        c = c+1
```



- [ ] 0
- [ ] 10
- [ ] 2
- [ ] 3

## Tris 

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



- [ ] Tri à bulles
- [ ] Tri par sélection
- [ ] Tri fusion
- [ ] Tri par insertion

### Soit un tableau à trier: <code>[56, 22, 14, 5, 35]</code>. Quel algorithme a trié ce tableau ?


Après chaque tour de la boucle principale, les étapes de tri sont les suivantes  :

|    |    |    |    |    |
|----|----|----|----|----|
| 56 | 22 | 14 | 5  | 35 |
| 22 | 56 | 14 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 14 | 22 | 56 | 5  | 35 |
| 5  | 14 | 22 | 56 | 35 |
| 5  | 14 | 22 | 35 | 56 |





- [ ] algorithme séquentiel
- [ ] algorithme préférentiel
- [ ] algorithme par sélection
- [ ] algorithme par insertion

### La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ? :


```python
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```



- [ ] 0 et <code>len(tableau) + 1</code>
- [ ] 1 et <code>len(tableau)</code>
- [ ] 0 et <code>len(tableau)</code>
- [ ] 1 et <code>len(tableau) + 1</code>

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



- [ ] La valeur du plus petit élément de la liste passée en paramètre.
- [ ] La valeur du plus grand élément de la liste passée en paramètre
- [ ] Une valeur booléenne indiquant si la liste liste passée en paramètre est triée
- [ ] Une valeur booléenne indiquant si la liste passée en paramètre contient plusieurs fois le même élément



\newpage

