try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogSale import FSLogSale
from .BSLogSale import BSLogSale
from .DSLogSale import DSLogSale


class LogSale():
    def __init__(self):
        self.FSLogSale = FSLogSale
        self.BSLogSale = BSLogSale
        self.DSLogSale = DSLogSale