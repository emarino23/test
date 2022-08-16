try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListAllUser import FSListAllUser
from .BSListAllUser import BSListAllUser
from .DSListAllUser import DSListAllUser


class ListAllUser():
    def __init__(self):
        self.FSListAllUser = FSListAllUser
        self.BSListAllUser = BSListAllUser
        self.DSListAllUser = DSListAllUser