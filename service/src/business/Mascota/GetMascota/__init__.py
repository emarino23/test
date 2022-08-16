try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetMascota import FSGetMascota
from .BSGetMascota import BSGetMascota
from .DSGetMascota import DSGetMascota


class GetMascota():
    def __init__(self):
        self.FSGetMascota = FSGetMascota
        self.BSGetMascota = BSGetMascota
        self.DSGetMascota = DSGetMascota