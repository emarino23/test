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


def DSNewId():
    try:
        table = "TOUR"
        schema = "entities"
        field = "tour_id"
        res = nbd.persistence.getNextVal(field, table, schema)
        return res
    except Exception as e:
        raise e
