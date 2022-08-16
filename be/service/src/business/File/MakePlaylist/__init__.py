try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSMakePlaylist import FSMakePlaylist
from .BSMakePlaylist import BSMakePlaylist
from .DSMakePlaylist import DSMakePlaylist


class MakePlaylist():
    def __init__(self):
        self.FSMakePlaylist = FSMakePlaylist
        self.BSMakePlaylist = BSMakePlaylist
        self.DSMakePlaylist = DSMakePlaylist