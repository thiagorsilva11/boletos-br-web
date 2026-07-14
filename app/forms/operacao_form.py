from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    TextAreaField,
    SubmitField
)
from wtforms.validators import DataRequired


class OperacaoForm(FlaskForm):

    cliente_id = SelectField(
        "Representante",
        coerce=int,
        validators=[DataRequired()]
    )

    fabrica_id = SelectField(
        "Fábrica",
        coerce=int,
        validators=[DataRequired()]
    )

    colaborador_id = SelectField(
        "Colaborador",
        coerce=int,
        validators=[DataRequired()]
    )

    data_operacao = DateField(
        "Data da Operação",
        validators=[DataRequired()]
    )

    observacao = TextAreaField(
        "Observações"
    )

    submit = SubmitField("Salvar")