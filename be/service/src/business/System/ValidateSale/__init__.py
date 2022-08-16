try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateSale import FSValidateSale
from .BSValidateSale import BSValidateSale
from .DSValidateSale import DSValidateSale


class ValidateSale():
    def __init__(self):
        self.FSValidateSale = FSValidateSale
        self.BSValidateSale = BSValidateSale
        self.DSValidateSale = DSValidateSale