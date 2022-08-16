try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSProcessDestinations import FSProcessDestinations
from .BSProcessDestinations import BSProcessDestinations
from .DSProcessDestinations import DSProcessDestinations


class ProcessDestinations():
    def __init__(self):
        self.FSProcessDestinations = FSProcessDestinations
        self.BSProcessDestinations = BSProcessDestinations
        self.DSProcessDestinations = DSProcessDestinations