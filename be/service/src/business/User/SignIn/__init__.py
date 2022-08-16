try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSSignIn import FSSignIn
from .BSSignIn import BSSignIn
from .DSSignIn import DSSignIn


class SignIn():
    def __init__(self):
        self.FSSignIn = FSSignIn
        self.BSSignIn = BSSignIn
        self.DSSignIn = DSSignIn