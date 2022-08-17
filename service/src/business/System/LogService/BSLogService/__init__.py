try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSLogService import DSLogService
from naver_core import *

def BSLogService(input):
    try:
        result = DSLogService(input)
        return result

    except Exception as e:
        raise e