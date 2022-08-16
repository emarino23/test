try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FS import FSGetMascota
from .BS import BSGetMascota
from .DS import DSGetMascota


class GetMascota():
    def __init__(self):
        self.FSGetMascota = FSGetMascota
        self.BSGetMascota = BSGetMascota
        self.DSGetMascota = DSGetMascota