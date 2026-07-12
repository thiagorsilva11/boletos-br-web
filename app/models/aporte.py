from app import db
from app.models.base import BaseModel


class Aporte(BaseModel):

    __tablename__ = "aportes"

    socio_id = db.Column(
        db.Integer,
        db.ForeignKey("socios.id"),
        nullable=False
    )

    data = db.Column(
        db.Date,
        nullable=False
    )

    tipo = db.Column(
        db.String(20),
        nullable=False
    )

    valor = db.Column(
        db.Numeric(15,2),
        nullable=False
    )

    observacao = db.Column(
        db.Text
    )

    def __repr__(self):
        return f"<Aporte {self.id}>"