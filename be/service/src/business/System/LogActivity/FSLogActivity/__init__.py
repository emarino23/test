try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSLogActivity import BSLogActivity
from naver_core import *

def FSLogActivity(input):
    try:
        result = BSLogActivity(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)