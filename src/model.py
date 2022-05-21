"""
title: model
author: qkzk
date: 2022/05/08

Models used in database and views.
"""
import csv
import os
import secrets
from datetime import datetime, timedelta
from random import randint, shuffle
from typing import Union

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from .parser import ParseQCM, QCM_Part, QCM_Question, QCM_Answer
from .create_app import app, db, ALLOWED_EXTENSIONS


def get_join_path_from_key(key: str, filename: str) -> str:
    """
    Returns the full path from  a valid `app` config key and a filename.
    """
    return os.path.join(os.getcwd(), app.config[key], filename)


class QcmParserError(Exception):
    pass


class Qcm(db.Model):
    """
    Root Qcm model.
    Its childen (`QcmPart`) holds questions which holds answers.
    It is created after the parsing of a .md file.
    """

    __tablename__ = "qcm"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.Text)
    datetime = db.Column(db.DateTime)
    id_teacher = db.Column(db.Integer, db.ForeignKey("teacher.id", ondelete="CASCADE"))
    teacher = db.relationship("Teacher", back_populates="qcms", passive_deletes=True)
    part = db.relationship(
        "QcmPart", back_populates="qcm", cascade="all,delete", passive_deletes=True
    )
    works = db.relationship(
        "Work", back_populates="qcm", cascade="all,delete", passive_deletes=True
    )

    @classmethod
    def from_parser(cls, parsed_qcm: ParseQCM, id_teacher) -> "Qcm":
        """
        Creates a Qcm instance from a parsed QCM.md file.
        Raise `QcmPaserError` if anything went wrong.
        """
        try:
            qcm = Qcm(
                title=parsed_qcm.title,
                datetime=datetime.now(),
                id_teacher=id_teacher,
            )
            for parsed_part in parsed_qcm.parts:
                qcm.part.append(QcmPart.from_parser(parsed_part))
            return qcm
        except Exception as e:
            raise QcmParserError(repr(e))

    def format(self):
        s = f"{self.id} - {self.title}"
        for part in self.part:
            s += f"\n   {part.title}"
            for question in part.questions:
                s += f"\n        {question.question}"
                s += f"\n        {question.sub_text}"
                for answer in question.answers:
                    s += f"\n            {answer.answer}"
                    s += f"\n            {answer.is_valid}"
        return s

    def count_works(self) -> int:
        """Returns the number of recorded works for this QCM"""
        return len(self.works)

    def has_works(self) -> bool:
        """True iff there's submitted works for this QCM"""
        return self.count_works() > 0

    @classmethod
    def clear_old_records(cls):
        """Self cleaning of the database. Uses the ForeignKey to clean children as well."""
        now = datetime.now()
        two_days_ago = now - timedelta(hours=48)
        cls.query.filter(cls.datetime < two_days_ago).delete()
        db.session.commit()

    def shuffled_parts(self):
        """
        Shuffle the parts to randomize the QCM.
        Used by the view to creates different work for students.
        """
        parts = list(self.part)
        shuffle(parts)
        return parts

    def flat_questions_formatted(self):
        """Returns a flat list of every of this QCM question, formatted."""
        return [question.format() for part in self.part for question in part.questions]

    def remove_and_commit(self):
        """
        Remove the `self` QCM and commit.
        Since all tables implement `ON DELETE CASCADE` it will also
        delete all parts, questions, answers and related works submitted by students.
        """
        db.session.delete(self)
        db.session.commit()

    def datetime_formated(self) -> str:
        return self.datetime.strftime("%a %d %b %Y - %H:%M")


class QcmPart(db.Model):
    """
    Holds the part of a QCM. A part is a `## title` and its following `### questions`.
    """

    __tablename__ = "qcm_part"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.Text)
    id_qcm = db.Column(
        "id_qcm", db.Integer, db.ForeignKey("qcm.id", ondelete="CASCADE")
    )
    qcm = db.relationship("Qcm", back_populates="part", passive_deletes=True)
    questions = db.relationship(
        "QcmPartQuestion",
        back_populates="part",
        cascade="all,delete",
        passive_deletes=True,
    )

    def shuffled_questions(self):
        """Shuffle its questions to randomize for the student view."""
        questions = list(self.questions)
        shuffle(questions)
        return questions

    @classmethod
    def from_parser(cls, parsed_part: QCM_Part) -> "QcmPart":
        """Creates a database part from  a parsed part."""
        part = cls(title=parsed_part.title)

        for parsed_question in parsed_part.questions:
            part.questions.append(QcmPartQuestion.from_parser(parsed_question))
        return part


class QcmPartQuestion(db.Model):
    """
    Holds a Question.
    A Question starts with `### question`, followed by an optional string,
    then a single line with:
        `- [t]` wich is a question whose answer is a text provided by the student.
     or a list of
        `- [ ] wrong answer` or
        `- [x] valid answer.` or
    """

    __tablename__ = "qcm_part_question"
    id = db.Column("id", db.Integer, primary_key=True)
    question = db.Column(db.Text)
    sub_text = db.Column(db.Text)
    id_part = db.Column(
        "id_part", db.Integer, db.ForeignKey("qcm_part.id", ondelete="CASCADE")
    )
    is_text_question = db.Column(db.Boolean)
    part = db.relationship("QcmPart", back_populates="questions", passive_deletes=True)
    answers = db.relationship(
        "QcmPartQuestionAnswer",
        back_populates="question",
        cascade="all,delete",
        passive_deletes=True,
    )
    texts = db.relationship(
        "Text",
        back_populates="question",
        cascade="all,delete",
        passive_deletes=True,
    )

    def shuffled_answers(self):
        """Shuffle the answers to randomize the test."""
        answers = list(self.answers)
        shuffle(answers)
        return answers

    @classmethod
    def from_parser(cls, parsed_question: QCM_Question) -> "QcmPartQuestion":
        """Creates a database record Question from  a parsed question."""
        question = cls(
            question=parsed_question.question_title,
            sub_text=parsed_question.text,
            is_text_question=parsed_question.is_text_question,
        )
        for parsed_answer in parsed_question.answers:
            question.answers.append(QcmPartQuestionAnswer.from_parser(parsed_answer))
        return question

    def __repr__(self):
        return f"QcmPartQuestion({self.question}, {self.sub_text}, {self.id_part})"

    def format(self):
        return f"{self.question} {self.sub_text}"


class QcmPartQuestionAnswer(db.Model):
    """
    Holds an answer.
    An answer is a choice which can be right or wrong.
    It may hold some LaTex or some inline code : `$1+1=2`, `1+1 == 2`.
    """

    __tablename__ = "qcm_part_question_answer"
    id = db.Column("id", db.Integer, primary_key=True)
    answer = db.Column("answer", db.Text)
    id_question = db.Column(
        "id_question",
        db.Integer,
        db.ForeignKey(
            "qcm_part_question.id",
            ondelete="CASCADE",
        ),
    )
    is_valid = db.Column("is_valid", db.Boolean)
    question = db.relationship(
        "QcmPartQuestion", back_populates="answers", passive_deletes=True
    )
    choices = db.relationship("Choice", back_populates="answer", passive_deletes=True)

    def __repr__(self):
        return (
            f"QcmPartQuestionAnswer({self.answer}, {self.id_question}, {self.is_valid})"
        )

    def format(self) -> str:
        return self.answer

    @classmethod
    def from_parser(cls, parsed_answer: QCM_Answer) -> "QcmPartQuestionAnswer":
        """Creates an answer record from a parsed answer."""
        return cls(answer=parsed_answer.text, is_valid=parsed_answer.is_valid)


class Student(db.Model):
    """
    Holds the information about our students.
    We records only their name and their answers. Thoses answers can't be retrieved yet.
    All we can do is get their score.
    """

    __tablename__ = "student"
    id = db.Column("id", db.Integer, primary_key=True)
    datetime = db.Column("datetime", db.DateTime)
    name = db.Column("name", db.String(100))
    works = db.relationship(
        "Work", back_populates="student", cascade="all,delete", passive_deletes=True
    )
    id_teacher = db.Column(db.Integer, db.ForeignKey("teacher.id", ondelete="CASCADE"))
    teacher = db.relationship(
        "Teacher", back_populates="students", passive_deletes=True
    )

    @classmethod
    def clear_old_records(cls):
        """Self cleaning purpose. Delete every old student and its children (Work)."""
        now = datetime.now()
        two_days_ago = now - timedelta(hours=48)
        cls.query.filter(cls.datetime < two_days_ago).delete()
        db.session.commit()

    @classmethod
    def find_or_add_student(cls, student_name: str) -> "Student":
        """
        Returns a student instance with given student_name
        If there's exactly one, returns it.
        If no student is found with this name or there's multiple students :
            creates a new one and commit.
        """
        students = cls.query.filter_by(name=student_name).all()
        if len(students) == 1:
            student = students[0]
        else:
            if len(students) > 1:
                # make a new student with variation of name
                student_name += str(randint(1, 9))
            # add the new student to database
            student = Student(name=student_name, datetime=datetime.now())
            db.session.add(student)
            db.session.commit()
        return student

    def __repr__(self):
        return f"Student({self.id}, {self.name})"


class Work(db.Model):
    """
    Holds the choices and text answers made in the QCM form by a Student.
    """

    __tablename__ = "work"
    id = db.Column("id", db.Integer, primary_key=True)
    id_qcm = db.Column(
        "id_qcm", db.Integer, db.ForeignKey("qcm.id", ondelete="CASCADE")
    )
    id_student = db.Column(
        "id_student", db.Integer, db.ForeignKey("student.id", ondelete="CASCADE")
    )
    student = db.relationship("Student", back_populates="works")
    choices = db.relationship(
        "Choice", back_populates="work", cascade="all,delete", passive_deletes=True
    )
    datetime = db.Column("datetime", db.DateTime)
    is_submitted = db.Column("is_submitted", db.Boolean)
    qcm = db.relationship("Qcm", back_populates="works")
    student_qcm = db.UniqueConstraint("id_student", "id_qcm")
    is_text = db.Column("is_text", db.Boolean)
    points = db.Column("points", db.Integer)
    texts = db.relationship(
        "Text", back_populates="work", cascade="all,delete", passive_deletes=True
    )

    _fieldnames = ["Nom", "Points", "Horaire"]

    @classmethod
    def create_and_commit(cls, id_qcm: int, id_student: int) -> "Work":
        """Returns a `Work` instance extracted from a POST form"""

        work = cls(
            id_qcm=id_qcm,
            id_student=id_student,
            datetime=datetime.now(),
            is_submitted=False,
        )
        db.session.add(work)
        db.session.commit()
        return work

    def count_points(self):
        """Used to count the right choices made by the student."""
        self.points = sum(1 for choice in self.choices if choice.answer.is_valid)

    def __repr__(self):
        return f"Work({self.id}, {self.id_qcm}, {self.id_student})"

    def format_dict(self) -> dict:
        """Format itself into a dict for exporting as CSV file."""
        row = {
            "Nom": self.student.name,
            "Points": self.points,
            "Horaire": self.datetime,
        }
        for choice in self.choices:
            row[choice.answer.question.format()] = [choice.answer.answer]
        for text in self.texts:
            row[text.question.format()] = [text.text]

        return row

    def datetime_formated(self) -> str:
        return self.datetime.strftime("%a %d %b %Y - %H:%M")

    @property
    def fieldnames(self) -> list:
        """Creates a fiednames list."""
        return self._fieldnames + self.qcm.flat_questions_formatted()

    def format_title(self) -> str:
        """Format itself into a title line for exporting as CSV file."""
        return f"id_qcm: {self.qcm.id} - Titre: {self.qcm.title} - Crée: {self.qcm.datetime}\n"

    @classmethod
    def write_export(cls, id_qcm: int) -> str:
        """
        Returns a `csv` content with the marks of every student who answered a QCM.
        """
        works = cls.query.filter_by(id_qcm=id_qcm).all()
        if works:
            filename = f"export-{id_qcm}.csv"
            fullpath = get_join_path_from_key("DOWNLOAD_FOLDER", filename)
            with open(fullpath, "w", encoding="utf-8") as csv_file:
                csv_file.write(works[0].format_title())
                dictwriter = csv.DictWriter(csv_file, fieldnames=works[0].fieldnames)
                dictwriter.writeheader()
                for work in works:
                    dictwriter.writerow(work.format_dict())

            print("write_export", fullpath, filename)
            return filename
        return ""

    def get_text(self, id_question: int) -> str:
        """Returns the textarea answer for a given `id_question`"""
        text_answer = Text.query.filter_by(
            id_work=self.id, id_question=id_question
        ).first()
        if text_answer is None:
            return ""
        return text_answer.text

    def is_correct(self, id_answser: int) -> bool:
        """True iff the choice made is correct"""
        return QcmPartQuestionAnswer.query.get(id_answser).is_valid

    def is_selected(self, id_question, id_answer):
        """
        True iff the answer `id_answer` is selected by a student
        for a question `id_question`.
        """
        for choice in self.choices:
            if choice.id_question == id_question and choice.id_answer == id_answer:
                return True
        return False

    def record(self):
        """Mark the work as submitted, count the points and commit."""
        self.is_submitted = True
        self.count_points()
        db.session.commit()


class Choice(db.Model):
    """
    A choice made by a Student.
    We only know who made the choice, what Answer the student choosed and which QCM
    the student was answering to.
    """

    __tablename__ = "choice"
    id = db.Column("id", db.Integer, primary_key=True)
    id_work = db.Column(
        "id_work", db.Integer, db.ForeignKey("work.id", ondelete="CASCADE")
    )
    id_question = db.Column(
        "id_question",
        db.Integer,
        db.ForeignKey("qcm_part_question.id", ondelete="CASCADE"),
    )
    id_answer = db.Column(
        "id_answer",
        db.Integer,
        db.ForeignKey("qcm_part_question_answer.id", ondelete="CASCADE"),
    )
    work = db.relationship("Work", back_populates="choices", passive_deletes=True)
    work_question_answer = db.UniqueConstraint("id_work", "id_question", "id_answer")
    answer = db.relationship(
        "QcmPartQuestionAnswer", back_populates="choices", passive_deletes=True
    )

    def __repr__(self):
        return (
            f"Choice({self.id}, {self.id_work}, {self.id_question}, {self.id_answer})"
        )


class Text(db.Model):
    """
    A text typed by a student in a `<textarea>` form field.
    """

    __tablename__ = "text"
    id = db.Column("id", db.Integer, primary_key=True)
    text = db.Column("text", db.Text)
    id_work = db.Column(
        "id_work", db.Integer, db.ForeignKey("work.id", ondelete="CASCADE")
    )
    id_question = db.Column(
        "id_question",
        db.Integer,
        db.ForeignKey("qcm_part_question.id", ondelete="CASCADE"),
    )
    work = db.relationship("Work", back_populates="texts", passive_deletes=True)
    question = db.relationship(
        "QcmPartQuestion", back_populates="texts", passive_deletes=True
    )
    work_question = db.UniqueConstraint("id_work", "id_question")

    def __repr__(self):
        return f"Text({self.id}, {self.id_work}, {self.id_question}, {self.text})"


class Teacher(UserMixin, db.Model):
    """
    A teacher.
    They must have :
    * (unique) email,
    * password,

    They have :
    * students,
    * qcms
    """

    __tablename__ = "teacher"
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.String(120), unique=True, nullable=False)
    password = db.Column("password", db.String(120), nullable=False)
    is_confirmed = db.Column("is_confirmed", db.Boolean)
    qcms = db.relationship(
        "Qcm", back_populates="teacher", cascade="all,delete", passive_deletes=True
    )
    keys = db.relationship(
        "ResetKey", back_populates="teacher", cascade="all,delete", passive_deletes=True
    )
    confirmation_keys = db.relationship(
        "EmailConfirmation",
        back_populates="teacher",
        cascade="all,delete",
        passive_deletes=True,
    )
    students = db.relationship(
        "Student",
        back_populates="teacher",
        cascade="all,delete",
        passive_deletes=True,
    )

    @classmethod
    def get_from_email(cls, email: str) -> Union["Teacher", None]:
        """
        Get a teacher with that email. Returns `None` if they're not found.
        """
        teachers = cls.query.filter_by(email=email).all()
        if not teachers:
            print("No teacher with email", email)
            return None
        if len(teachers) != 1:
            print("Multiple teachers with email", email, teachers)
            return None
        return teachers[0]

    def check_password_hash(self, clear_password):
        """
        Used to check password from clear password and hashed password.
        """
        return check_password_hash(self.password, clear_password)

    @classmethod
    def insert(cls, email: str, clear_password: str) -> Union["Teacher", None]:
        """
        Insert a new teacher in DB and commit.
        Returns `None` if a teacher with same email already exists.
        """
        if cls.get_from_email(email) is not None:
            print(f"teacher {email} already exists.")
            return None
        password = generate_password_hash(clear_password)
        teacher = Teacher(email=email, password=password)
        db.session.add(teacher)
        db.session.commit()
        print(f"successfully inserted {teacher} in database.")
        return teacher

    def update_password_and_commit(self, clear_password):
        """Update password"""
        self.password = generate_password_hash(clear_password)
        db.session.commit()

    def remove_and_commit(self):
        """
        Remove the `self` account and commit.
        Since all tables implement `ON DELETE CASCADE` it will also
        delete all QCM and related works submitted by the teacher.
        """
        db.session.delete(self)
        db.session.commit()

    def confirm_email(self):
        """Confirm the email of a teacher."""
        self.is_confirmed = True
        db.session.commit()

    def is_owner(self, qcm: Qcm) -> bool:
        """True iff the QCM is owned by the teacher"""
        return qcm.id_teacher == self.id

    def __repr__(self):
        return f"Teacher({self.email})"


class ResetKey(db.Model):
    """
    Holds the reset key
    """

    __tablename__ = "reset_key"
    id = db.Column("id", db.Integer, primary_key=True)
    key = db.Column("key", db.Text, nullable=False)
    id_teacher = db.Column(
        "id_teacher",
        db.Integer,
        db.ForeignKey("teacher.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )
    datetime = db.Column("datetime", db.DateTime)
    teacher = db.relationship("Teacher", back_populates="keys", passive_deletes=True)

    @classmethod
    def remove_key(cls, id_teacher: int):
        """Remove keys for this id_teacher. Commit"""
        cls.query.filter_by(id_teacher=id_teacher).delete()
        db.session.commit()

    @classmethod
    def from_id_teacher(cls, id_teacher: int) -> Union[None, "ResetKey"]:
        """Returns a teacher if there's one with a key."""
        keys = cls.query.filter_by(id_teacher=id_teacher).all()
        if not keys:
            return None
        if len(keys) > 1:
            return None
        return keys[0]

    @classmethod
    def key_match(cls, id_teacher, key) -> bool:
        """True iff the key match"""
        keys = cls.query.filter_by(key=key, id_teacher=id_teacher).all()
        if not len(keys) == 1:
            return False
        key = keys[0]
        return (datetime.now() - key.datetime).total_seconds() < 3600

    @classmethod
    def clear_old_records(cls) -> None:
        """Self cleaning purpose. Delete every old keys. Commit."""
        now = datetime.now()
        three_hours_ago = now - timedelta(hours=3)
        cls.query.filter(cls.datetime < three_hours_ago).delete()
        db.session.commit()

    @classmethod
    def clear(cls, id_teacher) -> type:
        """Remove all keys for `id_teacher` and return its class"""
        cls.remove_key(id_teacher)
        return cls

    @classmethod
    def new(cls, id_teacher) -> "ResetKey":
        """Creates a new element. Doesn't commit."""
        key = secrets.token_urlsafe(16)
        return cls(key=key, id_teacher=id_teacher, datetime=datetime.now())


class EmailConfirmation(db.Model):
    """
    Holds the confirmation key
    """

    __tablename__ = "confirmation_key"
    id = db.Column("id", db.Integer, primary_key=True)
    key = db.Column("key", db.Text, nullable=False)
    id_teacher = db.Column(
        "id_teacher",
        db.Integer,
        db.ForeignKey("teacher.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )
    datetime = db.Column("datetime", db.DateTime)
    teacher = db.relationship(
        "Teacher", back_populates="confirmation_keys", passive_deletes=True
    )

    @classmethod
    def remove_key(cls, id_teacher: int):
        """Remove all keys for this id_teacher and commit."""
        keys = cls.query.filter_by(id_teacher=id_teacher).delete()
        db.session.commit()

    @classmethod
    def from_id_teacher(cls, id_teacher) -> Union[None, "EmailConfirmation"]:
        """Find a teacher if there's one with this key"""
        keys = cls.query.filter_by(id_teacher=id_teacher).all()
        if not keys:
            return None
        if len(keys) > 1:
            return None
        return keys[0]

    @classmethod
    def key_match(cls, id_teacher, key) -> bool:
        """True iff the key match"""
        keys = cls.query.filter_by(key=key, id_teacher=id_teacher).all()
        if not len(keys) == 1:
            return False
        key = keys[0]
        return (datetime.now() - key.datetime).total_seconds() < 3600

    @classmethod
    def clear_old_records(cls) -> None:
        """Self cleaning purpose. Delete every old keys."""
        now = datetime.now()
        three_hours_ago = now - timedelta(hours=3)
        cls.query.filter(cls.datetime < three_hours_ago).delete()
        db.session.commit()

    @classmethod
    def clear(cls, id_teacher) -> type:
        """Remove all keys for `id_teacher` and return its class"""
        cls.remove_key(id_teacher)
        return cls

    @classmethod
    def new(cls, id_teacher: int) -> "EmailConfirmation":
        """Creates a new element. Doesn't commit."""
        key = secrets.token_urlsafe(16)
        return cls(key=key, id_teacher=id_teacher, datetime=datetime.now())


class QcmFileError(Exception):
    pass


class QcmFile:
    """
    Holds a QcmFile.
    It should be a valid markdown file uploaded by a teacher.
    If it's parsed correctly we send it to the db.
    """

    def __init__(self, file: "werkzeug.datastructures.FileStorage"):
        self.filename: str
        self.file = file
        self.save_file(file)

    def save_file(self, file: "werkzeug.datastructures.FileStorage"):
        full_path = os.path.join(
            app.config["UPLOAD_FOLDER"], secure_filename(file.filename)
        )
        self.filename = full_path
        self.file.save(self.filename)

    @classmethod
    def validate_file(cls, file: "werkzeug.datastructures.FileStorage") -> tuple:
        """
        Returns the couple (is_valid, message) where `is_valid` is `True` iff we could
        parse the content. The error message is used by the view to inform the teacher
        of the error : invalid filetype, file not found, error while parsing.
        """
        is_valid = True
        message = ""

        if not file or file.filename == "":
            is_valid = False
            message = "Fichier introuvable"
        elif not cls.validate_filename(file):
            is_valid = False
            message = "Fichier invalide"

        return is_valid, message

    @staticmethod
    def validate_filename(file: "werkzeug.datastructures.FileStorage") -> bool:
        """True if the file has only one `"."` in its name and its extension is `.md`"""
        return (
            "." in file.filename
            and file.filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )

    @classmethod
    def from_file(cls, file: "werkzeug.datastructures.FileStorage") -> "QcmFile":
        """
        Creates a QcmFile from a markdown file.
        Raise `QcmFileError` if it's impossible.
        """
        try:
            return cls(file)
        except Exception as e:
            print(repr(e))
            raise QcmFileError(repr(e))

    def __repr__(self):
        return f"Qcm({self.file})"


##################################################################################
##################################################################################
#                    WRITE CRAPPY TESTS BELOW THIS LINE
##################################################################################
##################################################################################
