from app import db
from app.models.base import BaseModel


class Fabrica(BaseModel):
    __tablename__ = "fabricas"

    nome = db.Column(
        db.String(150),
        nullable=False
    )

    endereco = db.Column(
        db.String(250)
    )

    telefone = db.Column(
        db.String(20)
    )

    percentual_comissao = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=0
    )

    observacoes = db.Column(
        db.Text
    )

    def __repr__(self):
        return f"<Fabrica {self.nome}>"