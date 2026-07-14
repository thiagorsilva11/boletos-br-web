from app.models.colaborador import Colaborador
from app.repositories.base_repository import BaseRepository


class ColaboradorRepository(BaseRepository):

    model = Colaborador

    @classmethod
    def listar(cls, busca=None):

        return super().listar(
            busca,
            Colaborador.nome
        )