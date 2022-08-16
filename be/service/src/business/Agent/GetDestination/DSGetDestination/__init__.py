try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
from src.business.Dto import ClientDto
from src.infra.web.app.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSGetDestination(destination, type):
    try:
        table = "DESTINATION"
        schema = "entities"
        stm = f"select * from {schema}.{table}"
        stm += f" where destination_name = upper('{destination}')"
        res = nbd.persistence.getQuery(stm, table)
        return res[type]
    except Exception as e:
        raise e


def DSGetDestination(input):
    try:
        destination_id = getValue(input, "destination_id")
        destination_name = getValue(input, "destination_name")
        destination_id_stm = f" where destination_id = '{destination_id}'"
        destination_name_stm = f" where destination_name = upper('{destination_name}')"
        where = ""
        if destination_id == None and destination_name == None:
            return None
        if destination_id != "ALL" and destination_id != "" and destination_id != None:
            where += destination_id_stm
        if (
            destination_name != "ALL"
            and destination_name != ""
            and destination_name != None
        ):
            where += destination_name_stm
        table = "DESTINATION"
        select = "select * from entities.destination"
        stm = select + where
        res = nbd.persistence.getQuery(stm, table)
        return res
    except Exception as e:
        raise e
