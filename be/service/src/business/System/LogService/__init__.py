try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogService import FSLogService
from .BSLogService import BSLogService
from .DSLogService import DSLogService


class LogService():
    def __init__(self):
        self.FSLogService = FSLogService
        self.BSLogService = BSLogService
        self.DSLogService = DSLogService