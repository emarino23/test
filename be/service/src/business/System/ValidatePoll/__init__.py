try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidatePoll import FSValidatePoll
from .BSValidatePoll import BSValidatePoll
from .DSValidatePoll import DSValidatePoll


class ValidatePoll():
    def __init__(self):
        self.FSValidatePoll = FSValidatePoll
        self.BSValidatePoll = BSValidatePoll
        self.DSValidatePoll = DSValidatePoll