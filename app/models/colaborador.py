from app import db
from app.models.base import BaseModel


class Colaborador(BaseModel):
    __tablename__ = "colaboradores"

    nome = db.Column(
        db.String(150),
        nullable=False
    )

    cpf = db.Column(
        db.String(14),
        unique=True
    )

    telefone = db.Column(
        db.String(20)
    )

    def __repr__(self):
        return f"<Colaborador {self.nome}>"