try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditOpportunity import FSEditOpportunity
from .BSEditOpportunity import BSEditOpportunity
from .DSEditOpportunity import DSEditOpportunity


class EditOpportunity():
    def __init__(self):
        self.FSEditOpportunity = FSEditOpportunity
        self.BSEditOpportunity = BSEditOpportunity
        self.DSEditOpportunity = DSEditOpportunity