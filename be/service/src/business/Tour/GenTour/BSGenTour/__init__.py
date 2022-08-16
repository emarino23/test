try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGenTour import DSGenTour

from naver_core import *


def BSGenTour(input):
    """_summary_

    Args:
        input (_type_): _description_

    Raises:
        Exception: _description_
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
       
        result =  DSGenTour(input)[0]["detail"]
        return result
    except Exception as e:
        raise e
