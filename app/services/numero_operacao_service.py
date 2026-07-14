from datetime import datetime

from app import db
from app.models.parametro import Parametro


class NumeroOperacaoService:

    @staticmethod
    def gerar():

        parametro = Parametro.query.first()

        if parametro is None:
            raise Exception(
                "Cadastre os parâmetros do sistema antes de criar uma operação."
            )

        sequencia = parametro.numero_operacao

        numero = f"01{sequencia:04d}{datetime.now().strftime('%d%m%y')}"

        parametro.numero_operacao += 1

        db.session.commit()

        return numero