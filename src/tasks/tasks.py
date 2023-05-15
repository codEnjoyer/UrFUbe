import smtplib
from email.message import EmailMessage

from celery import Celery

from config import SMTP_PASS, SMTP_USER, SMTP_PORT, SMTP_HOST, \
    BROKER_HOSTNAME, BROKER_PORT

celery = Celery('tasks', broker=f'amqp://{BROKER_HOSTNAME}:{BROKER_PORT}')


# Один сервис - один терминал
# Сначала перейти в src
# Запуск celery: celery -A tasks.tasks:celery worker --loglevel=INFO --pool=solo (--pool=solo писать только на windows)
# Запуск flower: celery -A tasks.tasks:celery flower

def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Натрейдил Отчет Дашборд'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
        '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
        '-mobile-free-vector.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email)
