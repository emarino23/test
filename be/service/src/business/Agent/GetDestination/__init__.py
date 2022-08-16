try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetDestination import FSGetDestination
from .BSGetDestination import BSGetDestination
from .DSGetDestination import DSGetDestination


class GetDestination():
    def __init__(self):
        self.FSGetDestination = FSGetDestination
        self.BSGetDestination = BSGetDestination
        self.DSGetDestination = DSGetDestination