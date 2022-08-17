try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSLogProspect import BSLogProspect
from naver_core import *

def FSLogProspect(input):
    try:
        result = BSLogProspect(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)