try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogAlert import FSLogAlert
from .BSLogAlert import BSLogAlert
from .DSLogAlert import DSLogAlert


class LogAlert():
    def __init__(self):
        self.FSLogAlert = FSLogAlert
        self.BSLogAlert = BSLogAlert
        self.DSLogAlert = DSLogAlert