try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSEditContact import BSEditContact
from naver_core import *

def FSEditContact(input):
    try:
        result = BSEditContact(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)