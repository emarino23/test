try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FS import FSCreateMascota
from .BS import BSCreateMascota
from .DS import DSCreateMascota


class CreateMascota():
    def __init__(self):
        self.FSCreateMascota = FSCreateMascota
        self.BSCreateMascota = BSCreateMascota
        self.DSCreateMascota = DSCreateMascota