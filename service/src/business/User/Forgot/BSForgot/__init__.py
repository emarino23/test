try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSForgot import DSForgot
from naver_core import *


def BSForgot(password, confirmation):
    """Método para recuperar contraseña

    Args:
        input (dict): Diccionario con los datos de entrada.
        
    Returns:
        bool: True si la contraseña fue cambiada, False en caso contrario.
    """ 
    try:
        result = DSForgot(password, confirmation)
        if len(result) > 0:
            result['session'].commit()
            return True

        raise Exception(619, "Error de Recuperar Credencial")

    except Exception as e:
        raise e
