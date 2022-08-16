try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.infra.web.app.routes import app
import json

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSNewMatch(id, match):
    """Método para procesar match de tour

    Args:
        id (int): Identificador de la Cotización
        match (list): Lista de Match

    Raises:
        e: Exception

    Returns:
        res: Resultado de la Cotización
    """
    try:
        match = json.dumps(match)
        table = "TOUR"
        schema = "entities"
        stm = " UPDATE " + schema + "." + str(table).lower()
        stm += " SET match='{}'".format(match)
        stm += ", tour_state_id=3"
        where = " WHERE tour_id = '{}'".format(id)
        stm += " " + where
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
