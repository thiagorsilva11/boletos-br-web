from app import db
from app.models.base import BaseModel


class Boleto(BaseModel):
    __tablename__ = "boletos"

    operacao_id = db.Column(
        db.Integer,
        db.ForeignKey("operacoes.id"),
        nullable=False
    )

    numero_boleto = db.Column(
        db.String(50),
        nullable=False
    )

    data_compra = db.Column(
        db.Date,
        nullable=False
    )

    valor_compra = db.Column(
        db.Numeric(15, 2),
        nullable=False
    )

    percentual_comissao = db.Column(
        db.Numeric(5, 2),
        nullable=False
    )

    valor_comissao = db.Column(
        db.Numeric(15, 2),
        nullable=False
    )

    dias = db.Column(
        db.Integer,
        nullable=False
    )

    juros = db.Column(
        db.Numeric(15, 2),
        nullable=False,
        default=0
    )

    taxa_cobranca = db.Column(
        db.Numeric(15, 2),
        nullable=False
    )

    valor_repasse = db.Column(
        db.Numeric(15, 2),
        nullable=False
    )

    data_prevista_recebimento = db.Column(
        db.Date,
        nullable=False
    )

    data_recebimento = db.Column(
        db.Date
    )

    status = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    def __repr__(self):
        return f"<Boleto {self.numero_boleto}>"