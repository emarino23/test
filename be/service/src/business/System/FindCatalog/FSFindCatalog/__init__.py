try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSFindCatalog import BSFindCatalog
from naver_core import *
import ast


def FSFindCatalog(input):
    try:
        result = BSFindCatalog(input)
        return Ok(result, True)

    except Exception as e:
        return ErrorResponse(e)
