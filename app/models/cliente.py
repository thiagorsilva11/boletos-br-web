from app import db
from app.models.base import BaseModel


class Cliente(BaseModel):

    __tablename__ = "clientes"

    nome = db.Column(db.String(150), nullable=False)

    nome_fantasia = db.Column(db.String(150))

    cpf = db.Column(db.String(14), nullable=False, unique=True)

    telefone = db.Column(db.String(20), nullable=False)

    endereco = db.Column(db.String(200))

    observacoes = db.Column(db.Text)

    def __repr__(self):
        return f"<Cliente {self.nome}>"