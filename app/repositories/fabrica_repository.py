from app.models.fabrica import Fabrica
from app.repositories.base_repository import BaseRepository


class FabricaRepository(BaseRepository):

    model = Fabrica

    @classmethod
    def listar(cls, busca=None):
        return super().listar(
            busca,
            Fabrica.nome
        )

    @classmethod
    def buscar_por_nome(cls, nome):
        return (
            cls.model.query
            .filter(
                cls.model.nome.ilike(nome)
            )
            .first()
        )

    @classmethod
    def listar_ativas(cls):
        return (
            cls.model.query
            .filter_by(ativa=True)
            .order_by(cls.model.nome.asc())
            .all()
        )

    @classmethod
    def listar_inativas(cls):
        return (
            cls.model.query
            .filter_by(ativa=False)
            .order_by(cls.model.nome.asc())
            .all()
        )

    @classmethod
    def obter_percentual_comissao(cls, fabrica_id):
        fabrica = cls.buscar_por_id(fabrica_id)

        if fabrica is None:
            return 0

        return fabrica.percentual_comissao