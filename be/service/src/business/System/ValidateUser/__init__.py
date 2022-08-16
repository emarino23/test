try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateUser import FSValidateUser
from .BSValidateUser import BSValidateUser
from .DSValidateUser import DSValidateUser


class ValidateUser():
    def __init__(self):
        self.FSValidateUser = FSValidateUser
        self.BSValidateUser = BSValidateUser
        self.DSValidateUser = DSValidateUser