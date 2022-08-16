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


def DSForgot(password, confirmation):
    """Método para recuperar la contraseña

    Args:
        password (str):     Contraseña nueva
        confirmation (str): Confirmación de la contraseña nueva

    Raises:
        e: Error de contraseña

    Returns:
        res: Resultado de la operación
    """
    try:
        stm = """ UPDATE USER
                    SET PASSWORD = \'{0}\', CONFIRMATION = django.uuid_generate_v1()
                    WHERE CONFIRMATION = \'{1}\' """.format(
            password, confirmation
        )

        table = "USER"
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
