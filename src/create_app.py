from flask import Flask
from flask_sqlalchemy import SQLAlchemy


##################################################################################
##################################################################################
#                                   RUNTIME
##################################################################################
##################################################################################


UPLOAD_FOLDER = "uploads/"
DOWNLOAD_FOLDER = "downloads/"
ALLOWED_EXTENSIONS = {"md"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db/qcm.db"
app.config["SECRET_KEY"] = "random string"

db = SQLAlchemy(app)

if "sqlite" in app.config["SQLALCHEMY_DATABASE_URI"]:

    def _fk_pragma_on_connect(dbapi_con, con_record):  # noqa
        dbapi_con.execute("pragma foreign_keys=ON")

    with app.app_context():
        from sqlalchemy import event

        event.listen(db.engine, "connect", _fk_pragma_on_connect)
