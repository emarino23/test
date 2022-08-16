try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSClientEdit import FSClientEdit
from .BSClientEdit import BSClientEdit
from .DSClientEdit import DSClientEdit


class ClientEdit():
    def __init__(self):
        self.FSClientEdit = FSClientEdit
        self.BSClientEdit = BSClientEdit
        self.DSClientEdit = DSClientEdit