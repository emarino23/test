try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSValidatePassword import DSValidatePassword
from naver_core import *


def BSValidatePassword(input):
    try:
        username = getValue(input, 'username')
        password = getValue(input, 'password')
        result = DSValidatePassword(username, password)
        return result

    except Exception as e:
        raise e
