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


def DSPromoteTour(tour_id):
    """Método de confirmación de usuario

    Args:
        tour_id (str): Código UUID enviado por correo electrónico para confirmar cuenta de usuario.

    Raises:
        e: Error de conexión a base de datos.

    Returns:
        dict: Diccionario con información de confirmación de usuario.
    """
    try:
        stm = """   UPDATE USER
                    SET tour_state_id = 2
                    WHERE tour_id = \'{}\'
                    AND tour_state_id = 1
                    ;""".format(
            tour_id
        )

        table = "USER"
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
