from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")

SECRET_KEY_JWT = os.environ.get("SECRET_KEY_JWT")
SECRET_AUTH = os.environ.get("SECRET_AUTH")

BROKER_PORT = os.environ.get("BROKER_PORT")
BROKER_HOST = os.environ.get("BROKER_HOST")

SMTP_PASS = os.environ.get("SMTP_PASS")
SMTP_USER = os.environ.get("SMTP_USER")
