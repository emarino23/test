try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLoadTemplate import FSLoadTemplate
from .BSLoadTemplate import BSLoadTemplate
from .DSLoadTemplate import DSLoadTemplate


class LoadTemplate():
    def __init__(self):
        self.FSLoadTemplate = FSLoadTemplate
        self.BSLoadTemplate = BSLoadTemplate
        self.DSLoadTemplate = DSLoadTemplate