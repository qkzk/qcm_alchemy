"""
title: QCM parser
author: qkzk
date: 2021/06/28
"""
import re
from html import escape

import markdown

EXTENSIONS = ["fenced_code", "codehilite", "tables"]


def no_p_markdown(non_p_string) -> str:
    """
    Strip enclosing paragraph marks, <p> ... </p>,
    which markdown() forces, and which interfere with some jinja2 layout
    """
    return re.sub(
        "(^<P>|</P>$)",
        "",
        markdown.markdown(non_p_string, extensions=EXTENSIONS),
        flags=re.IGNORECASE,
    )


class ParseQCMError(Exception):
    """Exception raised when parsing went wrong."""

    pass


class ParseQCM:
    """
    Parse a QCM into a QCM class.
    Raise `ParseQCMError` if parsing went wrong.
    """

    def __init__(self, lines: list, mode="web", code_present: bool = False):
        self.lines = lines
        self.mode = mode
        self.title = self.read_title()
        self.parts = self.separate_parts()
        self.code_present = code_present

    def read_title(self):
        title = ""
        is_code_block = False
        for line in self.lines:
            if line.startswith("```"):
                is_code_block = not is_code_block
            if not is_code_block and "title: " in line and not "subtitle" in line:
                start = line.index(":") + 2
                title = escape(
                    line[start:-1].strip().replace('"', "").replace("''", "")
                )
            if not is_code_block and line.startswith("# "):
                title = no_p_markdown(line[2:])
        if not title:
            raise ParseQCMError("The QCM has no title.")
        return title

    def separate_parts(self) -> list:
        """Returns  the parts of the QCM"""
        end_header = self.find_end_header()
        start_end_parts = self.find_start_end_parts(end_header)
        return [self.read_part(start, end) for start, end in start_end_parts]

    def find_end_header(self) -> int:
        """Locate the end of the header ('---') in the markdown content"""
        end_header = 0
        for index, line in enumerate(self.lines):
            if index > 0 and line.startswith("---"):
                end_header = index
        return end_header

    def find_start_end_parts(self, end_header):
        """Locate the start and the end of the header in the file"""
        start_end_parts = []
        is_code_block = False
        for index, line in enumerate(self.lines[end_header:], start=end_header):
            if line.startswith("```"):
                is_code_block = not is_code_block
            if line.startswith("## ") and not is_code_block:
                start = index
                if start_end_parts != []:
                    start_end_parts[-1].append(start)
                start_end_parts.append([start])
        if not start_end_parts:
            raise ParseQCMError("The QCM has no parts")
        start_end_parts[-1].append(len(self.lines))
        return start_end_parts

    def read_header(self, end_header) -> str:
        """Read the header of the markdown file"""
        return "".join(self.lines[: end_header + 1])

    def read_part(self, start: int, end: int) -> "QCM_Part":
        """Returns a `QCM_Part` holding a part located between `start` and `end`"""
        return QCM_Part(self.lines[start:end], mode=self.mode)

    @classmethod
    def from_file(
        cls, input_filename: str, mode="web", code_present: bool = False
    ) -> "ParseQCM":
        """
        Open and read an utf-8 encoded QCM file, returns a parsed QCM.
        Raise various kinds of errors if the QCM isn't encoded properly.
        """
        with open(input_filename, encoding="utf-8") as file_content:
            return cls(
                file_content.readlines(),
                mode=mode,
                code_present=code_present,
            )

    @classmethod
    def from_file_into_dict(cls, input_filename: str, return_dict: dict, **kwargs):
        """
        Parse a QCM using with given parameters.

        Try to parse `input_filename`.
            If the parsing is done correctly, stores it into `return_dict["qcm"]`
            Else, stores the Exception into `return_dict["error"]`

        This interface is there to allow parsing from a Process.
        """
        mode = kwargs.get("mode", "web")
        code_present = kwargs.get("code_present", False)
        try:
            qcm = cls.from_file(input_filename, mode=mode, code_present=code_present)
            return_dict["qcm"] = qcm
        except (ParseQCMError, UnicodeDecodeError) as e:
            return_dict["error"] = e

    def __repr__(self):
        return "".join(map(repr, self.parts))


class QCM_PartError(ParseQCMError):
    """Exception raised when parsing a `QCM_Part` went wrong."""


class QCM_Part:
    """Holds a part of the QCM"""

    def __init__(self, lines: list, mode="web"):
        self.lines = lines
        self.mode = mode
        self.start_questions, self.title = self.read_title()
        self.questions_lines = self.read_questions()
        self.questions = [
            self.read_question(start, end) for start, end in self.questions_lines
        ]

    def __repr__(self):
        return "".join(self.lines)

    def read_title(self) -> tuple:
        """Read the title of the part and returns its position and content"""
        for index, line in enumerate(self.lines):
            if line.startswith("## "):
                return index + 1, escape(no_p_markdown(line[3:]))
        raise QCM_PartError(f"No title found for this part : {self}")

    def read_questions(self) -> list:
        """Returns a list of line indexes questions"""
        questions = []
        is_code_block = False
        for index, line in enumerate(
            self.lines[self.start_questions :], start=self.start_questions
        ):
            if line.startswith("```"):
                is_code_block = not is_code_block
            if line.startswith("### ") and not is_code_block:
                start = index
                if questions != []:
                    questions[-1].append(start)
                questions.append([start])
        if not questions:
            raise QCM_PartError("The part has no question.")
        questions[-1].append(len(self.lines))
        return questions

    def read_question(self, start: int, end: int) -> "QCM_Question":
        """Read a single questions, returns a `QCM_Question` object"""
        return QCM_Question(self.lines[start:end], mode=self.mode)


class QCM_QuestionError(ParseQCMError):
    """Raised when parsing a question went wrong"""


class QCM_Question:
    """Holds a set of questions"""

    def __init__(self, lines: list, mode="web"):
        self.lines = lines
        self.mode = mode
        self.start_text, self.question_title = self.read_title()
        self.text, self.end_text = self.read_text()
        self.is_text_question = False
        self.answers = self.read_answers()
        self.reject_wrong_question()

    def reject_wrong_question(self):
        """
        Raise QCM_QuestionError if the question has no valid answer and isn't a text question.
        """
        if not self.is_text_question and not self.has_valid_answers():
            raise QCM_QuestionError(
                "Question should be 'text question' or have at least one valid answers"
            )

    def has_valid_answers(self) -> bool:
        """True iff there's at least one valid answer"""
        return len([answer for answer in self.answers if answer.is_valid]) > 0

    def __repr__(self):
        return "/n".join(
            [self.question_title, self.text] + list(map(repr, self.answers))
        )

    def read_title(self) -> tuple:
        """read the title of the question from the string"""
        for index, line in enumerate(self.lines):
            if line.startswith("### "):
                return index + 1, no_p_markdown(line[4:])
        raise QCM_QuestionError(f"The question has no title")

    def read_text(self) -> tuple[str, int]:
        """
        Read the 'text' of the question, the lines below the title and
        before the answer.
        """
        for index, line in enumerate(
            self.lines[self.start_text :], start=self.start_text
        ):
            if line.startswith("- ["):
                end = index
                if self.mode == "web":
                    return (
                        markdown.markdown(
                            "".join(
                                self.lines[self.start_text : end],
                            ),
                            extensions=EXTENSIONS,
                        ),
                        end,
                    )
                elif self.mode == "pdf":
                    return "".join(self.lines[self.start_text : end]), end
        raise QCM_QuestionError(f"No text found for question {self}")

    def read_answers(self) -> list["QCM_Answer"]:
        """
        Returns a list of answers from the content.
        Set the `is_text_question` flag if it's a text question.

        if there's answers, it can't be a "text_question".
        """
        answers = []
        for line in self.lines[self.end_text :]:
            if line.startswith("- [t]"):
                self.is_text_question = True
                if answers:
                    raise QCM_QuestionError(
                        "Question can't be a `text_question` and have answers."
                    )
                return []
            elif line.startswith("- ["):
                answers.append(QCM_Answer.from_line(line))
        return answers


class QCM_Answer:
    """Holds an answer and a status, valid or not"""

    def __init__(self, text: str, is_valid: bool):
        self.text = text
        self.is_valid = is_valid

    @classmethod
    def from_line(cls, line: str) -> "QCM_Answer":
        """Creates an answer from a line starting with - [ ] or - [x]"""
        text = no_p_markdown(line[5:])
        is_valid = "[x]" in line[:5]
        return cls(text, is_valid)

    def __repr__(self):
        return f"    - [{'x' if self.is_valid else ' '}] {self.text}"
