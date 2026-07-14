from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField
)
from wtforms.validators import DataRequired


class ClienteForm(FlaskForm):

    representante = StringField(
        "Representante",
        validators=[DataRequired()]
    )

    responsavel = StringField(
        "Responsável",
        validators=[DataRequired()]
    )

    cpf = StringField(
        "CPF"
    )

    telefone = StringField(
        "Telefone"
    )

    endereco = StringField(
        "Endereço"
    )

    observacoes = TextAreaField(
        "Observações"
    )

    submit = SubmitField("Salvar")