import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

##################################################################################
##################################################################################
#                                   RUNTIME
##################################################################################
##################################################################################


UPLOAD_FOLDER = "uploads/"
DOWNLOAD_FOLDER = "created_files/"
ALLOWED_EXTENSIONS = {"md"}

DEFAULT_DATABASE_PATH = "postgresql://quentin:bla@localhost/qcm"
uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
DATABASE_URL = uri if uri else DEFAULT_DATABASE_PATH

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db/qcm.db"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SECRET_KEY"] = "random string"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

if "sqlite" in app.config["SQLALCHEMY_DATABASE_URI"]:

    def _fk_pragma_on_connect(dbapi_con, con_record):
        dbapi_con.execute("pragma foreign_keys=ON")

    with app.app_context():
        from sqlalchemy import event

        event.listen(db.engine, "connect", _fk_pragma_on_connect)
