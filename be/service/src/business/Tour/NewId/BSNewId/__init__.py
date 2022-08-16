try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from src.business.System.FindCatalog import FindCatalog
from ..DSNewId import DSNewId

from naver_core import *


def BSNewId(): 
    try:
        res =  DSNewId()
        fc = FindCatalog()
        # catalogs = fc.BSFindCatalog(
        #             {"data": {"catalogs": ["ALL"]}}
        #         )
        res = {"id": res}
        return res
    except Exception as e:
        raise e
