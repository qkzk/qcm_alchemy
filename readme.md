# QCM with SQLAlchemy


## Roadmap

### Models

- [x] QCM original
- [ ] QCM pour un élève
- [ ] Student
- [ ] Marks

### Parsing

- [x] fichier .md -> model bdd

### Export -> html

- [ ] mélanger
- [ ] présenter une question par page
- [ ] lien entre les pages
- [ ] regrouper les résultats
- [ ] chronomètre
- [ ] cookies
- [ ] mode anti triche

### Marks

- [ ] enregistrer les réponses de l'élève
- [ ] compter les points

### Export Marks

- [ ] exporter les notes d'un QCM
- [ ] envoyer à l'enseignant un csv
- [ ] télécharger un csv
- [ ] nettoyer la bdd après l'envoi et régulièrement (RGPD)

## Mixing answers

* shuffle les parts, questions, answers
* lorsqu'on envoie les answers à la vue, faut envoyer l'`id_question: id_answer` à la vue
* ensuite on compare `id_question: id_answer` avec `id_question: id(answer where is_correct)`

## Steps

- présenter un qcm
