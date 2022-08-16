try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdatePlaylist import FSUpdatePlaylist
from .BSUpdatePlaylist import BSUpdatePlaylist
from .DSUpdatePlaylist import DSUpdatePlaylist


class UpdatePlaylist():
    def __init__(self):
        self.FSUpdatePlaylist = FSUpdatePlaylist
        self.BSUpdatePlaylist = BSUpdatePlaylist
        self.DSUpdatePlaylist = DSUpdatePlaylist
