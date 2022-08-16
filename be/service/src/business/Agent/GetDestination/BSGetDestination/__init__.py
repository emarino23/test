try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSGetDestination import DSGetDestination
from naver_core import *




def BSGetDestination(destination, type):
    try:
        res = DSGetDestination(destination, type)
        return res

    except Exception as e:
        raise e


def BSGetDestination(input):
    try:
        
        res = DSGetDestination(input)
        return res

    except Exception as e:
        raise e
