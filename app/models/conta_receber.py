from app import db
from app.models.base import BaseModel


class ContaReceber(BaseModel):
    __tablename__ = "contas_receber"

    boleto_id = db.Column(
        db.Integer,
        db.ForeignKey("boletos.id"),
        nullable=False
    )

    data_prevista = db.Column(
        db.Date,
        nullable=False
    )

    data_recebimento = db.Column(
        db.Date
    )

    valor_comissao = db.Column(
        db.Numeric(15, 2),
        nullable=False
    )

    status = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    def __repr__(self):
        return f"<ContaReceber {self.id}>"