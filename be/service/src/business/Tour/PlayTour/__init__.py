try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSPlayTour import FSPlayTour
from .BSPlayTour import BSPlayTour
from .DSPlayTour import DSPlayTour


class PlayTour():
    def __init__(self):
        self.FSPlayTour = FSPlayTour
        self.BSPlayTour = BSPlayTour
        self.DSPlayTour = DSPlayTour