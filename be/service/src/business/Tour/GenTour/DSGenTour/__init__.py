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


def DSGenTour(input):
    """_summary_

    Args:
        input (_type_): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
        tour_id = getValue(input, "tour_id")
        table = "TOUR"
        schema = "entities"
        stm = " SELECT  t.detail as detail"
        stm += f" FROM {schema}.{table} t"
        stm += f" JOIN {schema}.client c  "
        stm += "  ON t.client_id = c.client_dni"

        if tour_id != 0:
            stm += f" WHERE tour_id='{tour_id}'"

        stm += "  ORDER BY t.created DESC"
        res = nbd.persistence.getQuery(stm, table)
        return res

    except Exception as e:
        raise e
