try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSNewMatch import FSNewMatch
from .BSNewMatch import BSNewMatch
from .DSNewMatch import DSNewMatch


class NewMatch():
    def __init__(self):
        self.FSNewMatch = FSNewMatch
        self.BSNewMatch = BSNewMatch
        self.DSNewMatch = DSNewMatch