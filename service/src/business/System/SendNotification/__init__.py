try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSSendNotification import FSSendNotification
from .BSSendNotification import BSSendNotification
from .DSSendNotification import DSSendNotification


class SendNotification():
    def __init__(self):
        self.FSSendNotification = FSSendNotification
        self.BSSendNotification = BSSendNotification
        self.DSSendNotification = DSSendNotification