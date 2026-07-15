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
            nome=form.nome.data.strip(),
            cpf=form.cpf.data.strip() if form.cpf.data else None,
            telefone=form.telefone.data.strip() if form.telefone.data else None,
            email=form.email.data.strip() if form.email.data else None,
            percentual_participacao=form.percentual_participacao.data,
            saldo=form.saldo.data,
            observacoes=form.observacoes.data.strip() if form.observacoes.data else None,
        )

        SocioRepository.salvar(socio)

        return socio

    @staticmethod
    def atualizar(socio, form):

        socio.nome = form.nome.data.strip()

        socio.cpf = (
            form.cpf.data.strip()
            if form.cpf.data
            else None
        )

        socio.telefone = (
            form.telefone.data.strip()
            if form.telefone.data
            else None
        )

        socio.email = (
            form.email.data.strip()
            if form.email.data
            else None
        )

        socio.percentual_participacao = (
            form.percentual_participacao.data
        )

        socio.saldo = form.saldo.data

        socio.observacoes = (
            form.observacoes.data.strip()
            if form.observacoes.data
            else None
        )

        SocioRepository.atualizar()

        return socio

    @staticmethod
    def excluir(socio):

        SocioRepository.excluir(socio)

    @staticmethod
    def buscar_por_nome(nome):
        return SocioRepository.buscar_por_nome(nome)