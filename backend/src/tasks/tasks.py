import smtplib
from email.message import EmailMessage
from auth.schemas import UserRead
from config import SMTP_PASS, SMTP_USER, SMTP_PORT, SMTP_HOST  # ,BROKER_PASS, BROKER_HOSTNAME, BROKER_PORT


# from celery import Celery

def get_welcome_email_template(user: UserRead):
    e_msg = EmailMessage()
    e_msg['Subject'] = 'Приветственное письмо'
    e_msg['From'] = SMTP_USER
    e_msg['To'] = user.email

    e_msg.set_content(
        '<div>'
        f'<h1 style="color: green;">Здравствуйте, {user.username}, спасибо за регистрацию!</h1>'
        '<img src="https://images.unsplash.com/photo-1460467820054-c87ab43e9b59?ixlib=rb-4.0.3&ixid'
        '=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1067&q=80" width="600">'
        '</div>',
        subtype='html'
    )
    return e_msg


def send_welcome_email(user: UserRead):
    msg = get_welcome_email_template(user)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)

# celery = Celery('tasks', broker=f'amqp://{BROKER_HOSTNAME}:{BROKER_PORT}')


# Гайд по ручному запуску:
# Один сервис - один терминал
# Сначала перейти в src
# Запуск celery: celery -A tasks.tasks:celery worker --loglevel=INFO --pool=solo (--pool=solo писать только на windows)
# Запуск flower: celery -A tasks.tasks:celery flower

# def get_email_template_dashboard(username: str):
#     email = EmailMessage()
#     email['Subject'] = 'Натрейдил Отчет Дашборд'
#     email['From'] = SMTP_USER
#     email['To'] = SMTP_USER
#
#     email.set_content(
#         '<div>'
#         f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
#         '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
#         '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
#         '-mobile-free-vector.jpg" width="600">'
#         '</div>',
#         subtype='html'
#     )
#     return email
#
#
# # @celery.task
# def send_email_report_dashboard(username: str):
#     email = get_email_template_dashboard(username)
#     with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
#         server.login(SMTP_USER, SMTP_PASS)
#         server.send_message(email)
