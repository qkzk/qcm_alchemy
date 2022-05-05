import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from .parser import ParseQCM

app = Flask(__name__)
UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = {"md"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db/qcm.db"
app.config["SECRET_KEY"] = "random string"

db = SQLAlchemy(app)


class QcmPaserError(Exception):
    pass


class Qcm(db.Model):
    __tablename__ = "qcm"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    datetime = db.Column(db.DateTime)
    part = db.relationship("QcmPart", back_populates="qcm")
    works = db.relationship("Work", back_populates="qcm")

    @classmethod
    def from_parsed_qcm(cls, parsed_qcm: ParseQCM) -> "Qcm":
        try:
            qcm = Qcm(title=parsed_qcm.title, datetime=datetime.now())
            for parsed_part in parsed_qcm.parts:
                part = QcmPart(title=parsed_part.title)
                qcm.part.append(part)

                for parsed_question in parsed_part.questions:
                    question = QcmPartQuestion(
                        question=parsed_question.question_title,
                        sub_text=parsed_question.text,
                    )
                    part.questions.append(question)

                    for parsed_answer in parsed_question.answers:
                        parsed_answer = QcmPartQuestionAnswer(
                            answer=parsed_answer.text, is_valid=parsed_answer.is_valid
                        )
                        question.answers.append(parsed_answer)
            return qcm
        except Exception as e:
            raise QcmPaserError(repr(e))

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


class QcmPart(db.Model):
    __tablename__ = "qcm_part"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    id_qcm = db.Column("id_qcm", db.Integer, db.ForeignKey("qcm.id"))
    qcm = db.relationship("Qcm", back_populates="part")
    questions = db.relationship("QcmPartQuestion", back_populates="part")


class QcmPartQuestion(db.Model):
    __tablename__ = "qcm_part_question"
    id = db.Column("id", db.Integer, primary_key=True)
    question = db.Column(db.String(400))
    sub_text = db.Column(db.String(400))
    id_part = db.Column("id_part", db.Integer, db.ForeignKey("qcm_part.id"))
    part = db.relationship("QcmPart", back_populates="questions")
    answers = db.relationship("QcmPartQuestionAnswer", back_populates="question")


class QcmPartQuestionAnswer(db.Model):
    __tablename__ = "qcm_part_question_answer"
    id = db.Column("id", db.Integer, primary_key=True)
    answer = db.Column(db.String(200))
    id_question = db.Column(
        "id_question", db.Integer, db.ForeignKey("qcm_part_question.id")
    )
    is_valid = db.Column("is_valid", db.Boolean)
    question = db.relationship("QcmPartQuestion", back_populates="answers")

    def __repr__(self):
        return f"QcmPartQuestionAnswer({self.answer}, {self.id_question})"

    def format(self) -> str:
        return self.answer


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    works = db.relationship("Work", back_populates="student")

    def __repr__(self):
        return f"Student({self.id}, {self.name})"


class Work(db.Model):
    __tablename__ = "work"
    id = db.Column("id", db.Integer, primary_key=True)
    id_qcm = db.Column("id_qcm", db.Integer, db.ForeignKey("qcm.id"))
    id_student = db.Column("id_student", db.Integer, db.ForeignKey("student.id"))
    student = db.relationship("Student", back_populates="works")
    choices = db.relationship("Choice", back_populates="work")
    qcm = db.relationship("Qcm", back_populates="works")
    student_qcm = db.UniqueConstraint("id_student", "id_qcm")

    @classmethod
    def from_form(cls, id_qcm: int, id_student: int, parsed_choices: list[dict]):
        work = Work(id_qcm=id_qcm, id_student=id_student)
        for parsed_choice in parsed_choices:
            choice = Choice(
                id_question=parsed_choice["id_question"],
                id_answer=parsed_choice["id_answer"],
            )
            work.choices.append(choice)
        return work

    def __repr__(self):
        return f"Work({self.id}, {self.id_qcm}, {self.id_student})"


class Choice(db.Model):
    __tablename__ = "choice"
    id = db.Column("id", db.Integer, primary_key=True)
    id_work = db.Column("id_work", db.Integer, db.ForeignKey("work.id"))
    id_question = db.Column(
        "id_question", db.Integer, db.ForeignKey("qcm_part_question.id")
    )
    id_answer = db.Column(
        "id_answer", db.Integer, db.ForeignKey("qcm_part_question_answer.id")
    )
    work = db.relationship("Work", back_populates="choices")

    def __repr__(self):
        return f"Work({self.id}, {self.id_qcm}, {self.id_student})"


class Marks(db.Model):
    __tablename__ = "marks"
    id = db.Column("mark_id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    qcm_id = db.Column(db.String(50))
    answers = db.Column(db.String(400))
    points = db.Column(db.Integer)

    def __init__(self, name, qcm_id, answers, points):
        self.name = name
        self.qcm_id = qcm_id
        self.answers = answers
        self.points = points

    @staticmethod
    def validate_form(form: dict) -> bool:
        return all(("name" in form, "qcm_id" in form, "answers" in form))

    @classmethod
    def from_form(cls, form: dict) -> "Marks":
        name = form["name"]
        qcm_id = form["qcm_id"]
        answers = form["answers"]
        points = cls.calc_total(qcm_id, answers)
        return cls(name, qcm_id, answers, points)

    @classmethod
    def calc_total(cls, qcm_id, answers) -> int:
        return 0

    def __repr__(self):
        return f"Marks({self.id}, {self.name}, {self.qcm_id}, {self.total})"


class QcmFileError(Exception):
    pass


class QcmFile:
    def __init__(self, file: "werkzeug.datastructures.FileStorage"):
        self.filename: str
        self.file = file
        self.save_file(file)
        # TODO parsing
        print("parsing...")

    def save_file(self, file: "werkzeug.datastructures.FileStorage"):
        self.filename = os.path.join(
            app.config["UPLOAD_FOLDER"], secure_filename(file.filename)
        )
        self.file.save(self.filename)

    @classmethod
    def validate_file(cls, file: "werkzeug.datastructures.FileStorage") -> tuple:
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
        return (
            "." in file.filename
            and file.filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )

    @classmethod
    def from_file(cls, file: "werkzeug.datastructures.FileStorage") -> "QcmFile":
        try:
            return cls(file)
        except Exception as e:
            print(repr(e))
            raise QcmFileError(repr(e))

    def flash_message_ok(self):
        return f"Fichier uploadé dans {self.__repr__()}"

    def __repr__(self):
        return f"Qcm({self.file})"


##################################################################################
##################################################################################
#                    WRITE CRAPPY TESTS BELOW THIS LINE
##################################################################################
##################################################################################


def test_parser():
    db.create_all()

    parsed_qcm = ParseQCM.from_file(
        "uploads/test_nocode.md", mode="web", code_present=False
    )

    print(parsed_qcm)

    qcm = Qcm(title=parsed_qcm.title)
    for parsed_part in parsed_qcm.parts:
        part = QcmPart(title=parsed_part.title)
        qcm.part.append(part)

        for parsed_question in parsed_part.questions:
            question = QcmPartQuestion(
                question=parsed_question.question_title, sub_text=parsed_question.text
            )
            part.questions.append(question)

            for parsed_answer in parsed_question.answers:
                parsed_answer = QcmPartQuestionAnswer(
                    answer=parsed_answer.text, is_valid=parsed_answer.is_valid
                )
                question.answers.append(parsed_answer)

    db.session.add(qcm)
    db.session.commit()


def test_choicer():
    db.create_all()

    student = Student(name="Robert")
    db.session.add(student)
    db.session.commit()
    robert = Student.query.get(1)
    print(robert)

    id_qcm = 1
    parsed_choices = [
        {"id_question": 1, "id_answer": 1},
        {"id_question": 2, "id_answer": 7},
    ]
    work = Work.from_form(id_qcm, robert.id, parsed_choices)
    db.session.add(work)
    db.session.commit()


# test_parser()
# test_choicer()
