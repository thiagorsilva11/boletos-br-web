from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Length,
)


class ColaboradorForm(FlaskForm):

    nome = StringField(
        "Nome",
        validators=[
            DataRequired(),
            Length(max=150),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Nome do colaborador",
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

    submit = SubmitField(
        "Salvar Colaborador",
        render_kw={
            "class": "btn btn-primary",
        },
    )