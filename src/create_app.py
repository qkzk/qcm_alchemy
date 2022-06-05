"""
title: create_app
author: qkzk
date: 2022/05/08

Create a Flask app and an sqlalchemy database.
"""
import os

from flask import Flask
from flask_qrcode import QRcode
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

UPLOAD_FOLDER = "uploads/"
DOWNLOAD_FOLDER = "created_files/"
ALLOWED_EXTENSIONS = {"md"}
MAXPASSWORD = 2147483647

DEVELOPMENT_DATABASE_PATH = "postgresql://quentin:bla@localhost/qcm"
uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
DATABASE_URL = uri if uri else DEVELOPMENT_DATABASE_PATH

app = Flask(__name__)

app.config["MAX_PARSING_DURATION"] = 3
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024  # 1MB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db/qcm.db"
env_secret = os.getenv("FLASK_SECRET_KEY")
app.config["SECRET_KEY"] = env_secret if env_secret else "my_secret_key"

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
qr_code = QRcode(app)

if "sqlite" in app.config["SQLALCHEMY_DATABASE_URI"]:

    def _fk_pragma_on_connect(dbapi_con, con_record):
        dbapi_con.execute("pragma foreign_keys=ON")

    with app.app_context():
        from sqlalchemy import event

        event.listen(db.engine, "connect", _fk_pragma_on_connect)
