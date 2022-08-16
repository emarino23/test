try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSMakeEmail import FSMakeEmail
from .BSMakeEmail import BSMakeEmail
from .DSMakeEmail import DSMakeEmail


class MakeEmail():
    def __init__(self):
        self.FSMakeEmail = FSMakeEmail
        self.BSMakeEmail = BSMakeEmail
        self.DSMakeEmail = DSMakeEmail