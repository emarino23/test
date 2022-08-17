try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogEmail import FSLogEmail
from .BSLogEmail import BSLogEmail
from .DSLogEmail import DSLogEmail


class LogEmail():
    def __init__(self):
        self.FSLogEmail = FSLogEmail
        self.BSLogEmail = BSLogEmail
        self.DSLogEmail = DSLogEmail