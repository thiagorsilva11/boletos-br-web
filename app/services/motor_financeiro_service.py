from decimal import Decimal, ROUND_HALF_UP


class MotorFinanceiroService:

    TAXA_EMPRESA = Decimal("0.07")

    @staticmethod
    def calcular(
        valor_boleto,
        percentual_comissao,
        dias
    ):

        valor_boleto = Decimal(str(valor_boleto))
        percentual_comissao = Decimal(str(percentual_comissao))

        # Comissão

        valor_comissao = (
            valor_boleto
            * percentual_comissao
            / Decimal("100")
        ).quantize(
            Decimal("0.01"),
            ROUND_HALF_UP
        )

        # Taxa Empresa (7%)

        taxa_empresa = (
            valor_comissao
            * MotorFinanceiroService.TAXA_EMPRESA
        ).quantize(
            Decimal("0.01"),
            ROUND_HALF_UP
        )

        # Juros

        fator = Decimal("1.00")

        if dias <= 30:
            fator = Decimal("1.10")

        elif dias <= 60:
            fator = Decimal("1.21")

        elif dias <= 90:
            fator = Decimal("1.331")

        elif dias <= 120:
            fator = Decimal("1.4641")

        juros = (
            valor_comissao
            * (fator - Decimal("1"))
        ).quantize(
            Decimal("0.01"),
            ROUND_HALF_UP
        )

        # Representante

        valor_representante = (
            valor_comissao
            - taxa_empresa
            - juros
        ).quantize(
            Decimal("0.01"),
            ROUND_HALF_UP
        )

        # Receita Empresa

        lucro_empresa = (
            taxa_empresa
            + juros
        ).quantize(
            Decimal("0.01"),
            ROUND_HALF_UP
        )

        return {

            "dias": dias,

            "valor_boleto": valor_boleto,

            "percentual_comissao": percentual_comissao,

            "valor_comissao": valor_comissao,

            "taxa_empresa": taxa_empresa,

            "juros": juros,

            "valor_representante": valor_representante,

            "lucro_empresa": lucro_empresa,

            "fator_juros": fator,

        }