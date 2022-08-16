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


def DSFindHotel(input):
    """_summary_

    Args:
        input (_type_): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
        id = getValue(input, "id")
        table = "catalog_detail"
        schema = "entities"
        stm = "SELECT * FROM"
        stm += f" {schema}.{table}"
        stm += f" WHERE catalog_id = '24'"
        if(id>0):
            stm += f" AND code = '{id}'"
        res = nbd.persistence.getQuery(stm, table)
        return res

    except Exception as e:
        raise e
