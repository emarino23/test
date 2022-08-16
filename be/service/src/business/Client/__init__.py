from .ClientEdit import ClientEdit
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class Client():
    def __init__(self):
        self.ClientEdit = ClientEdit() 