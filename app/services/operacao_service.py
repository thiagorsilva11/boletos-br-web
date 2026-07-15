from app.models.operacao import Operacao
from app.repositories.operacao_repository import OperacaoRepository
from app.services.numero_operacao_service import NumeroOperacaoService


class OperacaoService:

    @staticmethod
    def criar(
        cliente_id,
        fabrica_id,
        colaborador_id,
        data_operacao,
        observacao,
    ):
        """
        Cria uma nova operação.

        Nesta versão (1.0) a operação continua
        armazenando fábrica e colaborador.

        Nas próximas versões essas informações
        passarão para os boletos.
        """

        numero = NumeroOperacaoService.gerar()

        operacao = Operacao(
            numero_operacao=numero,
            cliente_id=cliente_id,
            fabrica_id=fabrica_id,
            colaborador_id=colaborador_id,
            data_operacao=data_operacao,
            observacao=observacao,
            status=0,
        )

        try:

            OperacaoRepository.adicionar(operacao)

            OperacaoRepository.commit()

            return operacao

        except Exception:

            OperacaoRepository.rollback()

            raise

    @staticmethod
    def buscar(numero_operacao):
        return OperacaoRepository.buscar_por_numero(
            numero_operacao
        )

    @staticmethod
    def listar_abertas():
        return OperacaoRepository.listar_abertas()

    @staticmethod
    def listar_por_cliente(cliente_id):
        return OperacaoRepository.listar_por_cliente(
            cliente_id
        )