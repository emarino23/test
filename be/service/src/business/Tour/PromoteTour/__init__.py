try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSPromoteTour import FSPromoteTour
from .BSPromoteTour import BSPromoteTour
from .DSPromoteTour import DSPromoteTour


class PromoteTour():
    def __init__(self):
        self.FSPromoteTour = FSPromoteTour
        self.BSPromoteTour = BSPromoteTour
        self.DSPromoteTour = DSPromoteTour