try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogUser import FSLogUser
from .BSLogUser import BSLogUser
from .DSLogUser import DSLogUser


class LogUser():
    def __init__(self):
        self.FSLogUser = FSLogUser
        self.BSLogUser = BSLogUser
        self.DSLogUser = DSLogUser