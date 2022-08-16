try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.infra.web.app.routes import app
from src.infra.video.youtube import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSPlayTour(tour_id):
    """Método para reproducir una lista de videos del Tour.

    Args:
        tour_id (str): travel_code del Tour.

    Returns:
        res: Resultado de la operación.
    """
    try:
        table = "TOUR"
        schema = "entities"

        stm = "SELECT "
        stm += f" * FROM {schema}.{table}"
        if tour_id == 'null':
            tour_id = 0
        stm += f" WHERE tour_id = '{tour_id}'"

        tour = nbd.persistence.getQuery(stm, table)
        if len(tour) > 0:
            reproductions = tour[0]["reproductions"]
            if reproductions > 0:
                stm = "UPDATE "
                stm += f" {schema}.{table}"
                stm += f" SET reproductions={reproductions-1}"
                stm += f" WHERE tour_id = '{tour_id}'"
                update = nbd.persistence.setWrite(stm, table)
                if len(update) > 0:
                    update["session"].commit()
            else:
                return ErrorResponse("No hay videos para reproducir")
        return tour[0]["playlist_slug"]

    except Exception as e:
        raise e
