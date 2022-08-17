try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateProduct import FSValidateProduct
from .BSValidateProduct import BSValidateProduct
from .DSValidateProduct import DSValidateProduct


class ValidateProduct():
    def __init__(self):
        self.FSValidateProduct = FSValidateProduct
        self.BSValidateProduct = BSValidateProduct
        self.DSValidateProduct = DSValidateProduct