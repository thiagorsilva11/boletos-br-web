from flask import Blueprint, render_template, redirect, url_for, flash

from app.forms.operacao_form import OperacaoForm
from app.models.cliente import Cliente
from app.models.colaborador import Colaborador
from app.models.fabrica import Fabrica
from app.services.operacao_service import OperacaoService

operacoes_bp = Blueprint(
    "operacoes",
    __name__,
    url_prefix="/operacoes",
)


@operacoes_bp.route("/")
def listar():
    operacoes = OperacaoService.listar()

    return render_template(
        "operacoes/lista.html",
        operacoes=operacoes,
    )


@operacoes_bp.route("/nova", methods=["GET", "POST"])
def nova():

    form = OperacaoForm()

    form.cliente_id.choices = [
        (c.id, c.representante)
        for c in Cliente.query.order_by(
            Cliente.representante
        ).all()
    ]

    form.fabrica_id.choices = [
        (f.id, f.nome)
        for f in Fabrica.query.order_by(
            Fabrica.nome
        ).all()
    ]

    form.colaborador_id.choices = [
        (c.id, c.nome)
        for c in Colaborador.query.order_by(
            Colaborador.nome
        ).all()
    ]

    if form.validate_on_submit():

        OperacaoService.criar(
            cliente_id=form.cliente_id.data,
            fabrica_id=form.fabrica_id.data,
            colaborador_id=form.colaborador_id.data,
            data_operacao=form.data_operacao.data,
            observacao=form.observacao.data,
        )

        flash(
            "Operação cadastrada com sucesso!",
            "success",
        )

        return redirect(
            url_for("operacoes.listar")
        )

    return render_template(
        "operacoes/nova.html",
        form=form,
    )