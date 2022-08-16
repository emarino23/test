try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListUserDetail import FSListUserDetail
from .BSListUserDetail import BSListUserDetail
from .DSListUserDetail import DSListUserDetail


class ListUserDetail():
    def __init__(self):
        self.FSListUserDetail = FSListUserDetail
        self.BSListUserDetail = BSListUserDetail
        self.DSListUserDetail = DSListUserDetail