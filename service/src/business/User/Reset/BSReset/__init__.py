try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSReset import DSReset
from src.business.System import SendEmail
from naver_core import *
 
 
def BSReset(input):
    try:
        email= getValue(input, 'email')
        if email is not None:
            result = DSReset(email)
            if isinstance(result, list):
                if len(result) > 0:
                    res = SendEmail().BSSendEmail(input, "forgot")
                    return res
        raise Exception(608, 'Error de Email')
    except Exception as e:
        raise e
