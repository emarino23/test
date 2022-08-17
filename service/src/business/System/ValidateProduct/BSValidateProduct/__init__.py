try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateProduct import DSValidateProduct
from naver_core import *

def BSValidateProduct(input):
    try:
        result = DSValidateProduct(input)
        return result

    except Exception as e:
        raise e