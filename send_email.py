# Crear contraseñas de aplicación https://support.google.com/mail/answer/185833?hl=es-419
import json
import smtplib
from html_file import crear_html
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:

    def __init__(self):

        with open(file=r"parameters_email.json", mode="r", encoding="utf-8") as file:
            parameters = json.load(file)

        self.email_smt = parameters["smtp_server"]
        self.sender_email_address = parameters["sender_email_user"]
        self.sender_email_app_password = parameters["sender_email_password"]
        self.email_message = None

    def create_email(self, message_body):

        matricula = message_body["matricula"]
        timestamp = message_body["timestamp"]
        subject = message_body["subject"]
        receiver = message_body["receiver"]
        content = message_body["content"]

        crear_html(matricula, timestamp, subject, receiver, content)

        # Read file containing html
        with open(file=r"html_body.html", mode="r", encoding="utf-8") as file_html:
            file_content = file_html.read()

        self.email_message = EmailMessage()
        # Configure email headers
        self.email_message['Subject'] = subject
        self.email_message['From'] = self.sender_email_address
        self.email_message['To'] = receiver
        # Set email content
        self.email_message.set_content(file_content, subtype='html')
        self.__send_message__()

    def __send_message__(self):
        # Set smtp server and port
        server = smtplib.SMTP(self.email_smt, 587)
        # Identify this client to the SMTP server
        server.ehlo()
        # Secure the SMTP connection
        server.starttls()
        # Login to email account
        server.login(self.sender_email_address, self.sender_email_app_password)
        # Send email
        server.send_message(self.email_message)
        # Close connection to server
        server.quit()
