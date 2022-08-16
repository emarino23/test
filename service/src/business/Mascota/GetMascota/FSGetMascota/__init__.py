try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSGetMascota import BSGetMascota
from naver_core import *

def FSGetMascota(id):
    try:
        
        result = BSGetMascota(id)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)