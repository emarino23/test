try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)

from src.business.Dto import TourDto
from src.infra.web.app.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSTourEdit(input):
    """Método para validar una cotizacion

    Args:
        input (dict): Diccionario con los datos de la cotizacion

    Raises:
        e: Error de conexion con la base de datos

    Returns:
        res: Resultado de la operacion
    """
    try:
        data = dict(yaml.safe_load(input.get("data")))
        tour = TourDto(data).__dict__()
        return True if tour.get("tour_id") is None or "NULL" or "" else False
    except Exception as e:
        print("DsTourEdit: "+e)
        return True
