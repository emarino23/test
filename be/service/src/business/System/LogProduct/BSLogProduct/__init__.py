try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLogProduct import DSLogProduct
from naver_core import *

def BSLogProduct(input):
    try:
        result = DSLogProduct(input)
        return result

    except Exception as e:
        raise e