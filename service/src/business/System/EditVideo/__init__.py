try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSEditVideo import FSEditVideo
from .BSEditVideo import BSEditVideo
from .DSEditVideo import DSEditVideo


class EditVideo():
    def __init__(self):
        self.FSEditVideo = FSEditVideo
        self.BSEditVideo = BSEditVideo
        self.DSEditVideo = DSEditVideo
