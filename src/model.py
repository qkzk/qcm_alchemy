import csv
import os
from datetime import datetime, timedelta
from random import shuffle

from werkzeug.utils import secure_filename

from .parser import ParseQCM
from .create_app import app, db, ALLOWED_EXTENSIONS


class QcmPaserError(Exception):
    pass


class Qcm(db.Model):
    __tablename__ = "qcm"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    datetime = db.Column(db.DateTime)
    part = db.relationship(
        "QcmPart", back_populates="qcm", cascade="all,delete", passive_deletes=True
    )
    works = db.relationship(
        "Work", back_populates="qcm", cascade="all,delete", passive_deletes=True
    )

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

    def count_works(self) -> int:
        return len(self.works)

    @classmethod
    def clear_old_records(cls):
        now = datetime.now()
        two_days_ago = now - timedelta(minutes=2)
        cls.query.filter(cls.datetime < two_days_ago).delete()
        db.session.commit()

    def shuffled_parts(self):
        parts = list(self.part)
        shuffle(parts)
        return parts


class QcmPart(db.Model):
    __tablename__ = "qcm_part"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(100))
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
        questions = list(self.questions)
        shuffle(questions)
        return questions


class QcmPartQuestion(db.Model):
    __tablename__ = "qcm_part_question"
    id = db.Column("id", db.Integer, primary_key=True)
    question = db.Column(db.String(400))
    sub_text = db.Column(db.String(400))
    id_part = db.Column(
        "id_part", db.Integer, db.ForeignKey("qcm_part.id", ondelete="CASCADE")
    )
    part = db.relationship("QcmPart", back_populates="questions", passive_deletes=True)
    answers = db.relationship(
        "QcmPartQuestionAnswer",
        back_populates="question",
        cascade="all,delete",
        passive_deletes=True,
    )

    def shuffled_answers(self):
        answers = list(self.answers)
        shuffle(answers)
        return answers


class QcmPartQuestionAnswer(db.Model):
    __tablename__ = "qcm_part_question_answer"
    id = db.Column("id", db.Integer, primary_key=True)
    answer = db.Column(db.String(200))
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
        return f"QcmPartQuestionAnswer({self.answer}, {self.id_question})"

    def format(self) -> str:
        return self.answer


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column("id", db.Integer, primary_key=True)
    datetime = db.Column("datetime", db.DateTime)
    name = db.Column("name", db.String(100))
    works = db.relationship(
        "Work", back_populates="student", cascade="all,delete", passive_deletes=True
    )

    @classmethod
    def clear_old_records(cls):
        now = datetime.now()
        two_days_ago = now - timedelta(minutes=2)
        cls.query.filter(cls.datetime < two_days_ago).delete()
        db.session.commit()

    def __repr__(self):
        return f"Student({self.id}, {self.name})"


class Work(db.Model):
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
    qcm = db.relationship("Qcm", back_populates="works")
    student_qcm = db.UniqueConstraint("id_student", "id_qcm")
    points = db.Column("points", db.Integer)

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

    def count_points(self):
        self.points = sum(1 for choice in self.choices if choice.answer.is_valid)

    def __repr__(self):
        return f"Work({self.id}, {self.id_qcm}, {self.id_student})"

    @classmethod
    def write_export(cls, id_qcm: int) -> str:
        works = cls.query.filter_by(id_qcm=id_qcm).all()
        if works:
            filename = f"export-{id_qcm}.csv"
            with open(
                os.path.join(app.config["DOWNLOAD_FOLDER"], filename), "w"
            ) as csv_file:
                fieldnames = ["QCM_ID", "Titre", "Nom", "Points"]
                dictwriter = csv.DictWriter(csv_file, fieldnames=fieldnames)
                dictwriter.writeheader()
                for work in works:
                    dictwriter.writerow(
                        {
                            "QCM_ID": work.id_qcm,
                            "Titre": work.qcm.title,
                            "Nom": work.student.name,
                            "Points": work.points,
                        }
                    )

            return filename
        return ""


class Choice(db.Model):
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
        return f"Work({self.id}, {self.id_qcm}, {self.id_student})"


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
        full_path = os.path.join(
            app.config["UPLOAD_FOLDER"], secure_filename(file.filename)
        )
        self.filename = full_path
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
