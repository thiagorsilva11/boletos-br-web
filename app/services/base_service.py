class BaseService:

    repository = None

    @classmethod
    def listar(cls, busca=None):

        return cls.repository.listar(busca)

    @classmethod
    def buscar(cls, id):

        return cls.repository.buscar_por_id(id)

    @classmethod
    def excluir(cls, objeto):

        cls.repository.excluir(objeto)