try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSValidateProspect import BSValidateProspect
from naver_core import *

def FSValidateProspect(input):
    try:
        result = BSValidateProspect(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)