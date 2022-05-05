from flask import request, flash, url_for, redirect, render_template
from .model import app, db, Marks, QcmFile
from .parser import ParseQCM


def create_app():
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

    @app.route("/")
    def index():
        return render_template("index.html", marks=Marks.query.all())

    @app.route("/marks", methods=["GET", "POST"])
    def marks():
        if request.method == "POST":
            if not Marks.validate(request.form):
                flash("Vous devez remplir tous les champs.", "error")
            else:
                mark = Marks.from_form(request.form)
                db.session.add(mark)
                db.session.commit()
                flash("Réponses enregistrées.")
                return redirect(url_for("marks"))
        return render_template("marks.html")

    @app.route("/qcm/<id_qcm>")
    def qcm_view(id_qcm):
        qcm = Qcm.query.get(id_qcm)
        print(qcm.format())
        return render_template("qcm.html", qcm=qcm)

    @app.route("/answers", methods=["POST"])
    def answers():
        print(request.form)
        print(dir(request.form))
        return "<h1>ok</h1>"

    db.create_all()
    return app
