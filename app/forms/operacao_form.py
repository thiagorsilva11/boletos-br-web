from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import DataRequired


class OperacaoForm(FlaskForm):

    cliente_id = SelectField(
        "Representante",
        coerce=int,
        validators=[DataRequired()],
        render_kw={"class": "form-select"},
    )

    fabrica_id = SelectField(
        "Fábrica",
        coerce=int,
        validators=[DataRequired()],
        render_kw={"class": "form-select"},
    )

    colaborador_id = SelectField(
        "Colaborador",
        coerce=int,
        validators=[DataRequired()],
        render_kw={"class": "form-select"},
    )

    data_operacao = DateField(
        "Data da Operação",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    observacao = TextAreaField(
        "Observações",
        render_kw={
            "class": "form-control",
            "rows": 3,
            "maxlength": 500,
            "placeholder": "Observações da operação (opcional)"
        },
    )

    submit = SubmitField(
        "Salvar Operação",
        render_kw={"class": "btn btn-primary"},
    )