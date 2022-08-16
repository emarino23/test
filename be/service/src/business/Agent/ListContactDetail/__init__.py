try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListContactDetail import FSListContactDetail
from .BSListContactDetail import BSListContactDetail
from .DSListContactDetail import DSListContactDetail


class ListContactDetail():
    def __init__(self):
        self.FSListContactDetail = FSListContactDetail
        self.BSListContactDetail = BSListContactDetail
        self.DSListContactDetail = DSListContactDetail