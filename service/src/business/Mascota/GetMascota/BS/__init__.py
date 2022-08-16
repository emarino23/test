try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DS import DSGetMascota
from naver_core import *

def BSGetMascota(id):
    try:
        result = DSGetMascota(id)
        return result

    except Exception as e:
        raise e