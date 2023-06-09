from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")

APP_PORT = os.environ.get("APP_PORT")

SECRET_KEY_JWT = os.environ.get("SECRET_KEY_JWT")
SECRET_AUTH = os.environ.get("SECRET_AUTH")

BROKER_PORT = os.environ.get("BROKER_PORT")
BROKER_HOSTNAME = os.environ.get("BROKER_HOSTNAME")
BROKER_HOST_PORT = os.environ.get("BROKER_HOST_PORT")
BROKER_PASS = os.environ.get("BROKER_PASS")

SMTP_PASS = os.environ.get("SMTP_PASS")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")

BUCKET_NAME = os.environ.get("BUCKET_NAME")

ALLOWED_FILE_EXTENSIONS = ['.mp4', '.webm', '.ogg']
