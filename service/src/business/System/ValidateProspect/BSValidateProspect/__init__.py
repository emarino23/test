try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateProspect import DSValidateProspect
from naver_core import *

def BSValidateProspect(input):
    try:
        result = DSValidateProspect(input)
        return result

    except Exception as e:
        raise e