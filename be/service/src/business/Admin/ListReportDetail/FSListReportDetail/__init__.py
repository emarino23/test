try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSListReportDetail import BSListReportDetail
from naver_core import *

def FSListReportDetail(input):
    try:
        result = BSListReportDetail(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)