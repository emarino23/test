try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogClient import FSLogClient
from .BSLogClient import BSLogClient
from .DSLogClient import DSLogClient


class LogClient():
    def __init__(self):
        self.FSLogClient = FSLogClient
        self.BSLogClient = BSLogClient
        self.DSLogClient = DSLogClient