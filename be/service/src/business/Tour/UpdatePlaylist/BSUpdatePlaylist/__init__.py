try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSUpdatePlaylist import DSUpdatePlaylist
from ...PromoteTour import PromoteTour
from ...CancelTour import CancelTour
from naver_core import *


def BSUpdatePlaylist(playlist):
    """Método que confirma registro de usuario

    Args:
        playlist (dict): usuario de entrada

    Raises:
        Exception:  Error de validación de usuario

    Returns:
        boolean: True si el usuario se confirma, False si no
    """
    try:
        res = DSUpdatePlaylist(playlist)
        if len(res) > 0:
            res["session"].commit()
        return True
    except Exception as e:
        raise e
