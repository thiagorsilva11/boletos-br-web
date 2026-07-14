from app import db

from app.models.operacao import Operacao
from app.services.numero_operacao_service import NumeroOperacaoService


class OperacaoService:

    @staticmethod
    def criar(cliente_id,
              fabrica_id,
              colaborador_id,
              data_operacao,
              observacao):

        numero = NumeroOperacaoService.gerar()

        operacao = Operacao(
            numero_operacao=numero,
            cliente_id=cliente_id,
            fabrica_id=fabrica_id,
            colaborador_id=colaborador_id,
            data_operacao=data_operacao,
            observacao=observacao,
            status=0
        )

        db.session.add(operacao)
        db.session.commit()

        return operacao