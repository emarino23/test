try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditUser import FSEditUser
from .BSEditUser import BSEditUser
from .DSEditUser import DSEditUser


class EditUser():
    def __init__(self):
        self.FSEditUser = FSEditUser
        self.BSEditUser = BSEditUser
        self.DSEditUser = DSEditUser