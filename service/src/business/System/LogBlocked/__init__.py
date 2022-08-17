try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogBlocked import FSLogBlocked
from .BSLogBlocked import BSLogBlocked
from .DSLogBlocked import DSLogBlocked


class LogBlocked():
    def __init__(self):
        self.FSLogBlocked = FSLogBlocked
        self.BSLogBlocked = BSLogBlocked
        self.DSLogBlocked = DSLogBlocked