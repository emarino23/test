try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSLogDestiny import FSLogDestiny
from .BSLogDestiny import BSLogDestiny
from .DSLogDestiny import DSLogDestiny


class LogDestiny():
    def __init__(self):
        self.FSLogDestiny = FSLogDestiny
        self.BSLogDestiny = BSLogDestiny
        self.DSLogDestiny = DSLogDestiny