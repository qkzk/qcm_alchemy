---
title: "NSI Première - binaires, booléens, boucles, fonctions"
author: "qkzk"
date: "2021/11/02"
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


## Représenter du texte en machine 

### Combien de caractères sont encodés en ASCII ?

- [x] 128
- [ ] autant qu'on le souhaite, il est extensible
- [ ] 256
- [ ] 8

### Combien de bits sont nécessaires pour encoder un caractère en ASCII ?

- [x] 7
- [ ] 32
- [ ] 64
- [ ] 127

### Combien d'octets sont nécessaires pour encoder un caractère en UTF-8 ?

- [x] de 1 à 4
- [ ] 1
- [ ] 4
- [ ] 127

### Un document est enregistré avec l'encodage UTF-8. On l'ouvre avec un autre encodage :

- [x] les caractères non ASCII ne seront surement pas lus correctement
- [ ] l'ensemble du document est illisible
- [ ] l'ensemble du document est toujours lisible
- [ ] il est impossible d'ouvrir le document, le programme plante


## IHM sur le web


### On considère `https://www.service-public.fr/particuliers/vosdroits/`.

Que savons-nous **du protocole employé** ?

- [x] Il est sécurisé
- [ ] On ne peut rien savoir du protocole
- [ ] Il n'est pas sécurisé
- [ ] `service-public` et `.fr` inspirent confiance

### On considère `https://www.service-public.fr/particuliers/vosdroits/`.

Quel est le **domaine** ?

- [x] `service-public.fr`
- [ ] `/particuliers/vosdroits/`
- [ ] `https://`
- [ ] `www`

### `HTML` et `HTTP`

- [x] `HTML` est un langage de description balisé, `HTTP` est un protocole de communication
- [x] `HTTP` est un langage de description balisé, `HTML` est un protocole de communication
- [x] `HTML` et `HTTP` sont des protocoles
- [x] `HTML` et `HTTP` sont des langages

### On considère le code suivant :

```html
<html>
  <head>
    <title>Mon site</title>
  <body>
    <h1>Bienvenue !</h1>
    <a href="https://qkzk.xyz">des cours d'info</a>
  </body>
</html>
```

- [x] Une balise n'est pas fermée correctement
- [ ] Toutes les balises sont fermées correctement
- [ ] On ne peut pas savoir si les balises sont fermées, ce n'est qu'un extrait
- [ ] La balise `<a>` est incorrecte, il faut utiliser `<link>`

### Lors d'une connexion HTTP

- [x] Chaque requête provoque au plus une réponse
- [ ] Une requête peut engendrer plusieurs réponses
- [ ] Plusieurs requêtes peuvent engendrer une seule réponse, c'est plus efficace
- [ ] Les images d'une page sont transmises dans le texte directement


## Boucles et `list`

### On considère l'extrait d'une `list` Python suivant : `prenoms = ["Frank", "Paulette", "Suzanne", ...]`

Compléter le code suivant pour créer la liste des longueurs des prénoms :

```python
prenoms = ["Frank", "Paulette", "Suzanne", ...]
longueurs = []
for prenom in prenoms:
    ......
```

- [x] `longueurs.append(len(prenom))`
- [ ] `longueurs = longueurs + len(prenom)`
- [ ] `longueurs + [len(prenom)]`
- [ ] `longueurs = longueurs.append(len(prenom))`


### Dans une `list`, on peut enregistrer des éléments ...


- [x] ayant des types différents. Cela n'est pas incorrect
- [ ] n'ayant qu'un seul type. Sans quoi `ListError`
- [ ] du type entier (`int`) exclusivement
- [ ] dy type entier (`int`) ou (`str`) exclusivement

## Dictionnaires : `dict`

### On considère le dictionnaire suivant dont voici un extrait :

```python
repertoire = {"Pierre": "0611223344", "Fanny": "0622334455", "Nael": "0677889900", ...}
```

Quelle instruction nous permet de savoir si "Amandine" y figure ?

- [x] `"Amandine" in repertoire`
- [ ] Aucune, il faut faire une boucle et comparer
- [ ] `"Amandine" in repertoire.items()`
- [ ] `"Amandine" in repertoire.values()`

### On considère le dictionnaire suivant dont voici un extrait :

```python
repertoire = {"Pierre": "0611223344", "Fanny": "0622334455", "Nael": "0677889900", ...}
```

Quelle instruction nous permet d'ajouter Chantal dont le numéro est "0622224444" ?

- [x] `repertoire["Chantal"] = "062222444"`
- [ ] `repertoire.append("Chantal", "062222444")`
- [ ] `repertoire += {["Chantal"] = "062222444"}`
- [ ] `repertoire.add("Chantal") = "062222444"`

### On considère le dictionnaire suivant dont voici un extrait :

```python
repertoire = {"Pierre": "0611223344", "Fanny": "0622334455", "Nael": "0677889900", ...}
```

Quelle instruction nous permet de savoir si le numéro "0655443322" y figure ?

- [x] `"0655443322" in repertoire.values()`
- [ ] Aucune, il faut faire une boucle et comparer
- [ ] `"0655443322" in repertoire.items()`
- [ ] `"0655443322" in repertoire`

