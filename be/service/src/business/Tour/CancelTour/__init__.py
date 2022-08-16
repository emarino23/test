try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCancelTour import FSCancelTour
from .BSCancelTour import BSCancelTour
from .DSCancelTour import DSCancelTour


class CancelTour():
    def __init__(self):
        self.FSCancelTour = FSCancelTour
        self.BSCancelTour = BSCancelTour
        self.DSCancelTour = DSCancelTour