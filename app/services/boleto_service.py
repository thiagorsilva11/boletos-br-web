from app.models.boleto import Boleto
from app.models.conta_receber import ContaReceber

from app.repositories.boleto_repository import (
    BoletoRepository
)

from app.repositories.conta_receber_repository import (
    ContaReceberRepository
)

from app.services.motor_financeiro_service import (
    MotorFinanceiroService
)


class BoletoService:

    @staticmethod
    def criar(
        operacao,
        form
    ):

        dias = (
            form.data_prevista_recebimento.data
            - form.data_compra.data
        ).days

        financeiro = MotorFinanceiroService.calcular(
            valor_boleto=form.valor_compra.data,
            percentual_comissao=form.percentual_comissao.data,
            dias=dias
        )

        boleto = Boleto(

            operacao_id=operacao.id,

            numero_boleto=form.numero_boleto.data.strip(),

            data_compra=form.data_compra.data,

            valor_compra=financeiro["valor_boleto"],

            percentual_comissao=financeiro[
                "percentual_comissao"
            ],

            valor_comissao=financeiro[
                "valor_comissao"
            ],

            dias=financeiro["dias"],

            juros=financeiro["juros"],

            taxa_cobranca=financeiro[
                "taxa_empresa"
            ],

            valor_repasse=financeiro[
                "valor_representante"
            ],

            data_prevista_recebimento=form.data_prevista_recebimento.data,

            status=0,
        )

        BoletoRepository.adicionar(
            boleto
        )

        conta = ContaReceber(

            boleto=boleto,

            valor=financeiro[
                "valor_representante"
            ],

            data_prevista=form.data_prevista_recebimento.data,

            status=0,
        )

        ContaReceberRepository.adicionar(
            conta
        )

        BoletoRepository.commit()

        return boleto