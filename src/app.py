"""
title: app
author: qkzk
date: 2022/05/08
"""
import os
from datetime import datetime, timedelta
from random import randint

from flask import (
    abort,
    flash,
    Flask,
    g,
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
from werkzeug.utils import secure_filename

from .forms import (
    ForgottenPasswordForm,
    LoginForm,
    NewPasswordForm,
    NewTeacherForm,
    RemoveQCMForm,
    ResetPasswordForm,
    QcmFileForm,
    StudentForm,
)
from .model import (
    app,
    db,
    EmailConfirmation,
    Choice,
    Qcm,
    QcmFile,
    ResetKey,
    Student,
    Teacher,
    Text,
    Work,
)
from .parser import ParseQCM
from .sendmail import check_email, EmailSender


SERVER_PASSWORD_MAIL_ADDRESS = "qcm.serveur@lyceedesflandres.fr"
RESET_PASSWORD_MAIL_TOPIC = "qcmqkzk: réinitialisez votre mot de passe"
RESET_PASSWORD_MAIL_CONTENT = """Cher utilisateur de qcmqkzk,

Réinitialisez votre mot de passe en suivant ce lient : 

https://qcmqkzk.herokuapp.com/reset_password/{teacher_id}/{key} 

Ce lien est valable une heure.

                                                The QCM serveur.
                    """
CONFIRM_TEACHER_MAIL_TOPIC = "Confirmez votre compte sur qcmqkzk !"
CONFIRM_TEACHER_MAIL_CONTENT = """
Bienvenu sur qcmqkzk !

Votre compte n'est pas encore actif.

Veuillez suivre sur le lien ci-dessous pour le confirmer : 

https://qcmqkzk.herokuapp.com/email_confirmation/{teacher_id}/{key}

À bientôt,

qcmqkzk

                    """


def clear_records_and_files():
    """Scheduled task : clean the database and the old files."""
    print("cleaner is running...")
    Qcm.clear_old_records()
    Student.clear_old_records()
    ResetKey.clear_old_records()
    EmailConfirmation.clear_old_records()
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


def insert_from_file(file: "werkzeug.datastructures.FileStorage", current_user) -> int:
    """
    Insert a QCM in database from a downloaded file which has .md extension.
    Returns its qcm.id
    Returns -1 if the insertion went wrong.
    """
    try:
        qcm_file = QcmFile.from_file(file)
        parsed_qcm = ParseQCM.from_file(qcm_file.filename)
        qcm = Qcm.from_parser(parsed_qcm, current_user.id)
        print(qcm)
        db.session.add(qcm)
        db.session.commit()
        return qcm.id
    except Exception as e:
        return -1


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
        render_template(
            "qcm.html", qcm=qcm, name=name, base_data=format_name, preview=False
        )
    )
    resp.set_cookie("id_work", str(work.id), samesite="Strict")
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

    @app.before_request
    def fix_missing_csrf_token():
        if app.config["WTF_CSRF_FIELD_NAME"] not in session:
            if app.config["WTF_CSRF_FIELD_NAME"] in g:
                g.pop(app.config["WTF_CSRF_FIELD_NAME"])

    @app.after_request
    def add_security_headers(resp):
        resp.headers[
            "Content-Security-Policy"
        ] = "img-src *; default-src 'self'; style-src 'self' 'unsafe-inline'; frame-src www.youtube-nocookie.com www.youtube.com"
        return resp

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
        form = LoginForm()
        if form.validate_on_submit():
            email = form.email.data
            clear_password = form.clear_password.data

            teacher = Teacher.get_from_email(email)
            if teacher is None:
                print("teacher unknown")
                flash("Identifants incorrects.")
            elif not teacher.is_confirmed:
                print("teacher account not activated")
                flash("Ce compte n'est pas activé. Un mail vous a été adressé.")
                return render_template("index.html")
            elif teacher.check_password_hash(clear_password):
                print("login successful")
                login_user(teacher)
                flash("Vous êtes maintenant connecté.")
                return redirect(url_for("teacher"))
            else:
                flash("Identifants incorrects.")

        return render_template("login.html", form=form)

    @app.route("/new_password", methods=["GET", "POST"])
    @login_required
    def new_password():
        form = NewPasswordForm()
        base_data = {}
        if form.validate_on_submit():
            current_password = form.current_password.data
            new_password = form.new_password.data
            if current_password is None or new_password is None:
                return render_template("new_password.html")
            if current_user.check_password_hash(current_password):
                current_user.update_password_and_commit(new_password)
                flash("Mot de passe mis à jour")
                print("new password ok")
                return render_template("teacher.html", base_data=base_data)
            else:
                print("new password not ok")
                flash("Mot de passe invalide")

        return render_template("new_password.html", base_data=base_data, form=form)

    @app.route("/logout")
    def logout():
        logout_user()
        flash("Vous êtes deconnecté")
        return redirect(url_for("login"))

    @app.route("/new_teacher", methods=["GET", "POST"])
    def new_teacher():
        form = NewTeacherForm()
        if form.validate_on_submit():
            email = form.email.data
            clear_password = form.clear_password.data
            if email is None or clear_password is None:
                flash("Formulaire incomplet")
                return render_template("new_teacher.html")

            if not check_email(email):
                print(f"new_teacher: can't read form. {email}")
                flash("email invalide")
                return render_template("new_teacher.html", form=form)

            teacher = Teacher.insert(email, clear_password)
            if teacher is not None:
                print(f"teacher {teacher} inserted... redirecting")
                confirmation_key = EmailConfirmation.clear(teacher.id).new(teacher.id)
                if EmailSender(
                    SERVER_PASSWORD_MAIL_ADDRESS,
                    email,
                    CONFIRM_TEACHER_MAIL_TOPIC,
                    CONFIRM_TEACHER_MAIL_CONTENT.format(
                        teacher_id=teacher.id, key=confirmation_key.key
                    ),
                ).send_message():
                    db.session.add(confirmation_key)
                    db.session.commit()
                    return redirect(url_for("email_confirmation"))
                flash("Problème lors de l'envoi du mail de confirmation")
                return render_template(
                    "new_teacher.html",
                    form=form,
                )

        return render_template("new_teacher.html", form=form)

    @app.route("/forgotten_password", methods=["GET", "POST"])
    def forgotten_password():
        form = ForgottenPasswordForm()
        if form.validate_on_submit():
            email = form.email.data
            if email is None or not check_email(email):
                return render_template(
                    "forgotten_password.html", base_data="email invalide", form=form
                )

            teacher = Teacher.get_from_email(email)
            if teacher is None:
                abort(404)
            reset_key = ResetKey.clear(teacher.id).new(teacher.id)

            if EmailSender(
                SERVER_PASSWORD_MAIL_ADDRESS,
                email,
                RESET_PASSWORD_MAIL_TOPIC,
                RESET_PASSWORD_MAIL_CONTENT.format(
                    teacher_id=teacher.id, key=reset_key.key
                ),
            ).send_message():
                db.session.add(reset_key)
                db.session.commit()
                flash(
                    "Suivez les instructions dans l'email pour réinitialiser votre mot de passe."
                )
            else:
                flash("Une erreur est survenue lors de l'envoi du mail.")

        return render_template("forgotten_password.html", form=form)

    @app.route("/reset_password/<int:teacher_id>/<key>")
    def reset_password_from_key(teacher_id, key):
        print(f"reset_password ! with {teacher_id} and {key}")
        teacher = ResetKey.query.filter_by(key=key).first_or_404().teacher
        print("teacher", teacher)
        if ResetKey.key_match(teacher_id, key):
            ResetKey.remove_key(teacher.id)
            data = {
                "teacher_id": teacher.id,
                "email": teacher.email,
                "reset": True,
            }
            form = ResetPasswordForm()
            return render_template("reset_password.html", data=data, form=form)
        abort(404)

    @app.route("/email_confirmation")
    def email_confirmation():
        return render_template("email_confirmation.html")

    @app.route("/email_confirmation/<int:teacher_id>/<key>")
    def email_confirmation_from_id_key(teacher_id: int, key):
        teacher = Teacher.query.get(teacher_id)
        if teacher is None:
            abort(404)
        teacher.is_confirmed = True
        db.session.commit()
        if EmailConfirmation.key_match(teacher_id, key):
            EmailConfirmation.remove_key(teacher.id)
            flash("Votre compte est crée. Vous pouvez vous connecter")
            return render_template("index.html")
        abort(404)

    @app.route("/reset_password", methods=["POST"])
    def reset_password():
        data = None
        form = ResetPasswordForm()
        if form.validate_on_submit():
            print(request.form)
            clear_password = form.clear_password.data
            teacher_id = request.form.get("teacher_id")
            print("teacher_id", teacher_id)
            teacher = Teacher.query.get(teacher_id)
            if teacher is None:
                abort(404)
            teacher.update_password_and_commit(clear_password)
            flash("Mot de passe réinitialisé avec succès. Vous pouvez vous identifier.")
            data = {"reset": False}
        return render_template("reset_password.html", data=data, form=form)

    @app.route("/delete_account")
    @login_required
    def delete_account():
        return render_template("delete_account.html")

    @app.route("/remove_account")
    @login_required
    def remove_account():
        current_user.remove_and_commit()
        flash("Votre compte, vos qcms et les travaux de vos élèves sont supprimés.")
        return redirect(url_for("index"))

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
        if not current_user.is_confirmed:
            return abort(404)

        data = None
        form = QcmFileForm()
        if request.method == "GET":
            return render_template("new.html", data=data, form=form)

        if form.validate_on_submit():
            file = form.source.data
            filename = secure_filename(file.filename)
            print(f"qcm with sent filename {filename}")

            is_valid_file, error_message = QcmFile.validate_file(file)
            if is_valid_file:
                qcm_id = insert_from_file(file, current_user)
                if qcm_id == -1:
                    flash("Le fichier source n'est pas formaté correctement")
                else:
                    flash("QCM inséré dans la base !")
                    data = {"qcm_id": qcm_id}
                print(f"qcm inserted correctly {qcm_id}")
            else:
                flash("Fichier invalide")
                print(f"qcm couldn't be inserted")

        return render_template("new.html", data=data, form=form)

    @app.route("/qcms/<int:teacher_id>")
    @login_required
    def qcms(teacher_id):
        if not current_user.is_confirmed:
            return redirect(url_for("index"))
        return render_template(
            "qcms.html", qcms=Qcm.query.filter_by(id_teacher=teacher_id).all()
        )

    @app.route("/remove/<int:id_qcm>", methods=["GET", "POST"])
    @login_required
    def remove(id_qcm: int):
        qcm = Qcm.query.get(id_qcm)
        if qcm is None or not current_user.is_owner(qcm):
            abort(404)
        form = RemoveQCMForm()
        if form.validate_on_submit():
            title = qcm.title
            qcm_id = qcm.id
            qcm.remove_and_commit()
            print(f"{current_user} removed {qcm}")
            flash(f"QCM {title} numero {qcm_id} supprimé !")
            return redirect(url_for("qcms", teacher_id=current_user.id))

        return render_template("remove.html", qcm=qcm, form=form)

    @app.route("/export/<int:qcm_id>")
    @login_required
    def export(qcm_id: int):
        if not current_user.is_confirmed:
            return redirect(url_for("index"))
        path = Work.write_export(qcm_id)
        directory = os.path.join(os.getcwd(), app.config["DOWNLOAD_FOLDER"])
        return send_from_directory(directory=directory, path=path)

    @app.route("/marks/<int:id_qcm>")
    @login_required
    def marks(id_qcm):
        if not current_user.is_confirmed:
            return redirect(url_for("index"))
        qcm = Qcm.query.get(id_qcm)
        return render_template("marks.html", qcm=qcm)

    @app.route("/student")
    def student():
        form = StudentForm()
        return render_template("student.html", form=form)

    @app.route("/work", methods=["GET", "POST"])
    @login_required
    def work():
        id_qcm = int(request.values.get("id_qcm"))
        index = int(request.values.get("index"))
        qcm = Qcm.query.get(id_qcm)

        if qcm is None:
            abort(404)

        if request.values.get("preview") is not None:
            return render_template(
                "work.html",
                qcm=qcm,
                index=index,
                preview=True,
                base_data=f"- Prévisualiser",
                work=None,
            )
        try:
            work = qcm.works[index]
            print(work)
        except (IndexError, TypeError):
            abort(404)

        is_complete, error_message = validate_qcm_work(qcm, work)
        if not is_complete:
            return render_template("confirmation_page.html", data=error_message)
        return render_template(
            "work.html",
            qcm=qcm,
            index=index,
            work=work,
            base_data=f"- Nom: {work.student.name} - Score: {work.points}",
            preview=True,
        )

    @app.route("/qcm", methods=["POST"])
    def qcm():
        form = StudentForm()
        if not form.validate_on_submit():
            flash("Formulaire illisible")
            return render_template("confirmation_page.html")

        name = f"{form.lastname.data} {form.firstname.data}"
        name = trunctate_string(name, 100)
        id_qcm = form.qcm_id.data
        qcm = Qcm.query.get(id_qcm)
        if qcm is None:
            abort(404)

        # get the student id
        students = Student.query.filter_by(name=name).all()
        id_student = find_or_add_student(students, name)

        # create a work
        work = Work.create_and_commit(id_qcm=id_qcm, id_student=id_student)

        return construct_qcm_resonse(qcm, name, work)

    @app.route("/answers", methods=["POST"])
    def answers():
        id_work = read_id_work_from_cookie(request.cookies)
        work = Work.query.get(id_work)
        if work is None:
            abort(404)
        if work.is_submitted:
            flash("Vous avez déjà répondu à ce QCM")
            return render_template("confirmation_page.html")

        if not insert_answers_from_request(request.form, id_work):
            flash("Formulaire illisible")
            return render_template("confirmation_page.html")

        work.record()
        flash("Réponses enregistrées")
        return render_template("confirmation_page.html")

    # db.drop_all()
    db.create_all()

    return app
