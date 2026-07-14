from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from app.forms.colaborador_form import ColaboradorForm
from app.services.colaborador_service import ColaboradorService

colaboradores_bp = Blueprint(
    "colaboradores",
    __name__,
    url_prefix="/colaboradores"
)


@colaboradores_bp.route("/")
def listar():

    busca = request.args.get("busca", "").strip()

    colaboradores = ColaboradorService.listar(busca)

    return render_template(
        "colaboradores/lista.html",
        colaboradores=colaboradores,
        busca=busca
    )


@colaboradores_bp.route("/novo", methods=["GET", "POST"])
def novo():

    form = ColaboradorForm()

    if form.validate_on_submit():

        ColaboradorService.criar(form)

        flash(
            "Colaborador cadastrado com sucesso.",
            "success"
        )

        return redirect(
            url_for("colaboradores.listar")
        )

    return render_template(
        "colaboradores/novo.html",
        form=form
    )


@colaboradores_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    colaborador = ColaboradorService.buscar(id)

    form = ColaboradorForm(obj=colaborador)

    if form.validate_on_submit():

        ColaboradorService.atualizar(colaborador, form)

        flash(
            "Colaborador atualizado com sucesso.",
            "success"
        )

        return redirect(
            url_for("colaboradores.listar")
        )

    return render_template(
        "colaboradores/novo.html",
        form=form
    )


@colaboradores_bp.route("/excluir/<int:id>")
def excluir(id):

    colaborador = ColaboradorService.buscar(id)

    ColaboradorService.excluir(colaborador)

    flash(
        "Colaborador excluído com sucesso.",
        "success"
    )

    return redirect(
        url_for("colaboradores.listar")
    )