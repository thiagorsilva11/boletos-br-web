from app import db


class BaseRepository:

    model = None

    @classmethod
    def listar(cls, busca=None, campo=None):

        query = cls.model.query

        if busca and campo is not None:
            query = query.filter(
                campo.ilike(f"%{busca}%")
            )

        return query.all()

    @classmethod
    def buscar_por_id(cls, id):

        return cls.model.query.get_or_404(id)

    @staticmethod
    def salvar(objeto):

        db.session.add(objeto)
        db.session.commit()

    @staticmethod
    def atualizar():

        db.session.commit()

    @staticmethod
    def excluir(objeto):

        db.session.delete(objeto)
        db.session.commit()