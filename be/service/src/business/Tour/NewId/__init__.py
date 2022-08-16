try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSNewId import FSNewId
from .BSNewId import BSNewId
from .DSNewId import DSNewId


class NewId():
    def __init__(self):
        self.FSNewId = FSNewId
        self.BSNewId = BSNewId
        self.DSNewId = DSNewId