try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSProcessDays import FSProcessDays
from .BSProcessDays import BSProcessDays
from .DSProcessDays import DSProcessDays


class ProcessDays():
    def __init__(self):
        self.FSProcessDays = FSProcessDays
        self.BSProcessDays = BSProcessDays
        self.DSProcessDays = DSProcessDays