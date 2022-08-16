try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateCatalog import FSCreateCatalog
from .BSCreateCatalog import BSCreateCatalog
from .DSCreateCatalog import DSCreateCatalog


class CreateCatalog():
    def __init__(self):
        self.FSCreateCatalog = FSCreateCatalog
        self.BSCreateCatalog = BSCreateCatalog
        self.DSCreateCatalog = DSCreateCatalog