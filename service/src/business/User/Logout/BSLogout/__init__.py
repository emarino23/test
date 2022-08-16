try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLogout import DSLogout
from naver_core import *


def BSLogout(input):
    """Método de Negocio para desconectar usuario

    Args:
        input (dict): Diccionario con los datos de entrada

    Raises:
        e: Error de negocio o conexion de persistencia

    Returns:
        bool: True si se desconecto el usuario, False en caso contrario
    """    
    try:
        username = getValue(input, 'username')
        result = DSLogout(username)
        if len(result) > 0:
            result['session'].commit()
            return True
        return False

    except Exception as e:
        raise e
