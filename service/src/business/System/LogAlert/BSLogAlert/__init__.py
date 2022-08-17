try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLogAlert import DSLogAlert
from naver_core import *

def BSLogAlert(input):
    try:
        result = DSLogAlert(input)
        return result

    except Exception as e:
        raise e