try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

from .NewMatch import *
from .NewTour import *
from .NewId import *
from .ProcessTour import *
from .PromoteTour import *
from .UpdateTour import *
from .UpdatePlaylist import *
from .ProcessDestinations import *
from .TourEdit import *
from .CalculateNetRate import *
from .FindTour import *
from .FindCruise import *
from .FindHotel import *
from .GenTour import *
from .PlayTour import *