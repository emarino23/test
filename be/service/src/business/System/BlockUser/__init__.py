try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSBlockUser import FSBlockUser
from .BSBlockUser import BSBlockUser
from .DSBlockUser import DSBlockUser


class BlockUser():
    def __init__(self):
        self.FSBlockUser = FSBlockUser
        self.BSBlockUser = BSBlockUser
        self.DSBlockUser = DSBlockUser