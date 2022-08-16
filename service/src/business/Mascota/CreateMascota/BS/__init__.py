try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DS import DSCreateMascota
from naver_core import *

def BSCreateMascota(data):
    try:
        result = DSCreateMascota(data)
        if(len(result) > 0):
            result["session"].commit()
            return True
        else:
            raise Exception("Problema en grabar mascota")

    except Exception as e:
        raise e