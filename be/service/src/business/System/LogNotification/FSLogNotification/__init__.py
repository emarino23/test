try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSLogNotification import BSLogNotification
from naver_core import *

def FSLogNotification(input):
    try:
        result = BSLogNotification(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)