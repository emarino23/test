try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateContact import FSValidateContact
from .BSValidateContact import BSValidateContact
from .DSValidateContact import DSValidateContact


class ValidateContact():
    def __init__(self):
        self.FSValidateContact = FSValidateContact
        self.BSValidateContact = BSValidateContact
        self.DSValidateContact = DSValidateContact