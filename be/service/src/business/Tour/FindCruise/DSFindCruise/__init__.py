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


def DSFindCruise(input):
    """_summary_

    Args:
        input (_type_): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
        cruise_id = getValue(input, "cruise_id")
        cruise_name = getValue(input, "cruise_name")
        table = "cruise"
        table2 = "cruise_detail"
        schema = "entities"
        stm = " SELECT t.*, json_agg(td.*) as cabins "
        stm += f" FROM {schema}.{table} t, {schema}.{table2} td "
        stm += f" WHERE t.cruise_id = td.cruise_id "
        if cruise_id is not None and cruise_id != 0 and cruise_id != 999:
            stm += f" AND td.cruise_id='{cruise_id}'"
        if cruise_name is not None and cruise_name != "":
            stm += f" AND upper(t.cruise_name) like upper('{cruise_name}')"
        stm += "  GROUP BY t.cruise_id "
        stm += "  ORDER BY t.cruise_id DESC"
        res = nbd.persistence.getQuery(stm, table)
        return res

    except Exception as e:
        raise e
