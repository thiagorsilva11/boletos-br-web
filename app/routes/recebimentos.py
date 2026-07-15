from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
)

from app.repositories.boleto_repository import BoletoRepository
from app.services.recebimento_service import RecebimentoService


recebimentos_bp = Blueprint(
    "recebimentos",
    __name__,
    url_prefix="/recebimentos",
)


@recebimentos_bp.route("/")
def listar():

    boletos = BoletoRepository.listar_pendentes()

    return render_template(
        "recebimentos/lista.html",
        boletos=boletos,
    )


@recebimentos_bp.route("/receber/<int:id>")
def receber(id):

    try:

        RecebimentoService.receber(id)

        flash(
            "Boleto recebido com sucesso.",
            "success",
        )

    except Exception as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for("recebimentos.listar")
    )


@recebimentos_bp.route("/cancelar/<int:id>")
def cancelar(id):

    try:

        RecebimentoService.cancelar_recebimento(id)

        flash(
            "Recebimento cancelado.",
            "warning",
        )

    except Exception as e:

        flash(
            str(e),
            "danger",
        )

    return redirect(
        url_for("recebimentos.listar")
    )