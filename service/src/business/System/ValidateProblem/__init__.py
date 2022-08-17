try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateProblem import FSValidateProblem
from .BSValidateProblem import BSValidateProblem
from .DSValidateProblem import DSValidateProblem


class ValidateProblem():
    def __init__(self):
        self.FSValidateProblem = FSValidateProblem
        self.BSValidateProblem = BSValidateProblem
        self.DSValidateProblem = DSValidateProblem