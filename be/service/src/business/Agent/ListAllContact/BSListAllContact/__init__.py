try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSListAllContact import DSListAllContact
from naver_core import *

def BSListAllContact(input):
    try:
        result = DSListAllContact(input)
        return result

    except Exception as e:
        raise e