try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateTour import FSUpdateTour
from .BSUpdateTour import BSUpdateTour
from .DSUpdateTour import DSUpdateTour


class UpdateTour():
    def __init__(self):
        self.FSUpdateTour = FSUpdateTour
        self.BSUpdateTour = BSUpdateTour
        self.DSUpdateTour = DSUpdateTour