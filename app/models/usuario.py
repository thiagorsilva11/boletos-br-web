from app import db
from app.models.base import BaseModel


class Usuario(BaseModel):
    __tablename__ = "usuarios"

    nome = db.Column(
        db.String(150),
        nullable=False,
        index=True
    )

    login = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
        index=True
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

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
        index=True
    )

    def administrador(self):
        return self.perfil == "Administrador"

    def ativo_status(self):
        return self.ativo

    def inativo_status(self):
        return not self.ativo

    def __repr__(self):
        return (
            f"<Usuario "
            f"{self.login}>"
        )