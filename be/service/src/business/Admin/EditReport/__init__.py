try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditReport import FSEditReport
from .BSEditReport import BSEditReport
from .DSEditReport import DSEditReport


class EditReport():
    def __init__(self):
        self.FSEditReport = FSEditReport
        self.BSEditReport = BSEditReport
        self.DSEditReport = DSEditReport