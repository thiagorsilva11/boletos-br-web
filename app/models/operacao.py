from app import db
from app.models.base import BaseModel


class Operacao(BaseModel):
    __tablename__ = "operacoes"

    numero_operacao = db.Column(
        db.String(20),
        nullable=False,
        unique=True,
        index=True
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
        nullable=False,
        index=True
    )

    observacao = db.Column(
        db.Text
    )

    status = db.Column(
        db.Integer,
        nullable=False,
        default=0,
        index=True
    )

    boletos = db.relationship(
        "Boleto",
        backref="operacao",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def aberta(self):
        return self.status == 0

    def encerrada(self):
        return self.status == 1

    @property
    def quantidade_boletos(self):
        return len(self.boletos)

    @property
    def valor_total_compra(self):
        return sum(
            boleto.valor_compra
            for boleto in self.boletos
        )

    @property
    def valor_total_comissao(self):
        return sum(
            boleto.valor_comissao
            for boleto in self.boletos
        )

    def __repr__(self):
        return (
            f"<Operacao "
            f"{self.numero_operacao}>"
        )