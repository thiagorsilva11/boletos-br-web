from datetime import datetime

from app import db
from app.models.parametro import Parametro


class NumeroOperacaoService:

    @staticmethod
    def gerar():
        """
        Gera um número único para a operação.

        Formato:
        01 + sequência (4 dígitos) + DDMMAA

        Exemplo:
        010001150726
        """

        parametro = Parametro.obter()

        sequencia = parametro.numero_operacao

        numero = (
            f"01"
            f"{sequencia:04d}"
            f"{datetime.now():%d%m%y}"
        )

        parametro.numero_operacao += 1

        db.session.commit()

        return numero

    @staticmethod
    def visualizar_proximo():
        """
        Retorna o próximo número sem incrementar
        a sequência.
        """

        parametro = Parametro.obter()

        return (
            f"01"
            f"{parametro.numero_operacao:04d}"
            f"{datetime.now():%d%m%y}"
        )