try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSFindHotel import FSFindHotel
from .BSFindHotel import BSFindHotel
from .DSFindHotel import DSFindHotel


class FindHotel():
    def __init__(self):
        self.FSFindHotel = FSFindHotel
        self.BSFindHotel = BSFindHotel
        self.DSFindHotel = DSFindHotel
