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
            representante=form.representante.data.strip(),
            responsavel=form.responsavel.data.strip(),
            cpf=form.cpf.data.strip() if form.cpf.data else None,
            telefone=form.telefone.data.strip() if form.telefone.data else None,
            endereco=form.endereco.data.strip() if form.endereco.data else None,
            observacoes=form.observacoes.data.strip() if form.observacoes.data else None,
        )

        ClienteRepository.salvar(cliente)

        return cliente

    @staticmethod
    def atualizar(cliente, form):

        cliente.representante = form.representante.data.strip()

        cliente.responsavel = form.responsavel.data.strip()

        cliente.cpf = (
            form.cpf.data.strip()
            if form.cpf.data
            else None
        )

        cliente.telefone = (
            form.telefone.data.strip()
            if form.telefone.data
            else None
        )

        cliente.endereco = (
            form.endereco.data.strip()
            if form.endereco.data
            else None
        )

        cliente.observacoes = (
            form.observacoes.data.strip()
            if form.observacoes.data
            else None
        )

        ClienteRepository.atualizar()

        return cliente

    @staticmethod
    def excluir(cliente):

        ClienteRepository.excluir(cliente)

    @staticmethod
    def buscar_por_representante(representante):
        return ClienteRepository.buscar_por_representante(
            representante
        )