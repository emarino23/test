"""recoveryform module."""
from wtforms import Form, PasswordField, validators


class RecoveryForm(Form):
    """.
    
        _summary_

    Args:
        Form (_type_): _description_
    """

    password = PasswordField('Nueva Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Contraseñas deben coincidir')
    ])
    confirm = PasswordField('Repita Contraseña')
