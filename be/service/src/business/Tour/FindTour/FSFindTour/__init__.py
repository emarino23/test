try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSFindTour import BSFindTour
from naver_core import *
from flask import render_template, make_response

def FSFindTour	(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        result = BSFindTour(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e) 