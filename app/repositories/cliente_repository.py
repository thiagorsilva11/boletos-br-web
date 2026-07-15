from app.models.cliente import Cliente
from app.repositories.base_repository import BaseRepository


class ClienteRepository(BaseRepository):

    model = Cliente

    @classmethod
    def listar(cls, busca=None):
        return super().listar(
            busca,
            Cliente.representante,
        )

    @classmethod
    def buscar_por_representante(cls, representante):
        return (
            cls.model.query
            .filter(
                cls.model.representante.ilike(representante)
            )
            .first()
        )

    @classmethod
    def listar_ativos(cls):
        return (
            cls.model.query
            .filter_by(ativo=True)
            .order_by(cls.model.representante.asc())
            .all()
        )

    @classmethod
    def listar_inativos(cls):
        return (
            cls.model.query
            .filter_by(ativo=False)
            .order_by(cls.model.representante.asc())
            .all()
        )