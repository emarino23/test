try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateOpportunity import FSCreateOpportunity
from .BSCreateOpportunity import BSCreateOpportunity
from .DSCreateOpportunity import DSCreateOpportunity


class CreateOpportunity():
    def __init__(self):
        self.FSCreateOpportunity = FSCreateOpportunity
        self.BSCreateOpportunity = BSCreateOpportunity
        self.DSCreateOpportunity = DSCreateOpportunity