try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSValidateDestiny import FSValidateDestiny
from .BSValidateDestiny import BSValidateDestiny
from .DSValidateDestiny import DSValidateDestiny


class ValidateDestiny():
    def __init__(self):
        self.FSValidateDestiny = FSValidateDestiny
        self.BSValidateDestiny = BSValidateDestiny
        self.DSValidateDestiny = DSValidateDestiny