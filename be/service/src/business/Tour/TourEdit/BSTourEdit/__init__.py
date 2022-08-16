try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
from src.business.Dto.tour import TourDto
from ..DSTourEdit import DSTourEdit
from naver_core import *
from ... import NewTour, ProcessTour, UpdateTour, CalculateNetRate


def BSTourEdit(input):
    """Método que se encarga de ejecutar el comando edit.

    Args:
        input (dict): usuario de entrada

    Raises:
        Exception:  Error de validación de usuario

    Returns:
        boolean: True si el usuario se confirma, False si no
    """
    try:
        state = input.get("state")
        if state == "new" or state == "update":
            valid = DSTourEdit(input)
            if valid:
                tour_id, session = NewTour().BSNewTour(input)
                if tour_id is not None:
                    res =  ProcessTour().BSProcessTour(tour_id, session, input)
                    return res
                raise Exception("Error al crear el tour")
            raise Exception("Ya tiene un tour activo")
        if state == "calculate":
            return CalculateNetRate.BSCalculateNetRate(input)
        raise Exception(605, "Error de Edición")
    except Exception as e:
        raise e
