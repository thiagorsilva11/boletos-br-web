from app.models.socio import Socio
from app.repositories.socio_repository import SocioRepository


class SocioService:

    @staticmethod
    def listar(busca=None):
        return SocioRepository.listar(busca)

    @staticmethod
    def buscar(id):
        return SocioRepository.buscar_por_id(id)

    @staticmethod
    def criar(form):

        socio = Socio(
            nome=form.nome.data,
            cpf=form.cpf.data,
            telefone=form.telefone.data,
            email=form.email.data,
            percentual_participacao=form.percentual_participacao.data,
            saldo=form.saldo.data,
            observacoes=form.observacoes.data
        )

        SocioRepository.salvar(socio)

        return socio

    @staticmethod
    def atualizar(socio, form):

        socio.nome = form.nome.data
        socio.cpf = form.cpf.data
        socio.telefone = form.telefone.data
        socio.email = form.email.data
        socio.percentual_participacao = form.percentual_participacao.data
        socio.saldo = form.saldo.data
        socio.observacoes = form.observacoes.data

        SocioRepository.atualizar()

    @staticmethod
    def excluir(socio):

        SocioRepository.excluir(socio)