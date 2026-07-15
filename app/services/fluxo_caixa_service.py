from datetime import date

from app.models.fluxo_caixa import FluxoCaixa
from app.repositories.fluxo_caixa_repository import (
    FluxoCaixaRepository,
)


class FluxoCaixaService:

    @staticmethod
    def registrar_entrada(
        valor,
        descricao,
        origem,
        documento=None,
        observacoes=None,
    ):

        saldo = (
            FluxoCaixaRepository.saldo_atual()
            + valor
        )

        movimento = FluxoCaixa(
            data_movimento=date.today(),
            tipo="ENTRADA",
            origem=origem,
            documento=documento,
            descricao=descricao,
            valor=valor,
            saldo=saldo,
            observacoes=observacoes,
        )

        FluxoCaixaRepository.salvar(
            movimento
        )

        return movimento

    @staticmethod
    def registrar_saida(
        valor,
        descricao,
        origem,
        documento=None,
        observacoes=None,
    ):

        saldo = (
            FluxoCaixaRepository.saldo_atual()
            - valor
        )

        movimento = FluxoCaixa(
            data_movimento=date.today(),
            tipo="SAIDA",
            origem=origem,
            documento=documento,
            descricao=descricao,
            valor=valor,
            saldo=saldo,
            observacoes=observacoes,
        )

        FluxoCaixaRepository.salvar(
            movimento
        )

        return movimento