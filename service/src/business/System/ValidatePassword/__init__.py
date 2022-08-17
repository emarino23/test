try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidatePassword import FSValidatePassword
from .BSValidatePassword import BSValidatePassword
from .DSValidatePassword import DSValidatePassword


class ValidatePassword():
    def __init__(self):
        self.FSValidatePassword = FSValidatePassword
        self.BSValidatePassword = BSValidatePassword
        self.DSValidatePassword = DSValidatePassword