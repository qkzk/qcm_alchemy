Sujets de l'épreuve pratique NSI 2022
=====================================

## Sujet 1

**EXERCICE 1 (4 points)**

Écrire une fonction `recherche` qui prend en paramètres `caractere`, un caractère, et `mot`, une chaîne de caractères, et qui renvoie le nombre d’occurrences de caractere
dans mot, c’est-à-dire le nombre de fois où caractere apparaît dans mot.

Exemples :
```python
>>> recherche('e', "sciences")
2
>>> recherche('i',"mississippi")
4
>>> recherche('a',"mississippi")
0
```

**EXERCICE 2 (4 points)**

On s’intéresse à un algorithme récursif qui permet de rendre la monnaie à partir d’une liste donnée de valeurs de pièces et de billets - le système monétaire est donné sous
forme d’une liste `pieces=[100, 50, 20, 10, 5, 2, 1]`  (on supposera qu’il n’y a
pas de limitation quant à leur nombre), on cherche à donner la liste de pièces à rendre
pour une somme donnée en argument.
Compléter le code Python ci-dessous de la fonction `rendu_glouton` qui implémente cet
algorithme et renvoie la liste des pièces à rendre

```python
Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
    return ...
    p = pieces[i]
    if p <= ... :
        solution.append(...)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, ...)
```


On devra obtenir :

```python
>>>rendu_glouton_r(68,[],0)
[50, 10, 5, 2, 1]
>>>rendu_glouton_r(291,[],0)
[100, 100, 50, 20, 20, 1]
```


# Sujet 2

**EXERCICE 1 (4 points)**

Soit le couple `(note,coefficient)`:
* `note` est un nombre de type flottant (float) compris entre 0 et 20 ;
* `coefficient` est un nombre entier positif.

Les résultats aux évaluations d'un élève sont regroupés dans une liste composée de couples `(note,coefficient)`.

Écrire une fonction `moyenne` qui renvoie la moyenne pondérée de cette liste donnée en paramètre.

Par exemple, l’expression `moyenne([(15,2),(9,1),(12,3)])` devra renvoyer le résultat du calcul suivant :
$\dfrac{2 \times 15 + 1 \times 9+ 3 \times 12}{2+1+3}=12,5$


**EXERCICE 2 (4 points)**

On cherche à déterminer les valeurs du triangle de Pascal. Dans ce tableau de forme
triangulaire, chaque ligne commence et se termine par le nombre 1. Par ailleurs, la valeur
qui occupe une case située à l’intérieur du tableau s’obtient en ajoutant les valeurs des
deux cases situées juste au-dessus, comme l’indique la figure suivante :

```
           1
         1   1
       1   2   1
     1   3   **3**   **1**
   1   4   6   **4**   1
 1   5  10  10   5   1
```

Compléter la fonction `pascal` ci-après. Elle doit renvoyer une liste correspondant au triangle de Pascal de la ligne 1 à la ligne `n` où `n` est un nombre entier supérieur ou égal à 2 (le tableau sera contenu dans la variable `C`). La variable `Ck` doit, quant à elle, contenir, à l’étape numéro `k`, la k-ième ligne du tableau.



```python
def pascal(n):
    C= [[1]]
    for k in range(1,...):
        Ck = [...]
        for i in range(1,k):
            Ck.append(C[...][i-1]+C[...][...] )
        Ck.append(...)
        C.append(Ck)
    return C
```

Pour n = 4, voici ce que l’on devra obtenir :


```python
>> pascal(4)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```



Et pour n = 5, voici ce que l’on devra obtenir :

```python
>> pascal(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
```



## Sujet 3

**EXERCICE 1 (4 points)**


Le codage par différence (delta encoding en anglais) permet de compresser un tableau de données en indiquant pour chaque donnée, sa différence avec la précédente (plutôt que la donnée elle-même). On se retrouve alors avec un tableau de données assez petites nécessitant moins de place en mémoire. Cette méthode se révèle efficace lorsque les valeurs consécutives sont proches.

Programmer la fonction `delta` qui prend en paramètre un tableau non vide de nombres entiers et qui renvoie un tableau contenant les valeurs entières compressées à l�aide cette technique.

Exemples :

```python
>>> delta([1000, 800, 802, 1000, 1003])
[1000, -200, 2, 198, 3]
>>> delta([42])
42
```


**EXERCICE 2 (4 points)**

Une expression arithmétique ne comportant que les quatre opérations +, −,×,÷ peut être représentée sous forme d’arbre binaire. Les nœuds internes sont des opérateurs et les feuilles sont des nombres. Dans un tel arbre, la disposition des nœuds joue le rôle des parenthèses que
nous connaissons bien.

En parcourant en profondeur infixe l’arbre binaire ci-contre, on retrouve l’expression notée habituellement :
3 × (8 + 7) − (2 + 1) .

La classe Noeud ci-après permet d’implémenter une structure
d’arbre binaire.

Compléter la fonction récursive `expression_infixe` qui prend
en paramètre un objet de la classe Noeud et qui renvoie
l’expression arithmétique représentée par l’arbre binaire passé en paramètre, sous forme d’une chaîne de caractères contenant des parenthèses.


Résultat attendu avec l’arbre ci-dessus :

```python
>>> e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None),'+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+',Noeud(None, 1, None)))
>>> expression_infixe(e)
'((3*(8+7))-(2+1))'
```



```python
class Noeud:
    '''
    Classe implémentant un noeud d'arbre binaire disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre gauche.
    - droit : le sous-arbre droit.
    '''
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None
    def expression_infixe(e):
        s = ...
        if e.gauche is not None:
            s = s + expression_infixe(...)
            s = s + ...
        if ... is not None:
            s = s + ...
        if ...:
            return s
        return '('+ s +')'
 ```       
        
        
        
        
        
        
        
        
## Sujet 4

**EXERCICE 1 (4 points)**

Écrire une fonction `recherche` qui prend en paramètre un tableau de nombres entiers
`tab`, et qui renve la liste (éventuellement vide) des couples d'entiers consécutifs
successifs qu'il peut y avoir dans `tab`.


Exemples :
```python
>>> recherche([1, 4, 3, 5])
[]
>>> recherche([1, 4, 5, 3])
[(4, 5)]
>>> recherche([7, 1, 2, 5, 3, 4])
[(1, 2), (3, 4)]
>>> recherche([5, 1, 2, 3, 8, -5, -4, 7])
[(1, 2), (2, 3), (-5, -4)]
```


**EXERCICE 2 (4 points)**

Soit une image binaire représentée dans un tableau à 2 dimensions. Les éléments `M[i][j]`, appelés pixels, sont égaux soit à 0 soit à 1.

Une composante d’une image est un sous-ensemble de l’image constitué uniquement de 1 et de 0 qui sont côte à côte, soit horizontalement soit verticalement.

Par exemple, les composantes de M =

sont

On souhaite, à partir d’un pixel égal à 1 dans une image `M`, donner la valeur `val` à tous
les pixels de la composante à laquelle appartient ce pixel.

La fonction `propager` prend pour paramètre une image `M`, deux entiers `i` et `j` et une
valeur entière `val`. Elle met à la valeur `val` tous les pixels de la composante du pixel
`M[i][j]` s’il vaut 1 et ne fait rien s’il vaut 0.

Par exemple, `propager(M,2,1,3)` donne

Compléter le code récursif de la fonction `propager` donné ci-dessous.

```python
def propager(M, i, j, val):
    if M[i][j]== ...:
        return
    M[i][j]=val
    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == ...):
        propager(M, i-1, j, val)
    # l'élément en bas fait partie de la composante
    if ((...) < len(M) and M[i+1][j] == 1):
        propager(M, ..., j, val)
    # l'élément à gauche fait partie de la composante
    if ((...) >= 0 and M[i][j-1] == 1):
        propager(M, i, ..., val)
    # l'élément à droite fait partie de la composante
    if ((...) < len(M) and M[i][j+1] == 1):
        propager(M, i, ..., val)
```


Exemple :
```python
>>> M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]
>>> propager(M,2,1,3)
>>> M
[[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
```




## Sujet 5

**EXERCICE 1 (4 points)**

Écrire une fonction `RechercheMinMax` qui prend en paramètre un tableau de nombres
non triés `tab`, et qui renvoie la plus petite et la plus grande valeur du tableau sous la
forme d’un dictionnaire à deux clés `'min'` et `'max'`. Les tableaux seront représentés sous
forme de liste Python.

Exemples :

```python
>>> tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
>>> resultat = rechercheMinMax(tableau)
>>> resultat
{'min': -2, 'max': 9}
>>> tableau = []
>>> resultat = rechercheMinMax(tableau)
>>> resultat
{'min': None, 'max': None}
```


**EXERCICE 2 (4 points)**

On dispose d’un programme permettant de créer un objet de type `PaquetDeCarte`,
selon les éléments indiqués dans le code ci-dessous.

Compléter ce code aux endroits indiqués par #A compléter, puis ajouter des assertions dans l’initialiseur de `Carte`, ainsi que dans la méthode `getCarteAt()`.

```python
class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v
    """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"
    """Renvoie la couleur de la Carte (parmi pique, coeur,
carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur - 1]
        
        
class PaquetDeCarte:
    def __init__(self):
        self.contenu = []
    """Remplit le paquet de cartes"""
    def remplir(self):
        #A compléter
    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        #A compléter
```

Exemple :

```python
>>> unPaquet = PaquetDeCarte()
>>> unPaquet.remplir()
>>> uneCarte = unPaquet.getCarteAt(20)
>>> print(uneCarte.getNom() + " de " + uneCarte.getCouleur())
6 de coeur
```



## Sujet 6

**EXERCICE 1 (4 points)**

Écrire une fonction `maxi` qui prend en paramètre une liste `tab` de nombres entiers et qui
renvoie un couple donnant le plus grand élément de cette liste ainsi que l’indice de la
première apparition de ce maximum dans la liste.


Exemple :

```python
>>> maxi([1,5,6,9,1,2,3,7,9,8])
(9,3)
```


**EXERCICE 2 (4 points)**

La fonction `recherche` prend en paramètres deux chaines de caractères `gene` et
`seq_adn` et renvoie `True` si on retrouve `gene` dans `seq_adn` et `False` sinon.

Compléter le code Python ci-dessous pour qu’il implémente la fonction recherche.

```python
def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = ...
    trouve = False
    while i < ... and trouve == ... :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            ...
        if j == g:
            trouve = True
        ...
    return trouve
```

Exemples :

```python
>>> recherche("AATC", "GTACAAATCTTGCC")
True
>>> recherche("AGTC", "GTACAAATCTTGCC")
False
```



## Sujet 7


**EXERCICE 1 (4 points)**


Écrire une fonction `conv_bin` qui prend en paramètre un entier positif `n` et renvoie un couple `(b,bit)` où :

* `b` est une liste d'entiers correspondant à la représentation binaire de `n`;
* `bit` correspond aux nombre de bits qui constituent `b`.

Exemple :
```python
>>> conv_bin(9)
([1,0,0,1],4)

```

Aide :
* l'opérateur `//` donne le quotient de la division euclidienne : `5//2` donne `2` ;
* l'opérateur `%` donne le reste de la division euclidienne : `5%2` donne `1` ;
* `append` est une méthode qui ajoute un élément à une liste existante :
  Soit `T=[5,2,4]`, alors `T.append(10)` ajoute `10` à la liste `T`. Ainsi, `T` devient `[5,2,4,10]`.


* `reverse` est une méthode qui renverse les éléments d'une liste.
  Soit `T=[5,2,4,10]`. Après `T.reverse()`, la liste devient `[10,4,2,5]`.
  
On remarquera qu’on récupère la représentation binaire d’un entier `n` en partant de la
gauche en appliquant successivement les instructions :

```python
b = n%2
n = n//2
```

répétées autant que nécessaire.



**EXERCICE 2 (4 points)**

La fonction `tri_bulles` prend en paramètre une liste `T` d’entiers non triés et renvoie la
liste triée par ordre croissant.

Compléter le code Python ci-dessous qui implémente la fonction `tri_bulles`.

```python
def tri_bulles(T):
    n = len(T)
    for i in range(...,...,-1):
        for j in range(i):
            if T[j] > T[...]:
                ... = T[j]
                T[j] = T[...]
                T[j+1] = temp
    return T
```


## Sujet 8

**EXERCICE 1 (4 points)**

Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre entier et `tab`
un tableau de nombres entiers, et qui renvoie l’indice de la première occurrence de `elt`
dans `tab` si `elt` est dans `tab` et `-1` sinon.

Exemples :

```python
>>> recherche(1, [2, 3, 4])
-1
>>> recherche(1, [10, 12, 1, 56])
2
>>> recherche(50, [1, 50, 1])
1
>>> recherche(15, [8, 9, 10, 15])
3
```

**EXERCICE 2 (4 points)**

On considère la fonction `insere` ci-dessous qui prend en argument un entier `a` et un tableau `tab` d'entiers triés par ordre croissant. Cette fonction insère la valeur `a` dans le tableau et renvoie le nouveau tableau. Les tableaux seront représentés sous la forme de listes python.

```python
def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = ...
    while a < ... and i >= 0:
        l[i+1] = ...
        l[i] = a
        i = ...
    return l
```
    

Compléter la fonction `insere` ci-dessus.

Exemples :

```python
>>> insere(3,[1,2,4,5])
[1, 2, 3, 4, 5]
>>> insere(10,[1,2,7,12,14,25])
[1, 2, 7, 10, 12, 14, 25]
>>> insere(1,[2,3,4])
[1, 2, 3, 4]
```



## Sujet 9

**EXERCICE 1 (4 points)**

Soit un nombre entier supérieur ou égal à 1 :
* s'il est pair, on le divise par 2 ;
* s’il est impair, on le multiplie par 3 et on ajoute 1.

Puis on recommence ces étapes avec le nombre entier obtenu, jusqu’à ce que l’on obtienne la valeur 1.

On définit ainsi la suite $(u_n)$ par
* $u_0 = k$ , où $k$ est un entier choisi initialement ;
* $u_{n+1}=u_n/2$ si $u_n$ est pair ;
  $u_{n+1} = 3\times u_n + 1$ si $u_n$ est impair.
  
On admet que, quel que soit l’entier $k$ choisi au départ, la suite finit toujours sur la valeur 1.

Écrire une fonction `calcul` prenant en paramètres un entier `n` strictement positif et qui
renvoie la liste des valeurs $u_n$ , en partant de $n$ et jusqu’à atteindre 1.

Exemple :
```python
>>> calcul(7)
[7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```


**EXERCICE 2 (4 points)**

On affecte à chaque lettre de l’alphabet un code selon les tableaux ci-dessous :

|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|

Pour un mot donné, on détermine d’une part son code alphabétique concaténé, obtenu
par la juxtaposition des codes de chacun de ses caractères, et d’autre part, son code
additionné, qui est la somme des codes de chacun de ses caractères.
Par ailleurs, on dit que ce mot est « parfait » si le code additionné divise le code concaténé.

Exemples :
* Pour le mot "PAUL", le code concaténé est la chaîne 1612112, soit l’entier1 612 112.
  Son code additionné est l’entier 50 car 16 + 1 + 21 + 12=50.
  50 ne divise pas l’entier 1 612 112 ; par conséquent, le mot "PAUL" n’est pas parfait.
* Pour le mot "ALAIN", le code concaténé est la chaîne 1121914, soit l’entier 1 121 914.
  Le code additionné est l’entier 37 car 1 + 12 + 1 + 9 + 14 = 37.
  37 divise l’entier 1 121 914 ; par conséquent, le mot "ALAIN" est parfait.

Compléter la fonction `est_parfait` ci-dessous qui prend comme argument une chaîne de caractères `mot` (en lettres majuscules) et qui renvoie le code alphabétique concaténé,
le code additionné de mot, ainsi qu’un booléen qui indique si mot est parfait ou pas.

```python
dico = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, \
"H":8, "I":9, "J":10, "K":11, "L":12, "M":13, \
"N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, \
"T":20, "U":21,"V":22, "W":23, "X":24, "Y":25, "Z":26}

def est_parfait(mot) :
    #mot est une chaîne de caractères (en lettres majuscules)
    code_c = ""
    code_a = ???
    for c in mot :
        code_c = code_c + ???
        code_a = ???
    code_c = int(code_c)
    if ??? :
        mot_est_parfait = True
    else :
        mot_est_parfait = False
    return [code_a, code_c, mot_est_parfait]
```

Exemples :

```python
>>> est_parfait("PAUL")
[50, 1612112, False]
>>> est_parfait("ALAIN")
[37, 1121914, True]
```

## Sujet 10

**EXERCICE 1 (4 points)**

L’occurrence d’un caractère dans un phrase est le nombre de fois où ce caractère est présent.

Exemples :
* l’occurrence du caractère ‘o’ dans ‘bonjour’ est 2 ;
* l’occurrence du caractère ‘b’ dans ‘Bébé’ est 1 ;
* l’occurrence du caractère ‘B’ dans ‘Bébé’ est 1 ;
* l’occurrence du caractère ‘ ‘ dans ‘Hello world !’ est 2.

On cherche les occurrences des caractères dans une phrase. On souhaite stocker ces occurrences dans un dictionnaire dont les clefs seraient les caractères de la phrase et les valeurs l’occurrence de ces caractères.

Par exemple : avec la phrase `'Hello world !'` le dictionnaire est le suivant :

`{'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}`

(l’ordre des clefs n’ayant pas d’importance).


Écrire une fonction `occurence_lettres` prenant comme paramètre une variable `phrase` de type `str`. Cette fonction doit renvoyer un dictionnaire constitué des
occurrences des caractères présents dans la phrase.


**EXERCICE 2 (4 points)**

La fonction `fusion` prend deux listes `L1`, `L2` d’entiers triées par ordre croissant et les fusionne en une liste triée `L12` qu’elle renvoie.

Le code Python de la fonction est

```python
def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and ... :
        if L1[i1] < L2[i2]:
            L12[i] = ...
            i1 = ...
        else:
            L12[i] = L2[i2]
            i2 = ...
        i += 1
    while i1 < n1:
        L12[i] = ...
        i1 = i1 + 1
        i = ...
    while i2 < n2:
        L12[i] = ...
        i2 = i2 + 1
        i = ...
    return L12
```

Compléter le code.

Exemple :
```python
>>> fusion([1,6,10],[0,7,8,9])
[0, 1, 6, 7, 8, 9, 10]
```








## Sujet 11


**EXERCICE 1 (4 points)**

Écrire une fonction `recherche` qui prend en paramètres un tableau `tab` de nombres entiers triés par ordre croissant et un nombre entier `n`, et qui effectue une recherche
dichotomique du nombre entier `n` dans le tableau non vide `tab`.

Cette fonction doit renvoyer un indice correspondant au nombre cherché s’il est dans le tableau, `-1` sinon.

Exemples:
```python
>>> recherche([2, 3, 4, 5, 6], 5)
3
>>> recherche([2, 3, 4, 6, 7], 5)
-1
```

**EXERCICE 2 (4 points)**

Le codage de César transforme un message en changeant chaque lettre en la décalant dans l’alphabet.

Par exemple, avec un décalage de 3, le A se transforme en D, le B en E, ..., le X en A, le Y en B et le Z en C. Les autres caractères (‘!’,’ ?’…) ne sont pas codés.

La fonction `position_alphabet` ci-dessous prend en paramètre un caractère `lettre`
et renvoie la position de `lettre` dans la chaîne de caractères `ALPHABET` s’il s’y trouve
et `-1` sinon.

La fonction `cesar` prend en paramètre une chaîne de caractères `message` et un nombre entier `decalage` et renvoie le nouveau message codé avec le codage de César utilisant le décalage `decalage`.

```python
ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for ... in message :
        if lettre in ALPHABET :
            indice = ( ... )%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = ...
    return resultat
```


Compléter la fonction cesar.

Exemples :
```python
>>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4)
'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
>>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5)
'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
```

## Sujet 12

**EXERCICE 1 (4 points)**


Programmer la fonction `moyenne` prenant en paramètre un tableau d'entiers `tab` (type `list`) qui renvoie la moyenne de ses éléments si le tableau est non vide et affiche `'erreur'` si le tableau est vide.


Exemples :
```python
>>> moyenne([5,3,8])
5.333333333333333
>>> moyenne([1,2,3,4,5,6,7,8,9,10])
5.5
>>> moyenne([])
'erreur'
```

**EXERCICE 2 (4 points)**

On considère un tableau d'entiers `tab` (type `list` dont les éléments sont des 0 ou des 1). On se propose de trier ce tableau selon l'algorithme suivant : à chaque étape du tri, le tableau est constitué de trois zones consécutives, la première ne contenant que des 0, la seconde n'étant pas triée et la dernière ne contenant que des 1.


|Zone de 0|Zone non triée|Zone de 1|
|---------|--------------|---------|


Tant que la zone non triée n'est pas réduite à un seul élément, on regarde son premier élément :
* si cet élément vaut 0, on considère qu'il appartient désormais à la zone ne contenant que des 0 ;
* si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on considère alors qu’il appartient à la zone ne contenant que des 1.

Dans tous les cas, la longueur de la zone non triée diminue de 1.

Recopier sous Python en la complétant la fonction `tri` suivante :

```python
def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice.
    #Au debut, la zone non triee est le tableau entier.
    i= ...
    j= ...
    while i != j :
        if tab[i]== 0:
            i= ...
        else :
            valeur = tab[j]
            tab[j] = ...
            ...
            j= ...
    ...
```

Exemple :

```python
>>> tri([0,1,0,1,0,1,0,1,0])
[0, 0, 0, 0, 0, 1, 1, 1, 1]
```



## Sujet 13

**EXERCICE 1 (4 points)**

On s’intéresse au problème du rendu de monnaie. On suppose qu’on dispose d’un nombre infini de billets de 5 euros, de pièces de 2 euros et de pièces de 1 euro.

Le but est d’écrire une fonction nommée `rendu` dont le paramètre est un entier positif non
nul `somme_a_rendre` et qui retourne une liste de trois entiers `n1`, `n2` et `n3` qui
correspondent aux nombres de billets de 5 euros (`n1`) de pièces de 2 euros (`n2`) et de
pièces de 1 euro (`n3`) à rendre afin que le total rendu soit égal à `somme_a_rendre`.

On utilisera un algorithme glouton : on commencera par rendre le nombre maximal de
billets de 5 euros, puis celui des pièces de 2 euros et enfin celui des pièces de 1 euros.

Exemples :
```python
>>> rendu(13)
[2,1,1]
>>> rendu(64)
[12,2,0]
>>> rendu(89)
[17,2,0]
```


**EXERCICE 2 (4 points)**

On veut écrire une classe pour gérer une file à l’aide d’une liste chaînée. On dispose d’une classe `Maillon` permettant la création d’un maillon de la chaîne, celui-ci étant constitué d’une valeur et d’une référence au maillon suivant de la chaîne :

```python
class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None
```

Compléter la classe `File` suivante où l’attribut `dernier_file` contient le maillon correspondant à l’élément arrivé en dernier dans la file :

```python
class File :
    def __init__(self) :
        self.dernier_file = None
    def enfile(self,element) :
        nouveau_maillon = Maillon(...)
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = ...
    def est_vide(self) :
        return self.dernier_file == None
    def affiche(self) :
        maillon = self.dernier_file
        while maillon != ... :
            print(maillon.valeur)
            maillon = ...
    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = ...
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = ...
            maillon.suivant = None
            return resultat
        return None
```


On pourra tester le fonctionnement de la classe en utilisant les commandes suivantes dans la console Python :
```python
>>> F = File()
>>> F.est_vide()
True
>>> F.enfile(2)
>>> F.affiche()
2
>>> F.est_vide()
False
>>> F.enfile(5)
>>> F.enfile(7)
>>> F.affiche()
7
5
2
>>> F.defile()
2
>>> F.defile()
5
>>> F.affiche()
7
```





## Sujet 14

**EXERCICE 1 (4 points)**


On considère des mots à trous : ce sont des chaînes de caractères contenant uniquement des majuscules et des caractères `'*'`. Par exemple `'INFO*MA*IQUE'`, `'***I***E**'` et `'*S*'` sont des mots à trous.

Programmer une fonction `correspond` qui :
* prend en paramètres deux chaînes de caractères `mot` et `mot_a_trous` où `mot_a_trous` est un mot à trous comme indiqué ci-dessus,
* renvoie :
    * `True` si on peut obtenir mot en remplaçant convenablement les caractères `'*'` de `mot_a_trous`.
    * `False` sinon.
    
    
Exemples :
```python
>>> correspond('INFORMATIQUE', 'INFO*MA*IQUE')
True
>>> correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
False
```



**EXERCICE 2 (4 points)**

On considère au plus 26 personnes A, B, C, D, E, F ... qui peuvent s'envoyer des messages avec deux règles à respecter :
* chaque personne ne peut envoyer des messages qu'à la même personne (éventuellement elle-même),
* chaque personne ne peut recevoir des messages qu'en provenance d'une seule personne (éventuellement elle-même).

Voici un exemple - avec 6 personnes - de « plan d'envoi des messages » qui respecte les règles ci-dessus, puisque chaque personne est présente une seule fois dans chaque colonne :

* A envoie ses messages à E
* E envoie ses messages à B
* B envoie ses messages à F
* F envoie ses messages à A
* C envoie ses messages à D
* D envoie ses messages à C

Et le dictionnaire correspondant à ce plan d'envoi est le suivant :
`plan_a = {'A':'E', 'B':'F', 'C':'D', 'D':'C', 'E':'B', 'F':'A'}`

Sur le plan d'envoi `plan_a` des messages ci-dessus, il y a deux cycles distincts : un premier
cycle avec A, E, B, F et un second cycle avec C et D.

En revanche, le plan d’envoi `plan_b` ci-dessous :
`plan_b = {'A':'C', 'B':'F', 'C':'E', 'D':'A', 'E':'B', 'F':'D'}`
comporte un unique cycle : A, C, E, B, F, D. Dans ce cas, lorsqu’un plan d’envoi comporte un
unique cycle, on dit que le plan d’envoi est cyclique.


Pour savoir si un plan d'envoi de messages comportant `N` personnes est cyclique, on peut utiliser l'algorithme ci-dessous :

On part de la personne `A` et on inspecte les `N – 1` successeurs dans le plan d'envoi :
* Si un de ces `N – 1` successeurs est `A` lui-même, on a trouvé un cycle de taille inférieure ou égale à `N – 1`. Il y a donc au moins deux cycles et le plan d'envoi n'est
pas cyclique.
* Si on ne retombe pas sur `A` lors de cette inspection, on a un unique cycle qui passe par toutes les personnes : le plan d'envoi est cyclique.


Compléter la fonction suivante en respectant la spécification.

Remarque : la fonction python `len` permet d'obtenir la longueur d'un dictionnaire.

```python
def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire plan correspondant
    à un plan d'envoi de messages entre N personnes A, B, C,
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon.
    '''
    personne = 'A'
    N = len(...)
    for i in range(...):
        if plan[...] == ...:
            return ...
        else:
            personne = ...
    return ...
```

Exemples :
```python
>>> est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'})
False
>>> est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'})
True
>>> est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'})
True
>>> est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'})
False
```

## Sujet 15

**EXERCICE 1 (4 points)**


Écrire une fonction python appelée `nb_repetitions` qui prend en paramètres un
élément `elt` et une liste `tab` et renvoie le nombre de fois où l’élément apparaît dans la
liste.

Exemples :
```python
>>> nb_repetitions(5,[2,5,3,5,6,9,5])
3
>>> nb_repetitions('A',[ 'B', 'A', 'B', 'A', 'R'])
2
>>> nb_repetitions(12,[1, '! ',7,21,36,44])
0
```

**EXERCICE 2 (4 points)**

Pour rappel, la conversion d’un nombre entier positif en binaire peut s’effectuer à l’aide des divisions successives comme illustré ici :


Voici une fonction python basée sur la méthode des divisions successives permettant de convertir un nombre entier positif en binaire :

```python
def binaire(a):
    bin_a = str(...)
    a = a // 2
    while a ... :
        bin_a = ...(a%2) + ...
        a = ...
    return bin_a
```

Compléter la fonction binaire.

Exemples :

```python
>>> binaire(0)
'0'
>>> binaire(77)
'1001101'
```

## Sujet 16

**EXERCICE 1 (4 points)**

Écrire une fonction `maxi` qui prend en paramètre une liste `tab` de nombres entiers et renvoie un couple donnant le plus grand élément de cette liste, ainsi que l’indice de la
première apparition de ce maximum dans la liste.

Exemple :
```python
>>> maxi([1,5,6,9,1,2,3,7,9,8])
(9,3)
```

**EXERCICE 2 (4 points)**

Cet exercice utilise des piles qui seront représentées en Python par des listes (type `list`).

On rappelle que l’expression `T1 = list(T)` fait une copie de `T` indépendante de `T`, que l’expression `x = T.pop()` enlève le sommet de la pile `T` et le place dans la variable `x` et, enfin, que l’expression `T.append(v)` place la valeur `v` au sommet de la pile `T`.

Compléter le code Python de la fonction `positif` ci-dessous qui prend une pile `T` de
nombres entiers en paramètre et qui renvoie la pile des entiers positifs dans le même
ordre, sans modifier la variable `T`.


```python
def positif(T):
    T2 = ...(T)
    T3 = ...
    while T2 != []:
        x = ...
        if ... >= 0:
            T3.append(...)
            T2 = []
    while T3 != ...:
        x = T3.pop()
        ...
    print('T = ',T)
    return T2
```

Exemple :
```python
>>> positif([-1,0,5,-3,4,-6,10,9,-8 ])
T = [-1, 0, 5, -3, 4, -6, 10, 9, -8]
[0, 5, 4, 10, 9]
```


## Sujet 17

**Exercice 1 (4 points)**

Pour cet exercice :
* On appelle « mot » une chaîne de caractères composée avec des caractères choisis
parmi les 26 lettres minuscules ou majuscules de l'alphabet,
* On appelle « phrase » une chaîne de caractères :
    o composée avec un ou plusieurs « mots » séparés entre eux par un seul caractère espace ' ',
    o se finissant :
        - soit par un point '.' qui est alors collé au dernier mot,
        - soit par un point d'exclamation '!' ou d'interrogation '?' qui est alors séparé du dernier mot par un seul caractère espace ' '.
        
Voici quatre exemples de phrases :

* 'Le point d exclamation est separe !'
* 'Il y a un seul espace entre les mots !'
* 'Le point final est colle au dernier mot.'
* 'Gilbouze macarbi acra cor ed filbuzine ?'

Après avoir remarqué le lien entre le nombre de mots et le nombres de caractères espace dans une phrase, programmer une fonction `nombre_de_mots` qui prend en paramètre une phrase et renvoie le nombre de mots présents dans cette phrase.

Exemples :
```python
>>> nombre_de_mots('Le point d exclamation est separe !')
6
>>> nombre_de_mots('Il y a un seul espace entre les mots !')
9
```

**Exercice 2 (4 points)**

La classe `ABR` ci-dessous permet d'implémenter une structure d'arbre binaire de recherche.

```python
class Noeud:
    ''' Classe implémentant un noeud d'arbre binaire
    disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre gauche.
    - droit : le sous-arbre droit. '''
    def __init__(self, v, g, d):
        self.valeur = v
        self.gauche = g
        self.droite = d

class ABR:
    ''' Classe implémentant une structure
    d'arbre binaire de recherche. '''
    def __init__(self):
        '''Crée un arbre binaire de recherche vide'''
        self.racine = None
    def est_vide(self):
        '''Renvoie True si l'ABR est vide et False sinon.'''
        return self.racine is None
    def parcours(self, tab = []):
        ''' Renvoie la liste tab complétée avec tous les
        éléments de l'ABR triés par ordre croissant. '''
        if self.est_vide():
            return tab
        else:
            self.racine.gauche.parcours(tab)
            tab.append(...)
            ...
            return tab
    def insere(self, element):
        '''Insère un élément dans l'arbre binaire de recherche.'''
        if self.est_vide():
            self.racine = Noeud(element, ABR(), ABR())
        else:
            if element < self.racine.valeur:
                self.racine.gauche.insere(element)
            else :
                self.racine.droite.insere(element)
    def recherche(self, element):
        '''
        Renvoie True si element est présent dans l'arbre
        binaire et False sinon.
        '''
        if self.est_vide():
            return ...
        else:
            if element < self.racine.valeur:
                return ...
            elif element > self.racine.valeur:
                return ...
            else:
                return ...
```

Compléter les fonctions récursives parcours et recherche afin qu'elles respectent leurs spécifications.

Voici un exemple d'utilisation :
```python
>>> a = ABR()
>>> a.insere(7)
>>> a.insere(3)
>>> a.insere(9)
>>> a.insere(1)
>>> a.insere(9)
>>> a.parcours()
[1, 3, 7, 9, 9]
>>> a.recherche(4)
False
>>> a.recherche(3)
True
```




## Sujet 18

**EXERCICE 1 (4 points)**


On a relevé les valeurs moyennes annuelles des températures à Paris pour la période allant de 2013 à 2019. Les résultats ont été récupérés sous la forme de deux listes : l’une pour les températures, l’autre pour les années :

```python
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
```

Écrire la fonction `mini` qui prend en paramètres le tableau `releve` des relevés et le tableau `date` des dates et qui renvoie la plus petite valeur relevée au cours de la
période et l’année correspondante.

Exemple :

```python
>>> mini(t_moy, annees)
12.5, 2016
```


**EXERCICE 2 (4 points)**

Un mot palindrome peut se lire de la même façon de gauche à droite ou de droite à gauche : bob, radar, et non sont des mots palindromes.

De même certains nombres sont eux aussi des palindromes : 33, 121, 345543.


L’objectif de cet exercice est d’obtenir un programme Python permettant de tester si un nombre est un nombre palindrome.
Pour remplir cette tâche, on vous demande de compléter le code des trois fonctions ci-dessous sachant que la fonction `est_nbre_palindrome` s’appuiera sur la fonction `est_palindrome` qui elle-même s’appuiera sur la fonction `inverse_chaine`.

La fonction `inverse_chaine` inverse l'ordre des caractères d'une chaîne de caractères `chaine` et renvoie la chaîne inversée.

La fonction `est_palindrome` teste si une chaine de caractères `chaine` est un palindrome. Elle renvoie `True` si c’est le cas et `False` sinon. Cette fonction s’appuie sur la fonction précédente.

La fonction `est_nbre_palindrome` teste si un nombre `nbre` est un palindrome. Elle renvoie `True` si c’est le cas et `False` sinon. Cette fonction s’appuie sur la fonction
précédente.

Compléter le code des trois fonctions ci-dessous.

```python
def inverse_chaine(chaine):
    result = ...
    for caractere in chaine:
        result = ...
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return ...

def est_nbre_palindrome(nbre):
    chaine = ...
    return est_palindrome(chaine)
```

Exemples :
```python
>>> inverse_chaine('bac')
'cab'
>>> est_palindrome('NSI')
False
>>> est_palindrome('ISN-NSI')
True
>>>est_nbre_palindrome(214312)
False
>>>est_nbre_palindrome(213312)
True
```


## Sujet 19

**EXERCICE 1 (4 points)**

Programmer la fonction multiplication prenant en paramètres deux nombres entiers `n1` et `n2`, et qui renvoie le produit de ces deux nombres.

Les seules opérations autorisées sont l’addition et la soustraction.

Exemples :
```python
>>> multiplication(3,5)
15
>>> multiplication(-4,-8)
32
>>> multiplication(-2,6)
-12
>>> multiplication(-2,0)
0
```


**EXERCICE 2 (4 points)**

Soit `T` un tableau non vide d'entiers triés dans l'ordre croissant et `n` un entier.

La fonction `chercher` doit renvoyer un indice où la valeur `n` apparaît éventuellement dans `T`, et `None` sinon.

Les paramètres de la fonction sont :
* `T`, le tableau dans lequel s'effectue la recherche ;
* `n`, l'entier à chercher dans le tableau ;
* `i`, l'indice de début de la partie du tableau où s'effectue la recherche ;
* `j`, l'indice de fin de la partie du tableau où s'effectue la recherche.

La fonction `chercher` est une fonction récursive basée sur le principe « diviser pour régner ».

Le code de la fonction commence par vérifier si `0 <= i` et `j < len(T)`. Si cette
condition n’est pas vérifiée, elle affiche `"Erreur"` puis renvoie `None`.

Recopier et compléter le code de la fonction `chercher` proposée ci-dessous :

```python
def chercher(T,n,i,j):
    if i < 0 or ??? :
        print("Erreur")
        return None
    if i > j :
        return None
    m = (i+j) // ???
    if T[m] < ??? :
        return chercher(T, n, ??? , ???)
    elif ??? :
        return chercher(T, n, ??? , ??? )
    else :
        return ???
```

L’exécution du code doit donner :
```python
>>> chercher([1,5,6,6,9,12],7,0,10)
Erreur
>>> chercher([1,5,6,6,9,12],7,0,5)
>>> chercher([1,5,6,6,9,12],9,0,5)
4
>>> chercher([1,5,6,6,9,12],6,0,5)
2
```

## Sujet 20

**EXERCICE 1 (4 points)**

L'opérateur « ou exclusif » entre deux bits renvoie 0 si les deux bits sont égaux et 1 s'ils sont différents : 0 ⊕ 0 = 0 , 0 ⊕ 1 = 1 , 1 ⊕ 0 = 1 , 1 ⊕ 1 = 0.

On représente ici une suite de bits par un tableau contenant des 0 et des 1.

Exemples :
```python
a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1] 
```

Écrire la fonction `xor` qui prend en paramètres deux tableaux de même longueur et qui renvoie un tableau où l’élément situé à position `i` est le résultat, par l’opérateur « ou exclusif », des éléments à la position `i` des tableaux passés en paramètres.

En considérant les quatre exemples ci-dessus, cette fonction doit passer les tests suivants :

```python
assert(xor(a, b) == [1, 1, 0, 1, 1, 0, 0, 1])
assert(xor(c, d) == [1, 1, 1, 0])
```

**EXERCICE 2 (4 points)**

Dans cet exercice, on appelle carré d’ordre $n$ un tableau de $n$ lignes et $n$ colonnes dont chaque case contient un entier naturel.

Exemples :


Un  carré `c2` d’ordre 2

|1|1|
|-|-|
|1|1|

Un carré `c3` d'ordre 3

|2|9|4|
|-|-|-|
|7|5|3|
|6|1|8|



Un carré `c4` d’ordre 4

|4|5|16|9|
|-|-|-|-|
|14|7|2|11|
|3|10|15|6|
|13|12|8|1|




Un carré est dit magique lorsque les sommes des éléments situés sur chaque ligne, chaque colonne et chaque diagonale sont égales. Ainsi `c2` et `c3` sont magiques car la somme de chaque ligne, chaque colonne et chaque diagonale est égale à 2 pour `c2` et 15 pour `c3`. Par contre `c4` n’est pas magique car la somme de la première ligne est égale à 34 alors que celle de la dernière colonne est égale à 27.

La classe `Carre` ci-après contient des méthodes qui permettent de manipuler des carrés.

Compléter la fonction `est_magique` qui prend en paramètre un carré et qui renvoie la valeur de la somme si ce carré est magique, `False` sinon.

```python
class Carre:
    def __init__(self, tableau = [[]]):
        self.ordre = len(tableau)
        self.valeurs = tableau
    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.valeurs[i])
    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        return sum(self.valeurs[i])
    def somme_col(self, j):
        '''Calcule la somme des valeurs de la colonne j'''
        return sum([self.valeurs[i][j] for i in range(self.ordre)])
    def est_magique(carre):
        n = carre.ordre
        s = carre.somme_ligne(0)
        #test de la somme de chaque ligne
        for i in range(..., ...):
            if carre.somme_ligne(i) != s:
                return ...
        #test de la somme de chaque colonne
        for j in range(n):
            if ... != s:
                return False
        #test de la somme de chaque diagonale
        if sum([carre.valeurs[...][...] for k in range(n)]) != s:
            return False
        if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
            return False
        return ...
```        



Tester la fonction est_magique sur les carrés `c2`, `c3` et `c4`.



�
