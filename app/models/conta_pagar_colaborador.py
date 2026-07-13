from app import db
from app.models.base import BaseModel


class ContaPagarColaborador(BaseModel):
    __tablename__ = "contas_pagar_colaborador"

    operacao_id = db.Column(
        db.Integer,
        db.ForeignKey("operacoes.id"),
        nullable=False
    )

    colaborador_id = db.Column(
        db.Integer,
        db.ForeignKey("colaboradores.id"),
        nullable=False
    )

    data_pagamento = db.Column(
        db.Date
    )

    valor = db.Column(
        db.Numeric(15, 2),
        nullable=False
    )

    status = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    observacao = db.Column(
        db.Text
    )

    def __repr__(self):
        return f"<ContaPagarColaborador {self.id}>"