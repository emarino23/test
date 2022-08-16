try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateTour import FSValidateTour
from .BSValidateTour import BSValidateTour
from .DSValidateTour import DSValidateTour


class ValidateTour():
    def __init__(self):
        self.FSValidateTour = FSValidateTour
        self.BSValidateTour = BSValidateTour
        self.DSValidateTour = DSValidateTour