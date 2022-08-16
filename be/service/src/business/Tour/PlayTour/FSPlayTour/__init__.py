try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSPlayTour import BSPlayTour
from naver_core import *

def FSPlayTour(doc):
    """Método para reproducir una lista de reproduccion de Tour.
    Args:
        doc (str): documento de entrada.

    Returns:
        json: Resultado del API.
    """
    try:
 
        result = BSPlayTour(doc)
        return result

            
        
    except Exception as e:
        raise e