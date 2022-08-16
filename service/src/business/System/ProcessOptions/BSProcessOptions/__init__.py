try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSProcessOptions import DSProcessOptions
from naver_core import *

def BSProcessOptions(tour_id):
    try:
        result = DSProcessOptions(tour_id)
        return result

    except Exception as e:
        raise e