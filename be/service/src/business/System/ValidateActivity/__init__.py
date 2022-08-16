try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateActivity import FSValidateActivity
from .BSValidateActivity import BSValidateActivity
from .DSValidateActivity import DSValidateActivity


class ValidateActivity():
    def __init__(self):
        self.FSValidateActivity = FSValidateActivity
        self.BSValidateActivity = BSValidateActivity
        self.DSValidateActivity = DSValidateActivity