try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSConfirm import FSConfirm
from .BSConfirm import BSConfirm
from .DSConfirm import DSConfirm


class Confirm():
    def __init__(self):
        self.FSConfirm = FSConfirm
        self.BSConfirm = BSConfirm
        self.DSConfirm = DSConfirm