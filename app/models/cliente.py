from app import db
from app.models.base import BaseModel


class Cliente(BaseModel):
    __tablename__ = "clientes"

    representante = db.Column(
        db.String(150),
        nullable=False,
        index=True
    )

    responsavel = db.Column(
        db.String(150),
        nullable=False
    )

    cpf = db.Column(
        db.String(14),
        nullable=False,
        unique=True
    )

    telefone = db.Column(
        db.String(20),
        nullable=False
    )

    endereco = db.Column(
        db.String(250)
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

    operacoes = db.relationship(
        "Operacao",
        backref="cliente",
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
            f"<Cliente "
            f"{self.representante}>"
        )