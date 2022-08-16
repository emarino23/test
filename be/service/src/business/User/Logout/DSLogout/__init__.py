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


def DSLogout(username):
    """Método de persistencia para desconectar usuario

    0.- NEW: El usuario es nuevo, no se ha registrado en la base de datos
    1.- UNCONFIRMED: El usuario esta en la base de datos pero no ha confirmado su cuenta
    2.- REGISTERED: El usuario esta en la base de datos y ha confirmado su cuenta
    3.- FORGOT: El usuario esta en la base de datos pero ha olvidado su contraseña
    4.- BLOCK: El usuario esta en la base de datos pero ha sido bloqueado
    5.- DISCONNECTED: El usuario esta en la base de datos y ha cerrado sesion
    6.- CONNECTED: El usuario esta en la base de datos y ha iniciado sesion

    Args:
        username (str): identificador de usuario

    Raises:
        e: Error de conexión a base de datos

    Returns:
        dict: respuesta de conexión a base de datos
    """
    try:
        table = "USER"
        schema = "entities"
        stm = ""
        stm += f" UPDATE {schema}.{table}"
        stm += " SET STATE = 5"
        stm += f" WHERE username = '{username}'"
        stm += " AND STATE = 6"
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
