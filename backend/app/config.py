import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class ApplicationConfiguration:
    SECRET_KEY = os.getenv("APP_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///commerce.sqlite3"
    JWT_SECRET_KEY = os.getenv('APP_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = 900 #15 minutes
    JWT_REFRESH_TOKEN_EXPIRES = 86400 #1 day
    PAYSTACK_SECRET_KEY = os.environ.get('PAYSTACK_SECRET_KEY')