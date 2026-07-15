from datetime import date

from app import db
from app.models.boleto import Boleto
from app.models.conta_receber import ContaReceber


class RecebimentoService:

    @staticmethod
    def receber(
        boleto_id,
        data_recebimento=None,
    ):
        """
        Efetua o recebimento de um boleto.

        Atualiza:
        - Boleto
        - Conta a Receber
        """

        boleto = Boleto.query.get(boleto_id)

        if boleto is None:
            raise ValueError(
                "Boleto não encontrado."
            )

        if boleto.status == 1:
            raise ValueError(
                "Boleto já recebido."
            )

        if data_recebimento is None:
            data_recebimento = date.today()

        conta = ContaReceber.query.filter_by(
            boleto_id=boleto.id
        ).first()

        if conta is None:
            raise ValueError(
                "Conta a receber não encontrada."
            )

        boleto.status = 1
        boleto.data_recebimento = data_recebimento

        conta.status = 1
        conta.data_recebimento = data_recebimento

        db.session.commit()

        return boleto

    @staticmethod
    def cancelar_recebimento(
        boleto_id,
    ):

        boleto = Boleto.query.get(boleto_id)

        if boleto is None:
            raise ValueError(
                "Boleto não encontrado."
            )

        conta = ContaReceber.query.filter_by(
            boleto_id=boleto.id
        ).first()

        boleto.status = 0
        boleto.data_recebimento = None

        if conta:
            conta.status = 0
            conta.data_recebimento = None

        db.session.commit()

        return boleto

    @staticmethod
    def receber_lote(
        boletos,
        data_recebimento=None,
    ):

        if data_recebimento is None:
            data_recebimento = date.today()

        quantidade = 0

        for boleto in boletos:

            if boleto.status == 0:

                boleto.status = 1
                boleto.data_recebimento = data_recebimento

                conta = ContaReceber.query.filter_by(
                    boleto_id=boleto.id
                ).first()

                if conta:

                    conta.status = 1
                    conta.data_recebimento = data_recebimento

                quantidade += 1

        db.session.commit()

        return quantidade