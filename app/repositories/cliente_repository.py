from app.models.cliente import Cliente
from app.repositories.base_repository import BaseRepository


class ClienteRepository(BaseRepository):

    model = Cliente

    @classmethod
    def listar(cls, busca=None):

        return super().listar(
            busca,
            Cliente.representante
        )