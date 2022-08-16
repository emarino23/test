try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllContact import FSListAllContact
from .BSListAllContact import BSListAllContact
from .DSListAllContact import DSListAllContact


class ListAllContact():
    def __init__(self):
        self.FSListAllContact = FSListAllContact
        self.BSListAllContact = BSListAllContact
        self.DSListAllContact = DSListAllContact