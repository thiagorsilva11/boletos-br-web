from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DecimalField,
    TextAreaField,
    SubmitField
)
from wtforms.validators import DataRequired


class FabricaForm(FlaskForm):

    nome = StringField(
        "Nome da Fábrica",
        validators=[DataRequired()]
    )

    endereco = StringField(
        "Endereço"
    )

    telefone = StringField(
        "Telefone"
    )

    percentual_comissao = DecimalField(
        "Comissão (%)",
        places=2,
        default=0
    )

    observacoes = TextAreaField(
        "Observações"
    )

    submit = SubmitField(
        "Salvar"
    )