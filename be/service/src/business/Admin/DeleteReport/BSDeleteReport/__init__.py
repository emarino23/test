try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSDeleteReport import DSDeleteReport
from naver_core import *

def BSDeleteReport(input):
    try:
        result = DSDeleteReport(input)
        return result

    except Exception as e:
        raise e