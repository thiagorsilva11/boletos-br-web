from app import db
from app.models.base import BaseModel


class FluxoCaixa(BaseModel):
    __tablename__ = "fluxo_caixa"

    data_movimento = db.Column(
        db.Date,
        nullable=False,
        index=True
    )

    tipo = db.Column(
        db.String(20),
        nullable=False,
        index=True
    )

    origem = db.Column(
        db.String(30),
        nullable=False
    )

    documento = db.Column(
        db.String(50)
    )

    descricao = db.Column(
        db.String(255),
        nullable=False
    )

    valor = db.Column(
        db.Numeric(15, 2),
        nullable=False
    )

    saldo = db.Column(
        db.Numeric(15, 2),
        nullable=False,
        default=0
    )

    observacoes = db.Column(
        db.Text
    )

    def entrada(self):
        return self.tipo == "ENTRADA"

    def saida(self):
        return self.tipo == "SAIDA"

    def __repr__(self):
        return (
            f"<FluxoCaixa "
            f"{self.data_movimento} "
            f"{self.valor}>"
        )