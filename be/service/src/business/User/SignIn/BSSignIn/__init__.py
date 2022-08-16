try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSSignIn import DSSignIn
from naver_core import *
from src.business.Dto import *
from src.business.System.ValidatePassword import BSValidatePassword
 


def BSSignIn(input):
    """
        Método para realizar el inicio de sesion de un usuario

    Args:
        input (dict): datos de entrada del usuario

    Raises:
        Exception: Error de conexion con la base de datos

    Returns:
        boolean: True si el usuario se ha logueado correctamente, False en caso contrario
    """
    try:
        username = getValue(input, 'username') 
        user = DSSignIn(username)
        if len(user)>0:
            valid = BSValidatePassword(input)[0]['valid']
            if valid: 
                res = ProfileDto(user[0]).__dict__()
                return res
            raise Exception(601, 'Error de Login')
        raise Exception(603, 'Error de Login')
    except Exception as e:
        raise e
