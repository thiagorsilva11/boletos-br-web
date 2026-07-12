from app import db
from app.models.base import BaseModel


class Socio(BaseModel):

    __tablename__ = "socios"

    nome = db.Column(db.String(150), nullable=False)

    cpf = db.Column(db.String(14))

    telefone = db.Column(db.String(20))

    def __repr__(self):
        return f"<Socio {self.nome}>"