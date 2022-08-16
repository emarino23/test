try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSLogConnection import BSLogConnection
from naver_core import *

def FSLogConnection():
    """Método para crear un nuevo Sesión.

    

    Returns:
        json: Resultado del API.
    """
    try:
        result = BSLogConnection()
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e) 