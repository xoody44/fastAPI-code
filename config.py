from os import getenv

from dotenv import load_dotenv

load_dotenv()

SMTP_USER = getenv("SMTP_USER")
SMTP_PASSWORD = getenv("SMTP_PASSWORD")

REDIS_HOST = getenv("REDIS_HOST")

APP_PORT = getenv("APP_PORT")
APP_HOST = getenv("APP_HOST")

DB_PATH = getenv("DB_PATH")

SECRET_TOKEN = getenv("SECRET_TOKEN")
