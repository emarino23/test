try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSProcessTour import FSProcessTour
from .BSProcessTour import BSProcessTour
from .DSProcessTour import DSProcessTour


class ProcessTour():
    def __init__(self):
        self.FSProcessTour = FSProcessTour
        self.BSProcessTour = BSProcessTour
        self.DSProcessTour = DSProcessTour