from app.models.colaborador import Colaborador
from app.repositories.base_repository import BaseRepository


class ColaboradorRepository(BaseRepository):

    model = Colaborador

    @classmethod
    def listar(cls, busca=None):
        return super().listar(
            busca,
            Colaborador.nome,
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