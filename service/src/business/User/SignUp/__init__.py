try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSSignUp import FSSignUp
from .BSSignUp import BSSignUp
from .DSSignUp import DSSignUp


class SignUp():
    def __init__(self):
        self.FSSignUp = FSSignUp
        self.BSSignUp = BSSignUp
        self.DSSignUp = DSSignUp