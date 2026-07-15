from app import db
from app.models.base import BaseModel


class Colaborador(BaseModel):
    __tablename__ = "colaboradores"

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

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
        index=True
    )

    operacoes = db.relationship(
        "Operacao",
        backref="colaborador",
        lazy=True
    )

    @property
    def quantidade_operacoes(self):
        return len(self.operacoes)

    def ativo_status(self):
        return self.ativo

    def inativo_status(self):
        return not self.ativo

    def __repr__(self):
        return (
            f"<Colaborador "
            f"{self.nome}>"
        )