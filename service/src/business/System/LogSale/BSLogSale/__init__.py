try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLogSale import DSLogSale
from naver_core import *

def BSLogSale(input):
    try:
        result = DSLogSale(input)
        return result

    except Exception as e:
        raise e