try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidatePay import FSValidatePay
from .BSValidatePay import BSValidatePay
from .DSValidatePay import DSValidatePay


class ValidatePay():
    def __init__(self):
        self.FSValidatePay = FSValidatePay
        self.BSValidatePay = BSValidatePay
        self.DSValidatePay = DSValidatePay