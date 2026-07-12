from app import db
from app.models.base import BaseModel


class Usuario(BaseModel):

    __tablename__ = "usuarios"

    nome = db.Column(
        db.String(150),
        nullable=False
    )

    login = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    senha = db.Column(
        db.String(255),
        nullable=False
    )

    perfil = db.Column(
        db.String(30),
        nullable=False,
        default="Administrador"
    )

    def __repr__(self):
        return f"<Usuario {self.login}>"