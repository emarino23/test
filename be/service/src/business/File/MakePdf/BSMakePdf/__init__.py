try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSMakePdf import DSMakePdf

from naver_core import *


def BSMakePdf(input):
    """Método que confirma registro de usuario

    Args:
        input (dict): usuario de entrada

    Raises:
        Exception:  Error de validación de usuario

    Returns:
        boolean: True si el usuario se confirma, False si no
    """
    try:
        tour_id = input.get('tour_id')
        result = DSMakePdf(tour_id)
        if len(result) > 0:
            result['session'].commit()
            return True
        raise Exception(605, 'Error de MakePdfación')
    except Exception as e:
        raise e
