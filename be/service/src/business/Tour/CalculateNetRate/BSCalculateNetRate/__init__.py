try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSCalculateNetRate import DSCalculateNetRate 
from naver_core import *


def BSCalculateNetRate(input):
    """_summary_

    Args:
        input (_type_): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """

    try:
         result = DSCalculateNetRate(input)
         return result
    except Exception as e:
        raise e
