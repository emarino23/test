try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSTourEdit import FSTourEdit
from .BSTourEdit import BSTourEdit
from .DSTourEdit import DSTourEdit


class TourEdit():
    def __init__(self):
        self.FSTourEdit = FSTourEdit
        self.BSTourEdit = BSTourEdit
        self.DSTourEdit = DSTourEdit