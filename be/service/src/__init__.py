try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)


from .business import *
from .infra import *


class CRS:
    def __init__(self):
        self.User = User()
        self.Agent = Agent()
        self.Client = Client()
        self.File = File()
        self.Tour = Tour()
        self.Admin = Admin()
        self.System = System()
