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


def DSQuery(input):
    try:
        table = getValue(input, "table")
        name = table.get("name")
        pk = table.get("pk") or name + "_id"
        id = table.get("id")
        where = "where {0} = '{1}'".format(pk, id)
        if id == "ALL":
            where = ""
        table = str(name).upper()
        stm = "select * from entities.{} {}".format(name, where)
        res = nbd.persistence.getQuery(stm, table)
        return res
    except Exception as e:
        raise e
