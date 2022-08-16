try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateUser import DSValidateUser
from naver_core import *


def BSValidateUser(input):
    """Método para validar usuário en banco de dados.

    Args:
        input (dict):  datos de entrada del usuario

    Raises:
        e: error de conexión a base de datos

    Returns:
        boolean: True si el usuario existe en la base de datos, False si no existe
    """
    try:
       
        username= getValue(input, 'username')
        result = DSValidateUser(username)
        if isinstance(result, list):
            if len(result) > 0:
                return True
        return False
    except Exception as e:
        raise e
