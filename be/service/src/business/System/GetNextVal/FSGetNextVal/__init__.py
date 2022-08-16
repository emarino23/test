try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSGetNextVal import BSGetNextVal
from naver_core import *

def FSGetNextVal(input):
    try:
        table = input.get('table')
        field = input.get('field')
        result = BSGetNextVal(field, table)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)