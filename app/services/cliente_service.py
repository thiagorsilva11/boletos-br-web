from app.models.cliente import Cliente
from app.repositories.cliente_repository import ClienteRepository


class ClienteService:

    @staticmethod
    def listar(busca=None):
        return ClienteRepository.listar(busca)

    @staticmethod
    def buscar(id):
        return ClienteRepository.buscar_por_id(id)

    @staticmethod
    def criar(form):

        cliente = Cliente(
            representante=form.representante.data,
            responsavel=form.responsavel.data,
            cpf=form.cpf.data,
            telefone=form.telefone.data,
            endereco=form.endereco.data,
            observacoes=form.observacoes.data
        )

        ClienteRepository.salvar(cliente)

        return cliente

    @staticmethod
    def atualizar(cliente, form):

        cliente.representante = form.representante.data
        cliente.responsavel = form.responsavel.data
        cliente.cpf = form.cpf.data
        cliente.telefone = form.telefone.data
        cliente.endereco = form.endereco.data
        cliente.observacoes = form.observacoes.data

        ClienteRepository.atualizar()

    @staticmethod
    def excluir(cliente):

        ClienteRepository.excluir(cliente)