try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetNextVal import FSGetNextVal
from .BSGetNextVal import BSGetNextVal
from .DSGetNextVal import DSGetNextVal


class GetNextVal():
    def __init__(self):
        self.FSGetNextVal = FSGetNextVal
        self.BSGetNextVal = BSGetNextVal
        self.DSGetNextVal = DSGetNextVal