try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeleteSupplier import FSDeleteSupplier
from .BSDeleteSupplier import BSDeleteSupplier
from .DSDeleteSupplier import DSDeleteSupplier


class DeleteSupplier():
    def __init__(self):
        self.FSDeleteSupplier = FSDeleteSupplier
        self.BSDeleteSupplier = BSDeleteSupplier
        self.DSDeleteSupplier = DSDeleteSupplier