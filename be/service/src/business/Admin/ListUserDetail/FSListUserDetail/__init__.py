try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSListUserDetail import BSListUserDetail
from naver_core import *

def FSListUserDetail(input):
    try:
        result = BSListUserDetail(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)