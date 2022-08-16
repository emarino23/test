try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSCreateCatalog import DSCreateCatalog
from naver_core import *

    
def BSCreateCatalog(input):
    try:
        
        result = DSCreateCatalog(input)
        if len(result) > 0:
            result["session"].commit()
        return True

    except Exception as e:
        raise e
