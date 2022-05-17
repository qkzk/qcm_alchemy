from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, Length, NumberRange
from flask_wtf.file import FileAllowed, FileField, FileRequired


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Ce champ est requis."),
            Email(message="email invalide"),
        ],
        render_kw={"placeholder": "Email"},
    )
    clear_password = PasswordField(
        "Mot de passe",
        validators=[
            DataRequired(message="Ce champ est requis."),
        ],
        render_kw={"placeholder": "Mot de passe"},
    )


class NewPasswordForm(FlaskForm):
    current_password = PasswordField(
        "Actuel",
        validators=[
            DataRequired(message="Ce champ est requis."),
        ],
        render_kw={"placeholder": "Actuel"},
    )
    new_password = PasswordField(
        "Nouveau",
        validators=[
            DataRequired(message="Ce champ est requis."),
        ],
        render_kw={"placeholder": "Nouveau"},
    )


class NewTeacherForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Ce champ est requis."),
            Email(message="email invalide"),
        ],
        render_kw={"placeholder": "Email"},
    )
    clear_password = PasswordField(
        "Mot de passe",
        validators=[
            DataRequired(message="Ce champ est requis."),
            Length(
                min=8,
                max=250,
                message="Veuillez saisir un mot de passe entre 8 et 250 (lol) caractères",
            ),
        ],
        render_kw={"placeholder": "Mot de passe"},
    )


class ForgottenPasswordForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Ce champ est requis."),
            Email(message="email invalide"),
        ],
        render_kw={"placeholder": "Email"},
    )


class ResetPasswordForm(FlaskForm):
    clear_password = PasswordField(
        "Nouveau mot de passe",
        validators=[
            DataRequired(message="Ce champ est requis."),
            Length(
                min=8,
                max=250,
                message="Veuillez saisir un mot de passe entre 8 et 250 (lol) caractères",
            ),
        ],
        render_kw={"placeholder": "Nouveau mot de passe"},
    )


class StudentForm(FlaskForm):
    lastname = StringField(
        "Nom",
        validators=[
            DataRequired(message="Ce champ est requis."),
        ],
        render_kw={"placeholder": "Nom"},
    )
    firstname = StringField(
        "Prénom",
        validators=[
            DataRequired(message="Ce champ est requis."),
        ],
        render_kw={"placeholder": "Prénom"},
    )
    qcm_id = IntegerField(
        "Numéro",
        validators=[
            DataRequired(message="Ce champ est requis."),
            NumberRange(min=0, message="Le numéro est plus grand que 0."),
        ],
        render_kw={"placeholder": "Numéro"},
    )


class QcmFileForm(FlaskForm):
    source = FileField(
        "Envoyez un fichier source",
        validators=[
            FileRequired(),
            FileAllowed(["md"], message="Seulement des fichiers .md"),
        ],
    )