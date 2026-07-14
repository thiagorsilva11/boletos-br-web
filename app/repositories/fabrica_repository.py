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