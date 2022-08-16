try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogConnection import FSLogConnection
from .BSLogConnection import BSLogConnection
from .DSLogConnection import DSLogConnection


class LogConnection():
    def __init__(self):
        self.FSLogConnection = FSLogConnection
        self.BSLogConnection = BSLogConnection
        self.DSLogConnection = DSLogConnection