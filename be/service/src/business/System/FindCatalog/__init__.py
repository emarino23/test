try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindCatalog import FSFindCatalog
from .BSFindCatalog import BSFindCatalog
from .DSFindCatalog import DSFindCatalog


class FindCatalog():
    def __init__(self):
        self.FSFindCatalog = FSFindCatalog
        self.BSFindCatalog = BSFindCatalog
        self.DSFindCatalog = DSFindCatalog