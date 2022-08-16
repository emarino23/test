try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogProspect import FSLogProspect
from .BSLogProspect import BSLogProspect
from .DSLogProspect import DSLogProspect


class LogProspect():
    def __init__(self):
        self.FSLogProspect = FSLogProspect
        self.BSLogProspect = BSLogProspect
        self.DSLogProspect = DSLogProspect