try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidateActivity import DSValidateActivity
from naver_core import *

def BSValidateActivity(input):
    try:
        result = DSValidateActivity(input)
        return result

    except Exception as e:
        raise e