try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from .Admin import *
from .User import *
from .Agent import *
from .Client import *
from .Dto import * 
from .File import *
from .Tour import *
from .System import * 
from .User import *
