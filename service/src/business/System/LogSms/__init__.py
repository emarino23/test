try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogSms import FSLogSms
from .BSLogSms import BSLogSms
from .DSLogSms import DSLogSms


class LogSms():
    def __init__(self):
        self.FSLogSms = FSLogSms
        self.BSLogSms = BSLogSms
        self.DSLogSms = DSLogSms