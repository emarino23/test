try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogProduct import FSLogProduct
from .BSLogProduct import BSLogProduct
from .DSLogProduct import DSLogProduct


class LogProduct():
    def __init__(self):
        self.FSLogProduct = FSLogProduct
        self.BSLogProduct = BSLogProduct
        self.DSLogProduct = DSLogProduct