from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DecimalField,
    SubmitField,
    TextAreaField
)
from wtforms.validators import DataRequired


class SocioForm(FlaskForm):

    nome = StringField(
        "Nome",
        validators=[DataRequired()]
    )

    cpf = StringField(
        "CPF"
    )

    telefone = StringField(
        "Telefone"
    )

    email = StringField(
        "E-mail"
    )

    percentual_participacao = DecimalField(
        "Participação (%)",
        places=2,
        default=0
    )

    saldo = DecimalField(
        "Saldo Inicial",
        places=2,
        default=0
    )

    observacoes = TextAreaField(
        "Observações"
    )

    submit = SubmitField(
        "Salvar"
    )