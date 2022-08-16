try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
from .FSCalculateNetRate import FSCalculateNetRate
from .BSCalculateNetRate import BSCalculateNetRate
from .DSCalculateNetRate import DSCalculateNetRate


class CalculateNetRate:
    def __init__(self):
        self.FSCalculateNetRate = FSCalculateNetRate
        self.BSCalculateNetRate = BSCalculateNetRate
        self.DSCalculateNetRate = DSCalculateNetRate
