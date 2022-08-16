try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSFindHotel import BSFindHotel
from naver_core import *
from flask import render_template, make_response


def FSFindHotel(input):
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        result = BSFindHotel(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)
