try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSJoinPoll import DSJoinPoll
from naver_core import *

def BSJoinPoll(input):
    try:
        result = DSJoinPoll(input)
        return result

    except Exception as e:
        raise e