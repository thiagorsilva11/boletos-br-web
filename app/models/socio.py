from app import db
from app.models.base import BaseModel


class Socio(BaseModel):
    __tablename__ = "socios"

    nome = db.Column(
        db.String(150),
        nullable=False,
        index=True
    )

    cpf = db.Column(
        db.String(14),
        unique=True
    )

    telefone = db.Column(
        db.String(20)
    )

    email = db.Column(
        db.String(150)
    )

    percentual_participacao = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=0
    )

    saldo = db.Column(
        db.Numeric(15, 2),
        nullable=False,
        default=0
    )

    observacoes = db.Column(
        db.Text
    )

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
        index=True
    )

    def ativo_status(self):
        return self.ativo

    def inativo_status(self):
        return not self.ativo

    def __repr__(self):
        return f"<Socio {self.nome}>"