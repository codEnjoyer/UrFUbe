import smtplib
from email.message import EmailMessage
from auth.schemas import UserRead
from config import SMTP_PASS, SMTP_USER, SMTP_PORT, SMTP_HOST


def _get_welcome_email_template(user: UserRead):
    e_msg = EmailMessage()
    e_msg['Subject'] = 'Приветственное письмо'
    e_msg['From'] = SMTP_USER
    e_msg['To'] = user.email

    e_msg.set_content(
        '<div>'
        f'<h1>Здравствуйте, {user.username}, спасибо за регистрацию!</h1>'
        '<img src="https://images.unsplash.com/photo-1460467820054-c87ab43e9b59?ixlib=rb-4.0.3&ixid'
        '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1067&q=80" width="600">'
        '</div>',
        subtype='html'
    )
    return e_msg


def send_welcome_email(user: UserRead):
    msg = _get_welcome_email_template(user)
    send_email(msg)


def send_email(msg: EmailMessage):
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
