try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSSendEmail import FSSendEmail
from .BSSendEmail import BSSendEmail
from .DSSendEmail import DSSendEmail


class SendEmail():
    def __init__(self):
        self.FSSendEmail = FSSendEmail
        self.BSSendEmail = BSSendEmail
        self.DSSendEmail = DSSendEmail