try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogPoll import FSLogPoll
from .BSLogPoll import BSLogPoll
from .DSLogPoll import DSLogPoll


class LogPoll():
    def __init__(self):
        self.FSLogPoll = FSLogPoll
        self.BSLogPoll = BSLogPoll
        self.DSLogPoll = DSLogPoll