try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSDeleteUser import FSDeleteUser
from .BSDeleteUser import BSDeleteUser
from .DSDeleteUser import DSDeleteUser


class DeleteUser():
    def __init__(self):
        self.FSDeleteUser = FSDeleteUser
        self.BSDeleteUser = BSDeleteUser
        self.DSDeleteUser = DSDeleteUser