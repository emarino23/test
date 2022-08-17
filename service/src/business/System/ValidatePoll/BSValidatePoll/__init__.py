try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidatePoll import DSValidatePoll
from naver_core import *

def BSValidatePoll(input):
    try:
        result = DSValidatePoll(input)
        return result

    except Exception as e:
        raise e