try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSDeleteReport import BSDeleteReport
from naver_core import *

def FSDeleteReport(input):
    try:
        result = BSDeleteReport(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)