from decimal import Decimal, ROUND_HALF_UP

from app.models.parametro import Parametro


class BoletoService:

    @staticmethod
    def calcular(
        valor_compra,
        percentual_comissao,
        percentual_taxa=None,
        percentual_colaborador=None,
        juros=0,
    ):
        """
        Calcula todos os valores financeiros do boleto.

        Caso os percentuais não sejam informados,
        utiliza os parâmetros do sistema.
        """

        parametro = Parametro.obter()

        if percentual_taxa is None:
            percentual_taxa = parametro.taxa_empresa

        if percentual_colaborador is None:
            percentual_colaborador = parametro.percentual_colaborador

        valor_compra = Decimal(str(valor_compra))
        percentual_comissao = Decimal(str(percentual_comissao))
        percentual_taxa = Decimal(str(percentual_taxa))
        percentual_colaborador = Decimal(str(percentual_colaborador))
        juros = Decimal(str(juros))

        valor_comissao = (
            valor_compra * percentual_comissao / Decimal("100")
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

        taxa_empresa = (
            valor_comissao * percentual_taxa / Decimal("100")
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

        valor_colaborador = (
            taxa_empresa * percentual_colaborador / Decimal("100")
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

        valor_liquido = (
            valor_comissao
            - taxa_empresa
            - juros
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

        return {
            "valor_compra": valor_compra,
            "percentual_comissao": percentual_comissao,
            "valor_comissao": valor_comissao,
            "percentual_taxa": percentual_taxa,
            "taxa_empresa": taxa_empresa,
            "percentual_colaborador": percentual_colaborador,
            "valor_colaborador": valor_colaborador,
            "juros": juros,
            "valor_liquido": valor_liquido,
        }

    @staticmethod
    def calcular_comissao(
        valor_compra,
        percentual_comissao,
    ):
        valor_compra = Decimal(str(valor_compra))
        percentual_comissao = Decimal(str(percentual_comissao))

        return (
            valor_compra
            * percentual_comissao
            / Decimal("100")
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

    @staticmethod
    def calcular_dias(
        data_operacao,
        data_recebimento_prevista,
    ):
        """
        Retorna a quantidade de dias entre
        a operação e o recebimento previsto.
        """

        return (
            data_recebimento_prevista
            - data_operacao
        ).days