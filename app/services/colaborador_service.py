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
            nome=form.nome.data,
            cpf=form.cpf.data,
            telefone=form.telefone.data
        )

        ColaboradorRepository.salvar(colaborador)

        return colaborador

    @staticmethod
    def atualizar(colaborador, form):

        colaborador.nome = form.nome.data
        colaborador.cpf = form.cpf.data
        colaborador.telefone = form.telefone.data

        ColaboradorRepository.atualizar()

    @staticmethod
    def excluir(colaborador):

        ColaboradorRepository.excluir(colaborador)