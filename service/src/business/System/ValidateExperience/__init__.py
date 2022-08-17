try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateExperience import FSValidateExperience
from .BSValidateExperience import BSValidateExperience
from .DSValidateExperience import DSValidateExperience


class ValidateExperience():
    def __init__(self):
        self.FSValidateExperience = FSValidateExperience
        self.BSValidateExperience = BSValidateExperience
        self.DSValidateExperience = DSValidateExperience