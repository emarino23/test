try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSNewTour import DSNewTour

from naver_core import *


def BSNewTour(input):
    """Método para crear una nueva tour 

    Args:
        input (dict): Contiene los datos de el tour
        
    Raises:
        Exception: Cuando no se creó el tour
        e: Cuando no se creó el tour

    Returns:
        bool: True si se creó el tour, False si no se creó
    """    
    try:
 
        res =  DSNewTour(input)
        if len(res) > 0:
            new_tours = res['cursor'].fetchall()
            if len(new_tours) > 0:
                id = new_tours[0][0]
                session=res['session']
                return id,session
            raise Exception('No se creó el tour, pruebe los datos ingresados')
        raise Exception(605, 'Error de Creación de Tour')
    except Exception as e:
        raise e
