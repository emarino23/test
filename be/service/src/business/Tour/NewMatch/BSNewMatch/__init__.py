try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSNewMatch import DSNewMatch
from naver_core import *


def BSNewMatch(id, match):
    """Mètodo de Procesamiento de Match de Cotización

    Args:
        id (int): Identificador de la Cotización
        match (dict): Diccionario con los datos de la Cotización

    Raises:
        e: Cuando no se puede procesar la Cotización

    Returns:
        res: Resultado de la Cotización
    """
    try:
       
        res = DSNewMatch(id, match)
        return res
    except Exception as e:
        raise e
