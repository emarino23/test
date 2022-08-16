try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSProcessDestinations import DSProcessDestinations 
from naver_core import *


def BSProcessDestinations(id, input):
    """Método para procesar detsinos

    Args:
        id (int): Identificador del proceso
        input (dict): Diccionario con los datos del proceso

    Raises:
        Exception: Cuando no se puede procesar el proceso
        e: Cuando no se puede procesar el proceso

    Returns:
        bool: True si el proceso fue exitoso, False si no
    """ 
    try:
        
        res =  DSProcessDestinations(id, input)
        
        return res
    except Exception as e:
        raise e
