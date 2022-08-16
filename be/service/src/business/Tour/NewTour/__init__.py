try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSNewTour import FSNewTour
from .BSNewTour import BSNewTour
from .DSNewTour import DSNewTour


class NewTour():
    def __init__(self):
        self.FSNewTour = FSNewTour
        self.BSNewTour = BSNewTour
        self.DSNewTour = DSNewTour