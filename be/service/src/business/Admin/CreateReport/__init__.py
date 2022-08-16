try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateReport import FSCreateReport
from .BSCreateReport import BSCreateReport
from .DSCreateReport import DSCreateReport


class CreateReport():
    def __init__(self):
        self.FSCreateReport = FSCreateReport
        self.BSCreateReport = BSCreateReport
        self.DSCreateReport = DSCreateReport