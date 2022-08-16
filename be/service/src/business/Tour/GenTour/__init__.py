try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGenTour import FSGenTour
from .BSGenTour import BSGenTour
from .DSGenTour import DSGenTour


class GenTour():
    def __init__(self):
        self.FSGenTour = FSGenTour
        self.BSGenTour = BSGenTour
        self.DSGenTour = DSGenTour