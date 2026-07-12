import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = "boletosbr2026"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "boletos_br.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False