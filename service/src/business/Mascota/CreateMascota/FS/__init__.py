try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BS import BSCreateMascota
from naver_core import *

def FSCreateMascota(input):
    try:
        data = input.get("data")[0]
        result = BSCreateMascota(data)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)