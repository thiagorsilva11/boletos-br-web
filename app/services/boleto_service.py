from decimal import Decimal


class BoletoService:

    @staticmethod
    def calcular(
        valor_compra,
        percentual_comissao,
        percentual_taxa,
        percentual_colaborador,
        juros=0
    ):
        """
        Calcula todos os valores financeiros do boleto.

        Não grava dados no banco.
        Apenas retorna os valores calculados.
        """

        valor_compra = Decimal(str(valor_compra))
        percentual_comissao = Decimal(str(percentual_comissao))
        percentual_taxa = Decimal(str(percentual_taxa))
        percentual_colaborador = Decimal(str(percentual_colaborador))
        juros = Decimal(str(juros))

        valor_comissao = (
            valor_compra * percentual_comissao
        ) / Decimal("100")

        taxa_empresa = (
            valor_comissao * percentual_taxa
        ) / Decimal("100")

        valor_colaborador = (
            taxa_empresa * percentual_colaborador
        ) / Decimal("100")

        valor_liquido = (
            valor_comissao
            - taxa_empresa
            - juros
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
        percentual_comissao
    ):
        """
        Retorna apenas o valor da comissão.
        """

        valor_compra = Decimal(str(valor_compra))
        percentual_comissao = Decimal(str(percentual_comissao))

        return (
            valor_compra * percentual_comissao
        ) / Decimal("100")