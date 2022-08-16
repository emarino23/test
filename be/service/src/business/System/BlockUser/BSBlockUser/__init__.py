try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSBlockUser import DSBlockUser
from naver_core import *

def BSBlockUser(input):
    try:
        result = DSBlockUser(input)
        return result

    except Exception as e:
        raise e