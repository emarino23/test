try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditContact import FSEditContact
from .BSEditContact import BSEditContact
from .DSEditContact import DSEditContact


class EditContact():
    def __init__(self):
        self.FSEditContact = FSEditContact
        self.BSEditContact = BSEditContact
        self.DSEditContact = DSEditContact