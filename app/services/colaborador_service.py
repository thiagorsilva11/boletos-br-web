from app.models.colaborador import Colaborador
from app.repositories.colaborador_repository import ColaboradorRepository


class ColaboradorService:

    @staticmethod
    def listar(busca=None):
        return ColaboradorRepository.listar(busca)

    @staticmethod
    def buscar(id):
        return ColaboradorRepository.buscar_por_id(id)

    @staticmethod
    def criar(form):

        colaborador = Colaborador(
            nome=form.nome.data.strip(),
            cpf=form.cpf.data.strip() if form.cpf.data else None,
            telefone=form.telefone.data.strip() if form.telefone.data else None,
        )

        ColaboradorRepository.salvar(colaborador)

        return colaborador

    @staticmethod
    def atualizar(colaborador, form):

        colaborador.nome = form.nome.data.strip()

        colaborador.cpf = (
            form.cpf.data.strip()
            if form.cpf.data
            else None
        )

        colaborador.telefone = (
            form.telefone.data.strip()
            if form.telefone.data
            else None
        )

        ColaboradorRepository.atualizar()

        return colaborador

    @staticmethod
    def excluir(colaborador):

        ColaboradorRepository.excluir(colaborador)

    @staticmethod
    def buscar_por_nome(nome):
        return ColaboradorRepository.buscar_por_nome(
            nome
        )