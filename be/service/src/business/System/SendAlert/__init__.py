try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSSendAlert import FSSendAlert
from .BSSendAlert import BSSendAlert
from .DSSendAlert import DSSendAlert


class SendAlert():
    def __init__(self):
        self.FSSendAlert = FSSendAlert
        self.BSSendAlert = BSSendAlert
        self.DSSendAlert = DSSendAlert