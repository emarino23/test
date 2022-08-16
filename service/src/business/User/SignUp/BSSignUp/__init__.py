try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSSignUp import DSSignUp
from naver_core import *
from src.business.System import ValidateUser, SendEmail  


def BSSignUp(input):
    """
    Metodo para registrar un usuario en el sistema.
    Valida que el usuario no exista en la base de datos.
    Rgistra el usuario en la base de datos.

    Args:
        input (json): datos desde api/signup
    Raises:
        Exception: Error de conexion con la base de datos
        Exception: Error de conexion con la base de datos
    Returns:
        int: last_id
    """
    try:
        validuser = ValidateUser().BSValidateUser(input)
        data = input.get('data')
        if not validuser:
            res = DSSignUp(data)
            if isinstance(res, dict):
                if len(res) > 0:
                    session = res.get('session')
                    session.commit()
                    email = SendEmail().BSSendEmail(input, "confirmation")
                    if email:
                        
                        return "Se te envió un correo para confirmar!!"
                   
            raise Exception(610, "Error de datos de registro")

        raise Exception(604, "Username is already exist")
    except Exception as e:
        raise e
