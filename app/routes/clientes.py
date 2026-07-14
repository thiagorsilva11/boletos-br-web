from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from app.forms.cliente_form import ClienteForm
from app.services.cliente_service import ClienteService

clientes_bp = Blueprint(
    "clientes",
    __name__,
    url_prefix="/clientes"
)


@clientes_bp.route("/")
def listar():

    busca = request.args.get("busca", "").strip()

    clientes = ClienteService.listar(busca)

    return render_template(
        "clientes/lista.html",
        clientes=clientes,
        busca=busca
    )


@clientes_bp.route("/novo", methods=["GET", "POST"])
def novo():

    form = ClienteForm()

    if form.validate_on_submit():

        ClienteService.criar(form)

        flash(
            "Representante cadastrado com sucesso.",
            "success"
        )

        return redirect(
            url_for("clientes.listar")
        )

    return render_template(
        "clientes/novo.html",
        form=form
    )


@clientes_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    cliente = ClienteService.buscar(id)

    form = ClienteForm(obj=cliente)

    if form.validate_on_submit():

        ClienteService.atualizar(cliente, form)

        flash(
            "Representante atualizado com sucesso.",
            "success"
        )

        return redirect(
            url_for("clientes.listar")
        )

    return render_template(
        "clientes/novo.html",
        form=form
    )


@clientes_bp.route("/excluir/<int:id>")
def excluir(id):

    cliente = ClienteService.buscar(id)

    ClienteService.excluir(cliente)

    flash(
        "Representante excluído com sucesso.",
        "success"
    )

    return redirect(
        url_for("clientes.listar"))