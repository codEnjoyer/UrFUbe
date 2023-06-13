from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

FRONT_APP_PORT = os.environ.get("FRONT_APP_PORT")
BACKEND_APP_PORT = os.environ.get("BACKEND_APP_PORT")

SECRET_KEY_JWT = os.environ.get("SECRET_KEY_JWT")
RESET_PASSWORD_TOKEN = os.environ.get("RESET_PASSWORD_TOKEN")
VERIFICATION_TOKEN = os.environ.get("VERIFICATION_TOKEN")

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

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
