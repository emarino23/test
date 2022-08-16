try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateContact import FSCreateContact
from .BSCreateContact import BSCreateContact
from .DSCreateContact import DSCreateContact


class CreateContact():
    def __init__(self):
        self.FSCreateContact = FSCreateContact
        self.BSCreateContact = BSCreateContact
        self.DSCreateContact = DSCreateContact