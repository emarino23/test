try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSStart import FSStart
from .BSStart import BSStart
from .DSStart import DSStart


class Start():
    def __init__(self):
        self.FSStart = FSStart
        self.BSStart = BSStart
        self.DSStart = DSStart