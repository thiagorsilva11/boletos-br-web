from app.models.fluxo_caixa import FluxoCaixa
from app.repositories.base_repository import BaseRepository


class FluxoCaixaRepository(BaseRepository):

    model = FluxoCaixa

    @classmethod
    def listar_por_periodo(
        cls,
        data_inicial,
        data_final,
    ):
        return (
            cls.model.query
            .filter(
                cls.model.data_movimento >= data_inicial,
                cls.model.data_movimento <= data_final,
            )
            .order_by(
                cls.model.data_movimento.desc()
            )
            .all()
        )

    @classmethod
    def saldo_atual(cls):

        ultimo = (
            cls.model.query
            .order_by(cls.model.id.desc())
            .first()
        )

        if ultimo is None:
            return 0

        return ultimo.saldo