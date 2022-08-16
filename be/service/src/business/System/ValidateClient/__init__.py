try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateClient import FSValidateClient
from .BSValidateClient import BSValidateClient
from .DSValidateClient import DSValidateClient


class ValidateClient():
    def __init__(self):
        self.FSValidateClient = FSValidateClient
        self.BSValidateClient = BSValidateClient
        self.DSValidateClient = DSValidateClient