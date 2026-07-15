from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DecimalField,
    DateField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange,
)


class BoletoForm(FlaskForm):

    numero_boleto = StringField(
        "Número do Boleto",
        validators=[
            DataRequired(),
            Length(max=50),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Número do boleto",
        },
    )

    valor_compra = DecimalField(
        "Valor do Título",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0.01),
        ],
        render_kw={
            "class": "form-control",
            "step": "0.01",
        },
    )

    percentual_comissao = DecimalField(
        "Comissão (%)",
        places=2,
        validators=[
            DataRequired(),
            NumberRange(min=0, max=100),
        ],
        render_kw={
            "class": "form-control",
            "step": "0.01",
        },
    )

    data_compra = DateField(
        "Data da Compra",
        validators=[
            DataRequired(),
        ],
        render_kw={
            "class": "form-control",
        },
    )

    data_prevista_recebimento = DateField(
        "Previsão Recebimento",
        validators=[
            DataRequired(),
        ],
        render_kw={
            "class": "form-control",
        },
    )

    submit = SubmitField(
        "Adicionar Boleto",
        render_kw={
            "class": "btn btn-success",
        },
    )