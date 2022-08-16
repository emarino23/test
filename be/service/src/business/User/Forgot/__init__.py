try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSForgot import FSForgot
from .BSForgot import BSForgot
from .DSForgot import DSForgot


class Forgot():
    def __init__(self):
        self.FSForgot = FSForgot
        self.BSForgot = BSForgot
        self.DSForgot = DSForgot