# QCM with SQLAlchemy


## Roadmap

### Models

- [x] QCM original
- [x] Student
- [x] Marks

### Parsing

- [x] fichier .md -> model bdd

### Export -> html

- [ ] mélanger
- [ ] présenter une question par page
- [ ] lien entre les pages
- [x] regrouper les résultats
- [ ] chronomètre
- [x] cookies
- [x] mode anti triche

### Marks

- [x] enregistrer les réponses de l'élève
- [x] compter les points

### Export Marks

- [x] exporter les notes d'un QCM
- [x] télécharger un csv
- [ ] nettoyer la bdd après l'envoi et régulièrement (RGPD)

### Views

- [x] upload a .md (basic)
- [x] validate upload
- [x] qcm
- [x] validate

### Style

- [x] base
- [x] custom for teacher
- [x] custom for student
- [x] latex

## Mixing answers

* shuffle les parts, questions, answers
* lorsqu'on envoie les answers à la vue, faut envoyer l'`id_question: id_answer` à la vue
* ensuite on compare `id_question: id_answer` avec `id_question: id(answer where is_correct)`


### Caching

- [ ] utiliser [flask caching](https://flask-caching.readthedocs.io/en/latest/)
- [ ] stratégie : quand on veut accéder à un QCM, le cacher après l'avoir retrieve, le drop si plus de x qcm ?

## Steps

- [x] présenter un qcm
- [x] enregistrer les réponses
- [x] noter les réponses
- [x] afficher des récaps : 
    - [x] ensemble des qcm
    - [x] notes d'un qcm
    - [x] notes d'un étudiant
- [x] style pour chaque page
- [x] latex
- [x] block content etc.
- [x] exporter en csv
