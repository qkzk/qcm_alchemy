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


class ParseQCM:
    """Parse a QCM into a QCM class"""

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
        """open and read the file, returns a parsed QCM"""
        try:
            with open(input_filename) as file_content:
                return cls(
                    file_content.readlines(),
                    mode=mode,
                    code_present=code_present,
                )
        except:
            print("The first argument should be a correct filepath")
            raise

    def __repr__(self):
        return "".join(map(repr, self.parts))


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
        raise ValueError(f"No title found for this part : {self}")

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
        questions[-1].append(len(self.lines))
        return questions

    def read_question(self, start: int, end: int) -> "QCM_Question":
        """Read a single questions, returns a `QCM_Question` object"""
        return QCM_Question(self.lines[start:end], mode=self.mode)


class QCM_Question:
    """Holds a set of questions"""

    def __init__(self, lines: list, mode="web"):
        self.lines = lines
        self.mode = mode
        self.start_text, self.question_title = self.read_title()
        self.text, self.end_text = self.read_text()
        self.is_text_question = False
        self.answers = self.read_answers()

    def __repr__(self):
        return "/n".join(
            [self.question_title, self.text] + list(map(repr, self.answers))
        )

    def read_title(self) -> tuple:
        """read the title of the question from the string"""
        for index, line in enumerate(self.lines):
            if line.startswith("### "):
                return index + 1, no_p_markdown(line[4:])
        raise ValueError(f"No title found for this question : {self}")

    def read_text(self):
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
        raise ValueError(f"No text found for question {self}")

    def read_answers(self):
        """returns a list of answers from the content"""
        answers = []
        for line in self.lines[self.end_text :]:
            if line.startswith("- [t]"):
                self.is_text_question = True
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
