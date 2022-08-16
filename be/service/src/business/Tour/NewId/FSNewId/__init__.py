try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSNewId import BSNewId
from naver_core import *
from flask import render_template, make_response

def FSNewId	(): 
    try:
        result = BSNewId()
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e) 