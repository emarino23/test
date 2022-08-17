try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateContact import DSValidateContact
from naver_core import *

def BSValidateContact(input):
    try:
        result = DSValidateContact(input)
        return result

    except Exception as e:
        raise e