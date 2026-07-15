from app.models.boleto import Boleto
from app.repositories.base_repository import BaseRepository


class BoletoRepository(BaseRepository):

    model = Boleto

    @classmethod
    def buscar_por_numero(cls, numero_boleto):
        return cls.model.query.filter_by(
            numero_boleto=numero_boleto
        ).first()

    @classmethod
    def listar_por_operacao(cls, operacao_id):
        return (
            cls.model.query
            .filter_by(operacao_id=operacao_id)
            .order_by(cls.model.id)
            .all()
        )

    @classmethod
    def listar_pendentes(cls):
        return (
            cls.model.query
            .filter_by(status=0)
            .order_by(cls.model.data_prevista_recebimento)
            .all()
        )

    @classmethod
    def listar_recebidos(cls):
        return (
            cls.model.query
            .filter_by(status=1)
            .order_by(cls.model.data_recebimento.desc())
            .all()
        )