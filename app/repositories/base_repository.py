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

        return query.order_by(
            cls.model.id.desc()
        ).all()

    @classmethod
    def buscar_por_id(cls, id):

        return cls.model.query.get(id)

    @classmethod
    def existe(cls, id):

        return cls.model.query.get(id) is not None

    @staticmethod
    def salvar(objeto):

        db.session.add(objeto)
        db.session.commit()

        return objeto

    @staticmethod
    def adicionar(objeto):
        """
        Adiciona o objeto à sessão sem executar commit.
        Utilizado em operações com múltiplos registros.
        """

        db.session.add(objeto)

        return objeto

    @staticmethod
    def atualizar():

        db.session.commit()

    @staticmethod
    def commit():

        db.session.commit()

    @staticmethod
    def rollback():

        db.session.rollback()

    @staticmethod
    def excluir(objeto):

        db.session.delete(objeto)
        db.session.commit()