try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogProblem import FSLogProblem
from .BSLogProblem import BSLogProblem
from .DSLogProblem import DSLogProblem


class LogProblem():
    def __init__(self):
        self.FSLogProblem = FSLogProblem
        self.BSLogProblem = BSLogProblem
        self.DSLogProblem = DSLogProblem