from app.models.fabrica import Fabrica
from app.repositories.fabrica_repository import FabricaRepository


class FabricaService:

    @staticmethod
    def listar(busca=None):
        return FabricaRepository.listar(busca)

    @staticmethod
    def buscar(id):
        return FabricaRepository.buscar_por_id(id)

    @staticmethod
    def criar(form):

        fabrica = Fabrica(
            nome=form.nome.data,
            endereco=form.endereco.data,
            telefone=form.telefone.data,
            percentual_comissao=form.percentual_comissao.data,
            observacoes=form.observacoes.data
        )

        FabricaRepository.salvar(fabrica)

        return fabrica

    @staticmethod
    def atualizar(fabrica, form):

        fabrica.nome = form.nome.data
        fabrica.endereco = form.endereco.data
        fabrica.telefone = form.telefone.data
        fabrica.percentual_comissao = form.percentual_comissao.data
        fabrica.observacoes = form.observacoes.data

        FabricaRepository.atualizar()

    @staticmethod
    def excluir(fabrica):

        FabricaRepository.excluir(fabrica)