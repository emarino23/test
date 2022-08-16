try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSNotify import FSNotify
from .BSNotify import BSNotify
from .DSNotify import DSNotify


class Notify():
    def __init__(self):
        self.FSNotify = FSNotify
        self.BSNotify = BSNotify
        self.DSNotify = DSNotify