from app import db
from app.models.operacao import Operacao
from app.repositories.base_repository import BaseRepository


class OperacaoRepository(BaseRepository):

    model = Operacao

    @classmethod
    def buscar_por_numero(cls, numero_operacao):
        return cls.model.query.filter_by(
            numero_operacao=numero_operacao
        ).first()

    @classmethod
    def listar_por_cliente(cls, cliente_id):
        return (
            cls.model.query
            .filter_by(cliente_id=cliente_id)
            .order_by(cls.model.data_operacao.desc())
            .all()
        )

    @classmethod
    def listar_abertas(cls):
        return (
            cls.model.query
            .filter_by(status=0)
            .order_by(cls.model.data_operacao.desc())
            .all()
        )

    @staticmethod
    def adicionar(operacao):
        """
        Adiciona a operação na sessão.
        Não executa commit.
        """
        db.session.add(operacao)

    @staticmethod
    def commit():
        """
        Confirma toda a transação.
        """
        db.session.commit()

    @staticmethod
    def rollback():
        """
        Cancela toda a transação.
        """
        db.session.rollback()