from random import randint
from flask import request, flash, url_for, make_response, redirect, render_template
from .model import app, db, Choice, Marks, Qcm, QcmFile, Student, Work
from .parser import ParseQCM


def create_app():
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/teacher")
    def teacher():
        return render_template("teacher.html")

    @app.route("/new", methods=["GET", "POST"])
    def new():
        data = None
        if request.method == "POST":
            file = request.files.get("source")
            is_valid_file, error_message = QcmFile.validate_file(file)
            if not is_valid_file:
                flash(error_message)
                data = {"invalid file", repr(file)}
            else:
                try:
                    qcm_file = QcmFile.from_file(file)
                    message = qcm_file.flash_message_ok()
                    parsed_qcm = ParseQCM.from_file(qcm_file.filename)
                    qcm = Qcm.from_parsed_qcm(parsed_qcm)
                    db.session.add(qcm)
                    db.session.commit()
                    flash(f"{message}. Parsing correct, id_qcm : {qcm.id}")
                    data = {"qcm_id": qcm.id}

                except Exception as e:
                    flash(f"Fichier impossible à lire. {repr(e)}")
                    print(repr(e))
                    data = {"Fichier illisible": repr(e)}

        return render_template("new.html", data=data)

    @app.route("/qcms")
    def qcms():
        return render_template("qcms.html", qcms=Qcm.query.all())

    @app.route("/marks", methods=["GET", "POST"])
    def marks():
        if request.method == "POST":
            id_qcm_from_request = request.form.get("id_qcm")
            try:
                id_qcm = int(id_qcm_from_request)
            except TypeError:
                flash("QCM {id_qcm_from_request} introuvable.")
                return render_template("marks.html")
            qcm = Qcm.query.get(id_qcm)
            works = Work.query.filter_by(id_qcm=id_qcm).all()
            return render_template("marks.html", qcm=qcm)
        return render_template("marks.html")

    @app.route("/per_student/<id_student>")
    def per_student(id_student):
        try:
            id_student = int(id_student)
        except TypeError:
            return render_template("index.html")
        works = Work.query.filter_by(id_student=id_student).all()
        return render_template("per_student.html", works=works)

    @app.route("/marks/<id_qcm>")
    def marks_for_qcm(id_qcm):
        try:
            id_qcm = int(id_qcm)
            qcm = Qcm.query.get(id_qcm)
        except TypeError:
            qcm = None
        return render_template("marks.html", qcm=qcm)

    @app.route("/student")
    def student():
        return render_template("student.html")

    @app.route("/qcm", methods=["POST"])
    def qcm():
        print(request.form)
        try:
            name = f"{request.form.get('student.name')} {request.form.get('student.firstname')}"
            id_qcm = int(request.form.get("qcm.id"))
        except TypeError:
            return render_template(
                "confirmation_page.html", data="Formulaire illisible"
            )

        qcm = Qcm.query.get(id_qcm)
        if qcm is None:
            return render_template("confirmation_page.html", data="Qcm introuvable")

        # get the student id
        students = Student.query.filter_by(name=name).all()
        if len(students) == 1:
            student = students[0]
        else:
            if len(students) > 1:
                # make a new student with variation of name
                name += str(randint(1, 9))
            student = Student(name=name)
            db.session.add(student)
            db.session.commit()
        id_student = student.id

        print(qcm.format())

        # create a work
        work = Work(id_qcm=id_qcm, id_student=id_student)
        db.session.add(work)
        db.session.commit()

        # get work id
        id_work = work.id

        resp = make_response(render_template("qcm.html", qcm=qcm, name=name))
        resp.set_cookie("id_work", str(id_work))
        return resp

    @app.route("/answers", methods=["POST"])
    def answers():
        print(request.form)
        print(dir(request.form))
        try:
            id_work = int(request.cookies.get("id_work"))
        except TypeError:
            return render_template("confirmation_page.html", data="Utilisateur inconnu")

        print(f"id_work: {id_work}")

        for k, v in request.form.items():
            if k.startswith("Q ") and v.startswith("A "):
                id_question = int(k.split(" ")[1])
                id_answer = int(v.split(" ")[1])
                choice = Choice(
                    id_work=id_work, id_question=id_question, id_answer=id_answer
                )
                db.session.add(choice)
        work = Work.query.get(id_work)
        work.count_points()
        db.session.commit()
        return render_template("confirmation_page.html", data="Réponses enregistrées")

    db.create_all()
    return app
