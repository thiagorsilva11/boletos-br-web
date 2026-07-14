from app.models.socio import Socio
from app.repositories.base_repository import BaseRepository


class SocioRepository(BaseRepository):

    model = Socio

    @classmethod
    def listar(cls, busca=None):

        return super().listar(
            busca,
            Socio.nome
        )
        