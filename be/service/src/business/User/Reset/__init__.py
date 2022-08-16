# try: 
#     __import__('pkg_resources').declare_namespace(__name__)
# except ImportError:
#     __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSReset import FSReset
from .BSReset import BSReset
from .DSReset import DSReset


class Reset():
    def __init__(self):
        self.FSReset = FSReset
        self.BSReset = BSReset
        self.DSReset = DSReset