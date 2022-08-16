try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeleteReport import FSDeleteReport
from .BSDeleteReport import BSDeleteReport
from .DSDeleteReport import DSDeleteReport


class DeleteReport():
    def __init__(self):
        self.FSDeleteReport = FSDeleteReport
        self.BSDeleteReport = BSDeleteReport
        self.DSDeleteReport = DSDeleteReport