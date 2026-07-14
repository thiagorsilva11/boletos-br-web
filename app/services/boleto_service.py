from decimal import Decimal


class BoletoService:

    @staticmethod
    def calcular(
        valor_compra,
        percentual_comissao,
        percentual_taxa,
        percentual_colaborador,
        juros
    ):

        valor_compra = Decimal(valor_compra)

        percentual_comissao = Decimal(percentual_comissao)

        percentual_taxa = Decimal(percentual_taxa)

        percentual_colaborador = Decimal(percentual_colaborador)

        juros = Decimal(juros)

        valor_comissao = (
            valor_compra * percentual_comissao
        ) / Decimal("100")

        taxa_empresa = (
            valor_comissao * percentual_taxa
        ) / Decimal("100")

        valor_repasse = (
            taxa_empresa * percentual_colaborador
        ) / Decimal("100")

        valor_liquido = (
            valor_comissao
            - taxa_empresa
            - juros
        )

        return {
            "valor_comissao": valor_comissao,
            "taxa_empresa": taxa_empresa,
            "valor_repasse": valor_repasse,
            "valor_liquido": valor_liquido,
        }