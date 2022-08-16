try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSQuery import FSQuery
from .BSQuery import BSQuery
from .DSQuery import DSQuery


class Query():
    def __init__(self):
        self.FSQuery = FSQuery
        self.BSQuery = BSQuery
        self.DSQuery = DSQuery