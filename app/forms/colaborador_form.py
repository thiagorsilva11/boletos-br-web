from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField
)
from wtforms.validators import DataRequired


class ColaboradorForm(FlaskForm):

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

    submit = SubmitField(
        "Salvar"
    )
    