try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateOpportunity import FSValidateOpportunity
from .BSValidateOpportunity import BSValidateOpportunity
from .DSValidateOpportunity import DSValidateOpportunity


class ValidateOpportunity():
    def __init__(self):
        self.FSValidateOpportunity = FSValidateOpportunity
        self.BSValidateOpportunity = BSValidateOpportunity
        self.DSValidateOpportunity = DSValidateOpportunity