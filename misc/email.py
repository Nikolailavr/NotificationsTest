from fastapi import BackgroundTasks

from env.env import EmailSettings
from fastapi_mail import ConnectionConfig, MessageSchema, FastMail, MessageType

conf = ConnectionConfig(
    MAIL_USERNAME=EmailSettings.LOGIN,
    MAIL_PASSWORD=EmailSettings.PASSWORD,
    MAIL_FROM=EmailSettings.EMAIL,
    MAIL_PORT=EmailSettings.PORT,
    MAIL_SERVER=EmailSettings.HOST,
    MAIL_FROM_NAME=EmailSettings.NAME,
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    TEMPLATE_FOLDER='./templates',
)


def send_email(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        template_body=body,
        subtype=MessageType.html,
    )
    fm = FastMail(conf)
    background_tasks.add_task(
        fm.send_message, message, template_name='email.html')
