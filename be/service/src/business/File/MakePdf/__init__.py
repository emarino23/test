try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSMakePdf import FSMakePdf
from .BSMakePdf import BSMakePdf
from .DSMakePdf import DSMakePdf


class MakePdf():
    def __init__(self):
        self.FSMakePdf = FSMakePdf
        self.BSMakePdf = BSMakePdf
        self.DSMakePdf = DSMakePdf