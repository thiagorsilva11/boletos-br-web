from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DecimalField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange,
    Optional,
)


class SocioForm(FlaskForm):

    nome = StringField(
        "Nome",
        validators=[
            DataRequired(),
            Length(max=150),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Nome do sócio",
        },
    )

    cpf = StringField(
        "CPF",
        validators=[
            Optional(),
            Length(max=14),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "000.000.000-00",
        },
    )

    telefone = StringField(
        "Telefone",
        validators=[
            Optional(),
            Length(max=20),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "(00) 00000-0000",
        },
    )

    email = StringField(
        "E-mail",
        validators=[
            Optional(),
            Length(max=150),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "email@empresa.com.br",
        },
    )

    percentual_participacao = DecimalField(
        "Participação (%)",
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

    saldo = DecimalField(
        "Saldo Inicial",
        places=2,
        default=0,
        validators=[
            NumberRange(min=0),
        ],
        render_kw={
            "class": "form-control",
            "step": "0.01",
            "min": "0",
        },
    )

    observacoes = TextAreaField(
        "Observações",
        validators=[
            Optional(),
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
        "Salvar Sócio",
        render_kw={
            "class": "btn btn-primary",
        },
    )