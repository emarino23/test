try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindTour import FSFindTour
from .BSFindTour import BSFindTour
from .DSFindTour import DSFindTour


class FindTour():
    def __init__(self):
        self.FSFindTour = FSFindTour
        self.BSFindTour = BSFindTour
        self.DSFindTour = DSFindTour