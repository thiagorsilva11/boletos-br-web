from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
)

from app.forms.fabrica_form import FabricaForm
from app.services.fabrica_service import FabricaService

fabricas_bp = Blueprint(
    "fabricas",
    __name__,
    url_prefix="/fabricas",
)


@fabricas_bp.route("/")
def listar():

    busca = request.args.get("busca", "").strip()

    fabricas = FabricaService.listar(busca)

    return render_template(
        "fabricas/lista.html",
        fabricas=fabricas,
        busca=busca,
    )


@fabricas_bp.route("/novo", methods=["GET", "POST"])
def novo():

    form = FabricaForm()

    if form.validate_on_submit():

        FabricaService.criar(form)

        flash(
            "Fábrica cadastrada com sucesso.",
            "success",
        )

        return redirect(
            url_for("fabricas.listar")
        )

    return render_template(
        "fabricas/novo.html",
        form=form,
        titulo="Nova Fábrica",
        modo="novo",
    )


@fabricas_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    fabrica = FabricaService.buscar(id)

    if fabrica is None:

        flash(
            "Fábrica não encontrada.",
            "danger",
        )

        return redirect(
            url_for("fabricas.listar")
        )

    form = FabricaForm(obj=fabrica)

    if form.validate_on_submit():

        FabricaService.atualizar(
            fabrica,
            form,
        )

        flash(
            "Fábrica atualizada com sucesso.",
            "success",
        )

        return redirect(
            url_for("fabricas.listar")
        )

    return render_template(
        "fabricas/novo.html",
        form=form,
        titulo="Editar Fábrica",
        modo="editar",
    )


@fabricas_bp.route("/excluir/<int:id>")
def excluir(id):

    fabrica = FabricaService.buscar(id)

    if fabrica is None:

        flash(
            "Fábrica não encontrada.",
            "danger",
        )

        return redirect(
            url_for("fabricas.listar")
        )

    FabricaService.excluir(fabrica)

    flash(
        "Fábrica excluída com sucesso.",
        "success",
    )

    return redirect(
        url_for("fabricas.listar")
    )