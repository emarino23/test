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


def DSNewTour(input):
    """_summary_

    Args:
        input (_type_): _description_

    Raises:
        e: _description_

    Returns:
        _type_: _description_
    """
    try:
        data = input.get("data")
        state = input.get("state")
        yaml_object = dict(yaml.safe_load(data))
        tour = TourDto(yaml_object)
        table = "TOUR"
        schema = "entities" 
        if state == "new":
            res = nbd.persistence.insertDto(tour, table, schema)
        else:
            res = nbd.persistence.updateDto(tour, table, "tour_id", schema)
        return res

    except Exception as e:
        raise e
