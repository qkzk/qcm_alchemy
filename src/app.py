"""
title: app
author: qkzk
date: 2022/05/08
"""
import os
from datetime import datetime, timedelta
from random import randint
import secrets
from typing import Union

from flask import (
    Flask,
    make_response,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
)
from flask_apscheduler import APScheduler
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from werkzeug.datastructures import ImmutableMultiDict

from .model import app, db, Choice, Qcm, QcmFile, ResetKey, Student, Teacher, Text, Work
from .parser import ParseQCM
from .sendmail import EmailSender

RESET_PASSWORD_MAIL_ADDRESS = "qcm.serveur@lyceedesflandres.fr"
RESET_PASSWORD_MAIL_TOPIC = "qcmqkzk: réinitialisez votre mot de passe"
RESET_PASSWORD_MAIL_CONTENT = """Cher utilisateur de qcmqkzk,

Réinitialisez votre mot de passe en suivant ce lient : 

https://qcmqkzk.herokuapp.com/reset_password/{teacher_id}/{key} 

Ce lien est valable une heure.

                                                The QCM serveur.
                    """


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


def insert_from_file(file: "werkzeug.datastructures.FileStorage", current_user) -> dict:
    """
    Insert a QCM in database from a downloaded file which has .md extension.
    """
    qcm_file = QcmFile.from_file(file)
    parsed_qcm = ParseQCM.from_file(qcm_file.filename)
    try:
        qcm = Qcm.from_parser(parsed_qcm, current_user.id)
        print(qcm)
        db.session.add(qcm)
        db.session.commit()
        data = {"qcm_id": qcm.id}
        print(data)
        return data
    except Exception as e:
        return {"Fichier illisible": repr(e)}


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


def read_id_work_from_cookie(cookies: ImmutableMultiDict[str, str]) -> int:
    try:
        return int(cookies.get("id_work"))
    except TypeError:
        return -1


def insert_answers_from_request(form: ImmutableMultiDict[str, str], id_work: int):
    """
    Insert the received answers from a POST form.
    Returns True if the insertion went without error
    """
    for key, value in form.items():
        if key.startswith("Q_") and value.startswith("A_"):
            try:
                insert_choice(key, value, id_work)
            except TypeError:
                return False
        elif key.startswith("T_"):
            try:
                insert_textarea(key, value, id_work)
            except TypeError:
                return False
    return True


def construct_qcm_resonse(qcm: Qcm, name: str, work: Work):

    format_name = f" - Nom: {name}"
    resp = make_response(
        render_template("qcm.html", qcm=qcm, name=name, base_data=format_name)
    )
    resp.set_cookie("id_work", str(work.id))
    return resp


def validate_qcm_work(qcm: Qcm, work: Work) -> tuple[bool, str]:
    if not qcm:
        return False, "QCM introuvable"
    if not work:
        return False, "Travail introuvable"
    return True, ""


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

    login = LoginManager(app)
    login.login_view = "login"

    @app.before_request
    def make_session_permanent():
        """Limit sessions duration to 60 minutes."""
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=60)

    @app.context_processor
    def inject_enumerate():
        return dict(enumerate=enumerate)

    @login.user_loader
    def load_user(id):
        return Teacher.query.get(id)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form.get("email")
            clear_password = request.form.get("password")
            teacher = Teacher.get_from_email(email)
            if teacher is None:
                print("teacher unknown")
                return redirect(url_for("login"))
            if teacher.check_password_hash(clear_password):
                print("login successful")
                login_user(teacher)
                return redirect(url_for("teacher"))

        return render_template("login.html")

    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("login"))

    @app.route("/new_teacher", methods=["GET", "POST"])
    def new_teacher():
        if request.method == "POST":
            email = request.form.get("email")
            clear_password = request.form.get("password")
            if email is None or clear_password is None:
                print(f"new_teacher: can't read form. {email} - {clear_password}")
                return render_template("new_teacher.html")
            teacher = Teacher.insert(email, clear_password)
            if teacher is not None:
                print(f"teacher {teacher} inserted... redirecting")
                return redirect(url_for("login"))

        return render_template("new_teacher.html")

    @app.route("/forgotten_password", methods=["GET", "POST"])
    def forgotten_password():
        data = {}
        if request.method == "POST":
            email = request.form.get("email")
            if email is not None:
                teacher = Teacher.get_from_email(email)
                if teacher is None:
                    return render_template("404.html")
                key = secrets.token_urlsafe(16)
                ResetKey.remove_key(teacher.id)
                reset_key = ResetKey(
                    key=key, id_teacher=teacher.id, datetime=datetime.now()
                )
                db.session.add(reset_key)
                db.session.commit()
                EmailSender(
                    RESET_PASSWORD_MAIL_ADDRESS,
                    email,
                    RESET_PASSWORD_MAIL_TOPIC,
                    RESET_PASSWORD_MAIL_CONTENT.format(teacher_id=teacher.id, key=key),
                ).send_message()
            data = {
                "message": "Suivez les instructions dans l'email pour réinitialiser votre mot de passe."
            }

        return render_template("forgotten_password.html", data=data)

    @app.route("/reset_password/<teacher_id>/<key>")
    def reset_password_from_key(teacher_id, key):
        teacher = ResetKey.query.filter_by(key=key).first_or_404().teacher
        if ResetKey.key_match(teacher_id, key):
            ResetKey.remove_key(teacher.id)
            data = {
                "teacher_id": teacher.id,
                "email": teacher.email,
                "reset": True,
            }
            return render_template("reset_password.html", data=data)
        return render_template("404.html")

    @app.route("/reset_password", methods=["POST"])
    def reset_password():
        email = request.form.get("email")
        password = request.form.get("password")
        teacher_id = request.form.get("teacher_id")
        teacher = Teacher.query.get(teacher_id)
        if teacher is None:
            return render_template("404.html")
        teacher.update_password(password)
        data = {
            "message": "Mot de passe réinitialisé avec succès. Vous pouvez vous identifier.",
            "reset": False,
        }
        return render_template("reset_password.html", data=data)

    @app.route("/rgpd")
    def rgpd():
        return render_template("rgpd.html")

    @app.route("/tutorial")
    def tutorial():
        return render_template("tutorial.html")

    @app.route("/teacher")
    @login_required
    def teacher():
        return render_template("teacher.html", current_user=current_user)

    @app.route("/new", methods=["GET", "POST"])
    @login_required
    def new():
        if request.method == "GET":
            return render_template("new.html", data=None)

        file = request.files.get("source")
        is_valid_file, error_message = QcmFile.validate_file(file)
        if is_valid_file:
            data = insert_from_file(file, current_user)
        else:
            data = {"Fichier invalide": error_message}

        return render_template("new.html", data=data)

    @app.route("/qcms/<teacher_id>")
    @login_required
    def qcms(teacher_id):
        return render_template(
            "qcms.html", qcms=Qcm.query.filter_by(id_teacher=teacher_id).all()
        )

    @app.route("/export/<int:qcm_id>")
    @login_required
    def export(qcm_id: int):
        path = Work.write_export(qcm_id)
        directory = os.path.join(os.getcwd(), app.config["DOWNLOAD_FOLDER"])
        return send_from_directory(directory=directory, path=path)

    @app.route("/marks/<int:id_qcm>")
    @login_required
    def marks(id_qcm):
        qcm = Qcm.query.get(id_qcm)
        return render_template("marks.html", qcm=qcm)

    @app.route("/student")
    def student():
        return render_template("student.html")

    @app.route("/work", methods=["GET", "POST"])
    @login_required
    def work():
        print("work", request.values)
        try:
            id_qcm = int(request.values.get("id_qcm"))
            index = int(request.values.get("index"))
        except TypeError:
            return render_template("confirmation_page.html", data="Travail introuvable")

        qcm = Qcm.query.get(id_qcm)
        if request.values.get("preview") is not None:
            return render_template(
                "work.html",
                qcm=qcm,
                index=index,
                base_data=f"- Prévisualiser",
                work=None,
            )
        try:
            work = qcm.works[index]
        except IndexError:
            return render_template("confirmation_page.html", data="Mauvais index")
        is_complete, error_message = validate_qcm_work(qcm, work)
        if not is_complete:
            return render_template("confirmation_page.html", data=error_message)
        return render_template(
            "work.html",
            qcm=qcm,
            index=index,
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
        work = Work.create_and_commit(id_qcm=id_qcm, id_student=id_student)

        return construct_qcm_resonse(qcm, name, work)

    @app.route("/answers", methods=["POST"])
    def answers():
        id_work = read_id_work_from_cookie(request.cookies)
        if id_work == -1:
            render_template("confirmation_page.html", data="Utilisateur inconnu")

        work = Work.query.get(id_work)
        if work.is_submitted:
            return render_template(
                "confirmation_page.html", data="Vous avez déjà répondu à ce QCM."
            )

        if not insert_answers_from_request(request.form, id_work):
            return render_template("confirmation_page.html", data="Réponses illisibles")

        work.is_submitted = True
        work.count_points()
        db.session.commit()
        return render_template("confirmation_page.html", data="Réponses enregistrées")

    # db.drop_all()
    db.create_all()

    return app
