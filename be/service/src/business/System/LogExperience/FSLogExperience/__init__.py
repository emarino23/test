try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSLogExperience import BSLogExperience
from naver_core import *

def FSLogExperience(input):
    try:
        result = BSLogExperience(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)