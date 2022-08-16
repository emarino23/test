try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeleteTour import FSDeleteTour
from .BSDeleteTour import BSDeleteTour
from .DSDeleteTour import DSDeleteTour


class DeleteTour():
    def __init__(self):
        self.FSDeleteTour = FSDeleteTour
        self.BSDeleteTour = BSDeleteTour
        self.DSDeleteTour = DSDeleteTour