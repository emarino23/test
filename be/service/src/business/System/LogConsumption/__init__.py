try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogConsumption import FSLogConsumption
from .BSLogConsumption import BSLogConsumption
from .DSLogConsumption import DSLogConsumption


class LogConsumption():
    def __init__(self):
        self.FSLogConsumption = FSLogConsumption
        self.BSLogConsumption = BSLogConsumption
        self.DSLogConsumption = DSLogConsumption