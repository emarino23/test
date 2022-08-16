try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSProcessOptions import BSProcessOptions
from naver_core import *
from naver_core import *

def FSProcessOptions(input):
    try:
        tour_id = getValue(input, 'tour_id')
        result = BSProcessOptions(tour_id)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e) 