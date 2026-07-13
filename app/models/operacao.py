from app import db
from app.models.base import BaseModel


class Operacao(BaseModel):
    __tablename__ = "operacoes"

    numero_operacao = db.Column(
        db.String(20),
        nullable=False,
        unique=True
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("clientes.id"),
        nullable=False
    )

    fabrica_id = db.Column(
        db.Integer,
        db.ForeignKey("fabricas.id"),
        nullable=False
    )

    colaborador_id = db.Column(
        db.Integer,
        db.ForeignKey("colaboradores.id"),
        nullable=False
    )

    data_operacao = db.Column(
        db.Date,
        nullable=False
    )

    observacao = db.Column(
        db.Text
    )

    status = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    def __repr__(self):
        return f"<Operacao {self.numero_operacao}>" 