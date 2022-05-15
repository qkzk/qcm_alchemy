---
title: "Titre secondaire"
subtitle: "Titre à zapper"
author: "qkzk"
date: "2021/05/23"
theme: "metropolis"
geometry: "margin=1.5cm"
header-includes:
- \usepackage{fancyhdr}
- \pagestyle{fancy}
- \fancyhead[CO,CE]{This is fancy header}
- \fancyfoot[CO,CE]{And this is a fancy footer}
- \fancyfoot[LE,RO]{\thepage}
- \thispagestyle{fancy}
- \usepackage{tcolorbox}
- \newtcolorbox{myquote}{colback=teal!10!white, colframe=teal!55!black}
- \renewenvironment{Shaded}{\begin{myquote}}{\end{myquote}}

---

# Titre prioritaire

## culture

### Comment arrêter le réchauffement climatique ?

- [t]

### Qui est-ce ?

![personne](https://media.vogue.fr/photos/5d8c8e536f878f000880cbd5/16:9/w_1920%2Cc_limit/000_ARP4090096.jpg)

- [x] Jacques Chirac
- [ ] Raymond Barre
- [ ] François Mitterand
- [ ] Valery Giscard d'Estaing

## maths

### Calculer $1 +1$

- [x] 2
- [ ] 3
- [ ] 5


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
