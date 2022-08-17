try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateProspect import FSValidateProspect
from .BSValidateProspect import BSValidateProspect
from .DSValidateProspect import DSValidateProspect


class ValidateProspect():
    def __init__(self):
        self.FSValidateProspect = FSValidateProspect
        self.BSValidateProspect = BSValidateProspect
        self.DSValidateProspect = DSValidateProspect