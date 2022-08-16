try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllReport import FSListAllReport
from .BSListAllReport import BSListAllReport
from .DSListAllReport import DSListAllReport


class ListAllReport():
    def __init__(self):
        self.FSListAllReport = FSListAllReport
        self.BSListAllReport = BSListAllReport
        self.DSListAllReport = DSListAllReport