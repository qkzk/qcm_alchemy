from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.file import FileField, FileRequired


class MyForm(FlaskForm):
    name = StringField(
        "name",
        validators=[
            DataRequired(message="Ce champ est requis."),
            Length(min=8, message="Veuillez saisir un nom de 8 caractères blablal"),
        ],
    )


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Ce champ est requis."),
            Email(message="email invalide"),
        ],
    )
    clear_password = PasswordField(
        "Mot de passe",
        validators=[
            DataRequired(message="Ce champ est requis."),
        ],
    )


class NewPasswordForm(FlaskForm):
    current_password = PasswordField(
        "Actuel",
        validators=[
            DataRequired(message="Ce champ est requis."),
        ],
    )
    new_password = PasswordField(
        "Nouveau",
        validators=[
            DataRequired(message="Ce champ est requis."),
        ],
    )


class NewTeacherForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Ce champ est requis."),
            Email(message="email invalide"),
        ],
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
    )


class ForgottenPasswordForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Ce champ est requis."),
            Email(message="email invalide"),
        ],
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
    )
