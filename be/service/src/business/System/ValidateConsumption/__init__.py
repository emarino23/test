try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateConsumption import FSValidateConsumption
from .BSValidateConsumption import BSValidateConsumption
from .DSValidateConsumption import DSValidateConsumption


class ValidateConsumption():
    def __init__(self):
        self.FSValidateConsumption = FSValidateConsumption
        self.BSValidateConsumption = BSValidateConsumption
        self.DSValidateConsumption = DSValidateConsumption