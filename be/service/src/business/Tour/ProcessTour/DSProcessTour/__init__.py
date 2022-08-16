try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.infra.web.app.routes import app


config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSProcessTour(id):
    """Método para validar si existe un tour

    Args:
        id (int): id de el tour

    Raises:
        e: Error de conexión a la base de datos

    Returns:
        res: Resultado de la consulta
    """
    try:
        table = "TOUR"
        schema = "entities"
        stm = " UPDATE "
        stm += schema + "." + table
        stm += " SET TOUR_STATE_ID = 2 "
        stm += " WHERE tour_id = '{}'".format(id)
        stm += " AND tour_state_id >= 1"
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
