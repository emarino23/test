try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSCreateUser import FSCreateUser
from .BSCreateUser import BSCreateUser
from .DSCreateUser import DSCreateUser


class CreateUser():
    def __init__(self):
        self.FSCreateUser = FSCreateUser
        self.BSCreateUser = BSCreateUser
        self.DSCreateUser = DSCreateUser