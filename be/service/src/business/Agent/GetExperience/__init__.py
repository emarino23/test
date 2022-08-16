try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSGetExperience import FSGetExperience
from .BSGetExperience import BSGetExperience
from .DSGetExperience import DSGetExperience


class GetExperience():
    def __init__(self):
        self.FSGetExperience = FSGetExperience
        self.BSGetExperience = BSGetExperience
        self.DSGetExperience = DSGetExperience