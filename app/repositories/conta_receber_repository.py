from app.models.conta_receber import ContaReceber
from app.repositories.base_repository import BaseRepository


class ContaReceberRepository(BaseRepository):

    model = ContaReceber

    @classmethod
    def listar_em_aberto(cls):
        return (
            cls.model.query
            .filter_by(status=0)
            .order_by(cls.model.data_prevista)
            .all()
        )

    @classmethod
    def listar_recebidas(cls):
        return (
            cls.model.query
            .filter_by(status=1)
            .order_by(cls.model.data_recebimento.desc())
            .all()
        )

    @classmethod
    def listar_vencidas(cls):
        from datetime import date

        return (
            cls.model.query
            .filter(
                cls.model.status == 0,
                cls.model.data_prevista < date.today()
            )
            .order_by(cls.model.data_prevista)
            .all()
        )

    @classmethod
    def listar_por_boleto(cls, boleto_id):
        return cls.model.query.filter_by(
            boleto_id=boleto_id
        ).first()