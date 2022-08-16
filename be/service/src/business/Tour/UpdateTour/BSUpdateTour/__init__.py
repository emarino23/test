try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSUpdateTour import DSUpdateTour
from ...PromoteTour import PromoteTour
from ...CancelTour import CancelTour
from naver_core import *


def BSUpdateTour(input):
    """Método que confirma registro de usuario

    Args:
        input (dict): usuario de entrada

    Raises:
        Exception:  Error de validación de usuario

    Returns:
        boolean: True si el usuario se confirma, False si no
    """
    try:
        state = input.get("state")
        id = input.get('id')
        if state == 'update':
            result = DSUpdateTour(input)
            if len(result) > 0:
                result['session'].commit()
                return True
            raise Exception(605, 'Error de Actualización de Cotización')
        if state == 'cancel':
            result = CancelTour().DSCancelTour(id)
            if len(result) > 0:
                result['session'].commit()
                return True
            raise Exception(605, 'Error de Cancelado de Cotización')
        if state == 'promote':
            result = PromoteTour().DSPromoteTour(id)
            if len(result) > 0:
                result['session'].commit()
                return True
            raise Exception(605, 'Error de Promoción de Cotización')
    except Exception as e:
        raise e
