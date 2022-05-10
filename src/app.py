"""
title: app
author: qkzk
date: 2022/05/08
"""
import os
from datetime import datetime
from random import randint
from flask import (
    Flask,
    request,
    flash,
    url_for,
    make_response,
    redirect,
    render_template,
    send_from_directory,
)
from flask_apscheduler import APScheduler

from .model import app, db, Choice, Qcm, QcmFile, Student, Text, Work
from .parser import ParseQCM


def clear_records_and_files():
    """Scheduled task : clean the database and the old files."""
    print("cleaner is running...")
    Qcm.clear_old_records()
    Student.clear_old_records()
    delete_old_files("UPLOAD_FOLDER")
    delete_old_files("DOWNLOAD_FOLDER")
    print("cleaner completed")


def delete_old_files(env_name: str):
    """Delete old files from created_files and uploads"""
    directory = os.path.join(os.getcwd(), app.config[env_name])
    for filename in os.listdir(directory):
        if filename != "readme.md":
            os.remove(os.path.join(directory, filename))


def trunctate_string(string: str, size: int):
    """Truncate a string after `size` chars."""
    if len(string) > size:
        return string[:size]
    return string


def find_or_add_student(students: list[Student], name: str) -> int:
    if len(students) == 1:
        student = students[0]
    else:
        if len(students) > 1:
            # make a new student with variation of name
            name += str(randint(1, 9))
        # add the new student to database
        student = Student(name=name, datetime=datetime.now())
        db.session.add(student)
        db.session.commit()
    return student.id


def insert_from_file(file: "werkzeug.datastructures.FileStorage") -> dict:
    """
    Insert a QCM in database from a downloaded file which has .md extension.
    """
    qcm_file = QcmFile.from_file(file)
    parsed_qcm = ParseQCM.from_file(qcm_file.filename)
    password = randint(1000, 9999)
    try:
        qcm = Qcm.from_parser(parsed_qcm, password)
        print(qcm)
    except Exception as e:
        print(repr(e))
        raise e
    db.session.add(qcm)
    db.session.commit()
    data = {"qcm_id": qcm.id, "password": password}
    print(data)
    return data


def insert_textarea(key: str, value: str, id_work: int):
    """Insert a textarea answer into the database. Doesn't commit."""
    id_question = int(key.split("_")[1])
    text = Text(id_work=id_work, id_question=id_question, text=value.strip())
    db.session.add(text)


def insert_choice(key: str, value: str, id_work: int):
    """Insert a choice into the database. Doesn't commit."""
    id_question = int(key.split("_")[1])
    id_answer = int(value.split("_")[1])
    choice = Choice(id_work=id_work, id_question=id_question, id_answer=id_answer)
    db.session.add(choice)


def create_app() -> Flask:
    """Create a Flask Application with database and scheduler."""
    sched = APScheduler()
    sched.add_job(
        id="clear_records_and_files",
        func=clear_records_and_files,
        trigger="interval",
        hours=24,
    )
    sched.start()

    @app.context_processor
    def inject_enumerate():
        return dict(enumerate=enumerate)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/rgpd")
    def rgpd():
        return render_template("rgpd.html")

    @app.route("/tutorial")
    def tutorial():
        return render_template("tutorial.html")

    @app.route("/teacher")
    def teacher():
        return render_template("teacher.html")

    @app.route("/new", methods=["GET", "POST"])
    def new():
        if request.method == "GET":
            return render_template("new.html", data=None)

        file = request.files.get("source")
        is_valid_file, error_message = QcmFile.validate_file(file)
        if is_valid_file:
            try:
                data = insert_from_file(file)
            except Exception as e:
                print(repr(e))
                data = {"Fichier illisible": repr(e)}
        else:
            data = {"invalid file", error_message}

        return render_template("new.html", data=data)

    @app.route("/qcms")
    def qcms():
        return render_template("qcms.html", qcms=Qcm.query.all())

    @app.route("/export", methods=["POST"])
    def export():
        try:
            id_qcm = int(request.form.get("id_qcm"))
            qcm = Qcm.query.get(id_qcm)
            if qcm.validate_password(request.form.get("password")):
                path = Work.write_export(id_qcm)
                directory = os.path.join(os.getcwd(), app.config["DOWNLOAD_FOLDER"])
                return send_from_directory(directory=directory, path=path)
            else:
                return render_template(
                    "confirmation_page.html", data="Mauvais mot de passe"
                )

        except TypeError as e:
            print(repr(e))
            raise e
            return render_template("index.html")

    @app.route("/marks", methods=["POST"])
    def marks():
        id_qcm_from_request = request.values.get("id_qcm")
        try:
            id_qcm = int(id_qcm_from_request)
        except TypeError:
            return render_template("marks.html")
        qcm = Qcm.query.get(id_qcm)
        password = request.values.get("password")
        if qcm.validate_password(password):
            return render_template("marks.html", qcm=qcm, password=password)
        return render_template("confirmation_page.html", data="Mauvais password.")

    @app.route("/student")
    def student():
        return render_template("student.html")

    @app.route("/work", methods=["GET", "POST"])
    def work():
        print("work", request.values)
        try:
            id_qcm = int(request.values.get("id_qcm"))
            index = int(request.values.get("index"))
        except TypeError:
            raise
            return render_template("confirmation_page.html", data="Travail introuvable")

        password = int(request.values.get("password"))
        qcm = Qcm.query.get(id_qcm)
        if request.values.get("preview") is not None:
            return render_template(
                "work.html",
                qcm=qcm,
                index=index,
                password=password,
                base_data=f"- Prévisualiser",
                work=None,
            )
        try:
            work = qcm.works[index]
        except IndexError:
            return render_template("confirmation_page.html", data="Mauvais index")
        if not qcm:
            return render_template("confirmation_page.html", data="QCM introuvable")
        if not work:
            return render_template("confirmation_page.html", data="Travail introuvable")
        if not qcm.validate_password(password):
            return render_template("confirmation_page.html", data="Mauvais password")
        return render_template(
            "work.html",
            qcm=qcm,
            index=index,
            password=password,
            work=work,
            base_data=f"- Nom: {work.student.name} - Score: {work.points}",
        )

    @app.route("/qcm", methods=["POST"])
    def qcm():
        try:
            name = f"{request.form.get('student.name')} {request.form.get('student.firstname')}"
            name = trunctate_string(name, 100)
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
        id_student = find_or_add_student(students, name)

        # create a work
        work = Work(
            id_qcm=id_qcm,
            id_student=id_student,
            datetime=datetime.now(),
            is_submitted=False,
        )
        db.session.add(work)
        db.session.commit()

        format_name = f" - Nom: {name}"

        resp = make_response(
            render_template("qcm.html", qcm=qcm, name=name, base_data=format_name)
        )
        resp.set_cookie("id_work", str(work.id))
        return resp

    @app.route("/answers", methods=["POST"])
    def answers():
        try:
            id_work = int(request.cookies.get("id_work"))
        except TypeError:
            return render_template("confirmation_page.html", data="Utilisateur inconnu")

        work = Work.query.get(id_work)
        if work.is_submitted:
            return render_template(
                "confirmation_page.html", data="Vous avez déjà répondu à ce QCM."
            )

        for key, value in request.form.items():
            if key.startswith("Q_") and value.startswith("A_"):
                try:
                    insert_choice(key, value, id_work)
                except TypeError:
                    return render_template(
                        "confirmation_page.html", data="Réponses illisibles"
                    )
            elif key.startswith("T_"):
                try:
                    insert_textarea(key, value, id_work)
                except TypeError:
                    return render_template(
                        "confirmation_page.html", data="Réponses illisibles"
                    )

        work.is_submitted = True
        work.count_points()
        db.session.commit()
        return render_template("confirmation_page.html", data="Réponses enregistrées")

    # db.drop_all()
    db.create_all()

    return app
