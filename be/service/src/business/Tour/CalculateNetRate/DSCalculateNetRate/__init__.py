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


def DSCalculateNetRate(input):
    try:
        table = "TOUR"
        schema = "entities"
        stm = " SELECT * from "
        stm += schema + "." + table
        res = nbd.persistence.getQuery(stm, table)
        return res

    except Exception as e:
        raise e
