try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSSendSms import FSSendSms
from .BSSendSms import BSSendSms
from .DSSendSms import DSSendSms


class SendSms():
    def __init__(self):
        self.FSSendSms = FSSendSms
        self.BSSendSms = BSSendSms
        self.DSSendSms = DSSendSms