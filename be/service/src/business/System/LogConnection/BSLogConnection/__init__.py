try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLogConnection import DSLogConnection
from naver_core import *
# from naver_web import *

def BSLogConnection	(config):
    """Método para Controlar una nueva Sesión.

    Args:
        data (dict): Diccionario con los datos del Sesión.

    Returns:
	    bool: True si se creó correctamente, False en caso contrario.
    """
    try:
        pksalt = config.core.myVariables['PKSALT']
        # result = sendsalt(pksalt)
        result = (pksalt)
        return result

    except Exception as e:
        raise e
