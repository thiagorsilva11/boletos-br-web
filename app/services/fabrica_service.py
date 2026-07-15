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
            nome=form.nome.data.strip(),
            endereco=form.endereco.data.strip() if form.endereco.data else None,
            telefone=form.telefone.data.strip() if form.telefone.data else None,
            percentual_comissao=form.percentual_comissao.data,
            observacoes=form.observacoes.data.strip() if form.observacoes.data else None,
        )

        FabricaRepository.salvar(fabrica)

        return fabrica

    @staticmethod
    def atualizar(fabrica, form):

        fabrica.nome = form.nome.data.strip()
        fabrica.endereco = (
            form.endereco.data.strip()
            if form.endereco.data
            else None
        )

        fabrica.telefone = (
            form.telefone.data.strip()
            if form.telefone.data
            else None
        )

        fabrica.percentual_comissao = form.percentual_comissao.data

        fabrica.observacoes = (
            form.observacoes.data.strip()
            if form.observacoes.data
            else None
        )

        FabricaRepository.atualizar()

        return fabrica

    @staticmethod
    def excluir(fabrica):

        FabricaRepository.excluir(fabrica)

    @staticmethod
    def percentual_padrao(fabrica_id):
        """
        Retorna o percentual de comissão padrão da fábrica.
        Será utilizado automaticamente no cadastro dos boletos.
        """

        fabrica = FabricaRepository.buscar_por_id(fabrica_id)

        if fabrica is None:
            return 0

        return fabrica.percentual_comissao