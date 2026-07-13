from app import db
from app.models.base import BaseModel


class Socio(BaseModel):
    __tablename__ = "socios"

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

    saldo = db.Column(
        db.Numeric(15,2),
        nullable=False,
        default=0
    )

    def __repr__(self):
        return f"<Socio {self.nome}>"