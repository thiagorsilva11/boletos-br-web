from app.models.socio import Socio
from app.repositories.base_repository import BaseRepository


class SocioRepository(BaseRepository):

    model = Socio

    @classmethod
    def listar(cls, busca=None):
        return super().listar(
            busca,
            Socio.nome,
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
    def listar_ativos(cls):
        return (
            cls.model.query
            .filter_by(ativo=True)
            .order_by(cls.model.nome.asc())
            .all()
        )

    @classmethod
    def listar_inativos(cls):
        return (
            cls.model.query
            .filter_by(ativo=False)
            .order_by(cls.model.nome.asc())
            .all()
        )

    @classmethod
    def listar_por_saldo(cls):
        return (
            cls.model.query
            .order_by(cls.model.saldo.desc())
            .all()
        )