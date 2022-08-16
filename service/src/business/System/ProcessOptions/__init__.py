try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSProcessOptions import FSProcessOptions
from .BSProcessOptions import BSProcessOptions
from .DSProcessOptions import DSProcessOptions


class ProcessOptions():
    def __init__(self):
        self.FSProcessOptions = FSProcessOptions
        self.BSProcessOptions = BSProcessOptions
        self.DSProcessOptions = DSProcessOptions