try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSConnect import FSConnect
from .BSConnect import BSConnect
from .DSConnect import DSConnect


class Connect():
    def __init__(self):
        self.FSConnect = FSConnect
        self.BSConnect = BSConnect
        self.DSConnect = DSConnect