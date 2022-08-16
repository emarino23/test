try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSEditUser import DSEditUser
from naver_core import *

def BSEditUser(input):
    try:
        result = DSEditUser(input)
        return result

    except Exception as e:
        raise e