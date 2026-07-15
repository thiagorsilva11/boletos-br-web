from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Length,
)


class ClienteForm(FlaskForm):

    representante = StringField(
        "Representante",
        validators=[
            DataRequired(),
            Length(max=150),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Nome do representante",
        },
    )

    responsavel = StringField(
        "Responsável",
        validators=[
            DataRequired(),
            Length(max=150),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Nome do responsável",
        },
    )

    cpf = StringField(
        "CPF",
        validators=[
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
            Length(max=20),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "(00) 00000-0000",
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
        "Salvar Representante",
        render_kw={
            "class": "btn btn-primary",
        },
    )