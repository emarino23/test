try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateService import FSValidateService
from .BSValidateService import BSValidateService
from .DSValidateService import DSValidateService


class ValidateService():
    def __init__(self):
        self.FSValidateService = FSValidateService
        self.BSValidateService = BSValidateService
        self.DSValidateService = DSValidateService