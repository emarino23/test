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


def DSUpdatePlaylist(playlist):

    try:
        playlist_slug = playlist.get('playlist_slug')
        tour_id = playlist.get('tour_id')
        schema = "entities"
        table = "tour"
        stm = f" update {schema}.{table}"
        stm += f" set playlist_slug = '{playlist_slug}'"
        stm += f" where tour_id = '{tour_id}'"
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
