"""
title: sendmail
author: qkzk & google
date: 2021/05/20

Creates a gmail service with send credentials.
Send email with this service.
"""
from .fix_collections_import import collections

import base64
import mimetypes
import os.path
import re
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

TOKEN_PATH = "./tokens/token.json"
CREDS_PATH = "./tokens/credentials.json"

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def check_email(email: str) -> bool:
    """Check if an email has
    * exactly one @
    * at least one . after the @
    """
    return bool(EMAIL_REGEX.fullmatch(email))


class EmailSender:
    """
    Sent email with gmail.
    Uses `gmail.send` scopes.
    """

    def __init__(
        self, sender: str, to: str, subject: str, content: str, attachment=None
    ):
        self.sender = sender
        self.to = to
        self.subject = subject
        self.content = content
        self.service = self.__create_service()
        if attachment is None:
            self.message = self.__create_message()
        else:
            self.message = self.__create_message_with_attachment(attachment)

    @staticmethod
    def __create_service():
        """Creates a gmail service"""
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(TOKEN_PATH):
            creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(TOKEN_PATH, "w") as token:
                token.write(creds.to_json())

        return build("gmail", "v1", credentials=creds)

    def __create_message(self):
        """Create a message for an email.

        Args:
          sender: Email address of the sender.
          to: Email address of the receiver.
          subject: The subject of the email message.
          message_text: The text of the email message.

        Returns:
          An object containing a base64url encoded email object.
        """
        mime_message = MIMEMultipart()
        mime_message["to"] = self.to
        mime_message["subject"] = self.subject
        mime_message["from"] = self.sender
        mime_message.attach(MIMEText(self.content, "plain"))
        return {"raw": base64.urlsafe_b64encode(mime_message.as_bytes()).decode()}

    def __create_message_with_attachment(self, file):
        """Create a message for an email.

        Args:
          sender: Email address of the sender.
          to: Email address of the receiver.
          subject: The subject of the email message.
          message_text: The text of the email message.
          file: The path to the file to be attached.

        Returns:
          An object containing a base64url encoded email object.
        """
        # sender, to, subject, message_text, file):
        mime_message = MIMEMultipart()
        mime_message["to"] = self.to
        mime_message["from"] = self.sender
        mime_message["subject"] = self.subject

        mime_message.attach(MIMEText(self.content, "html"))
        mime_message.attach(MIMEText(self.content))
        content_type, encoding = mimetypes.guess_type(file)

        if content_type is None or encoding is not None:
            content_type = "application/octet-stream"
        main_type, sub_type = content_type.split("/", 1)
        if main_type == "text":
            with open(file, "r") as fp:
                msg = MIMEText(fp.read(), _subtype=sub_type)
        elif main_type == "image":
            with open(file, "rb") as fp:
                msg = MIMEImage(fp.read(), _subtype=sub_type)
        else:
            with open(file, "rb") as fp:
                msg = MIMEBase(main_type, _subtype=sub_type)
                msg.set_payload(fp.read())
        filename = os.path.basename(file)
        msg.add_header("Content-Disposition", "attachment", filename=filename)
        mime_message.attach(msg)
        return {"raw": base64.urlsafe_b64encode(mime_message.as_bytes()).decode()}

    def send_message(self) -> bool:
        """
        Try to send an email message. `True` iff the mail was sent successfully.

        Args:
          service: Authorized Gmail API service instance.
          user_id: User's email address. The special value "me"
          can be used to indicate the authenticated user.
          message: Message to be sent.

        Returns:
          Sent Message.
        """
        try:
            (
                self.service.users()
                .messages()
                .send(userId=self.sender, body=self.message)
                .execute()
            )
            return True
        except Exception as error:
            print("An error occurred: %s" % error)
            print(repr(error))
            print(error.__cause__)
            return False


def main():
    EmailSender(
        "qcm.serveur@lyceedesflandres.fr",
        "quentin.konieczko@lyceedesflandres.fr",
        "test",
        "content",
    ).send_message()


def test():
    emails = [
        "qu3nt1n@gmail.com",
        "bla@localhost.com",
        "m.maze@yahoo.fr",
        "aze+tag@bbc.uk.com",
        "aze@@qskdjf.fr",
        "azeaze@aze.fr",
    ]
    for email in emails:
        print(email, check_email(email))


if __name__ == "__main__":
    test()
