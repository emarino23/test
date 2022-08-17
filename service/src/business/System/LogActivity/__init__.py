try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogActivity import FSLogActivity
from .BSLogActivity import BSLogActivity
from .DSLogActivity import DSLogActivity


class LogActivity():
    def __init__(self):
        self.FSLogActivity = FSLogActivity
        self.BSLogActivity = BSLogActivity
        self.DSLogActivity = DSLogActivity