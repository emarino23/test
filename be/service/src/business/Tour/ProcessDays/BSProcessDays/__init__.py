try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSProcessDays import DSProcessDays 
from naver_core import *


def BSProcessDays(tour_id, destination):
    """Método de Negocio para procresar dias de un Tour

    Args:
        tour_id (int): identificacion del tour
        destination (dict): destino

    Raises:
        e: error de proceso

    Returns:
        res: resultado de la operación
    """
    try: 
        res =  DSProcessDays(tour_id, destination)
        return res
    except Exception as e:
        raise e
