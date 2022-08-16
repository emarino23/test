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


def DSProcessOptions(tour_id):
    """Método para procesar opciones de inclusión

    Args:
        input (dict): Entrada del método

    Raises:
        e: error del proceso

    Returns:
        res: resultadod de la operación
    """
    try:
        table = "CATALOG"
        stm = """
                select  entities.sp_options({});
        """.format(
            tour_id
        )
        res = nbd.persistence.getQuery(stm, table)[0]["sp_options"]
        return res

    except Exception as e:
        raise e
