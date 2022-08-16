try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSValidateOpportunity import BSValidateOpportunity
from naver_core import *

def FSValidateOpportunity(input):
    try:
        result = BSValidateOpportunity(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)