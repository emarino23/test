try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogout import FSLogout
from .BSLogout import BSLogout
from .DSLogout import DSLogout


class Logout():
    def __init__(self):
        self.FSLogout = FSLogout
        self.BSLogout = BSLogout
        self.DSLogout = DSLogout