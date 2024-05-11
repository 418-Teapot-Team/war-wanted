import os
from os.path import join, dirname
from dotenv import load_dotenv


# find .env file
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    class db:
        user = os.getenv("DB_USER")
        pswd = os.getenv("DB_PSWD")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        name = os.getenv("DB_NAME")
        uri = f"postgresql://{user}:{pswd}@{host}:{port}/{name}"
