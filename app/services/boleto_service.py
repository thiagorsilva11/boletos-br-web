from decimal import Decimal, ROUND_HALF_UP

from app.repositories.boleto_repository import BoletoRepository
from app.repositories.conta_receber_repository import ContaReceberRepository
from app.models.boleto import Boleto
from app.models.conta_receber import ContaReceber


class BoletoService:

    @staticmethod
    def criar(
        operacao,
        form,
    ):

        dias = (
            form.data_prevista_recebimento.data
            - form.data_compra.data
        ).days

        valor_compra = Decimal(
            str(form.valor_compra.data)
        )

        percentual = Decimal(
            str(form.percentual_comissao.data)
        )

        valor_comissao = (
            valor_compra
            * percentual
            / Decimal("100")
        ).quantize(
            Decimal("0.01"),
            ROUND_HALF_UP,
        )

        juros = Decimal("0")

        taxa = Decimal("0")

        valor_repasse = valor_comissao

        boleto = Boleto(

            operacao_id=operacao.id,

            numero_boleto=form.numero_boleto.data,

            data_compra=form.data_compra.data,

            valor_compra=valor_compra,

            percentual_comissao=percentual,

            valor_comissao=valor_comissao,

            dias=dias,

            juros=juros,

            taxa_cobranca=taxa,

            valor_repasse=valor_repasse,

            data_prevista_recebimento=form.data_prevista_recebimento.data,

            status=0,

        )

        BoletoRepository.adicionar(
            boleto
        )

        conta = ContaReceber(

            boleto=boleto,

            data_prevista=form.data_prevista_recebimento.data,

            valor=valor_comissao,

            status=0,

        )

        ContaReceberRepository.adicionar(
            conta
        )

        BoletoRepository.commit()

        return boleto
        