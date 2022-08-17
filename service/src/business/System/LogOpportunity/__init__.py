try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogOpportunity import FSLogOpportunity
from .BSLogOpportunity import BSLogOpportunity
from .DSLogOpportunity import DSLogOpportunity


class LogOpportunity():
    def __init__(self):
        self.FSLogOpportunity = FSLogOpportunity
        self.BSLogOpportunity = BSLogOpportunity
        self.DSLogOpportunity = DSLogOpportunity