from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DecimalField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange,
)


class FabricaForm(FlaskForm):

    nome = StringField(
        "Nome da Fábrica",
        validators=[
            DataRequired(),
            Length(max=150),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Nome da fábrica",
        },
    )

    endereco = StringField(
        "Endereço",
        validators=[
            Length(max=250),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Endereço (opcional)",
        },
    )

    telefone = StringField(
        "Telefone",
        validators=[
            Length(max=20),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "(00) 00000-0000",
        },
    )

    percentual_comissao = DecimalField(
        "Comissão (%)",
        places=2,
        default=0,
        validators=[
            NumberRange(min=0, max=100),
        ],
        render_kw={
            "class": "form-control",
            "step": "0.01",
            "min": "0",
            "max": "100",
        },
    )

    observacoes = TextAreaField(
        "Observações",
        validators=[
            Length(max=500),
        ],
        render_kw={
            "class": "form-control",
            "rows": 3,
            "maxlength": 500,
            "placeholder": "Observações (opcional)",
        },
    )

    submit = SubmitField(
        "Salvar Fábrica",
        render_kw={
            "class": "btn btn-primary",
        },
    )