try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogNotification import FSLogNotification
from .BSLogNotification import BSLogNotification
from .DSLogNotification import DSLogNotification


class LogNotification():
    def __init__(self):
        self.FSLogNotification = FSLogNotification
        self.BSLogNotification = BSLogNotification
        self.DSLogNotification = DSLogNotification