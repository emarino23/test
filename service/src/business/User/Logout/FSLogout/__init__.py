try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSLogout import BSLogout
from naver_core import *

def FSLogout(data):
    """Método de fachada para desconexión de usuario.

    Args:
        data (dict): Diccionario con los datos de la petición.

    Returns:
        boolean: True si la desconexión se realizó correctamente, False en caso contrario.
    """    
    try:
        result = BSLogout(data)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e) 