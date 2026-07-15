from app import db
from app.models.base import BaseModel


class Parametro(BaseModel):
    __tablename__ = "parametros"

    taxa_empresa = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=7
    )

    percentual_colaborador = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=50
    )

    juros_30 = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=10
    )

    juros_60 = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=20
    )

    juros_90 = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=30
    )

    juros_120 = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=40
    )

    dias_amarelo = db.Column(
        db.Integer,
        nullable=False,
        default=15
    )

    dias_vermelho = db.Column(
        db.Integer,
        nullable=False,
        default=15
    )

    numero_operacao = db.Column(
        db.Integer,
        nullable=False,
        default=1
    )

    @classmethod
    def obter(cls):
        parametro = cls.query.first()

        if not parametro:
            parametro = cls()
            db.session.add(parametro)
            db.session.commit()

        return parametro

    def __repr__(self):
        return (
            f"<Parametro "
            f"{self.id}>"
        )