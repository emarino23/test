try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSJoinPoll import FSJoinPoll
from .BSJoinPoll import BSJoinPoll
from .DSJoinPoll import DSJoinPoll


class JoinPoll():
    def __init__(self):
        self.FSJoinPoll = FSJoinPoll
        self.BSJoinPoll = BSJoinPoll
        self.DSJoinPoll = DSJoinPoll