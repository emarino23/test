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


def DSSignIn(username):
    """Método para iniciar sesión en el sistema
    0.- NEW: El usuario es nuevo, no se ha registrado en la base de datos
    1.- UNCONFIRMED: El usuario esta en la base de datos pero no ha confirmado su cuenta
    2.- REGISTERED: El usuario esta en la base de datos y ha confirmado su cuenta
    3.- FORGOT: El usuario esta en la base de datos pero ha olvidado su contraseña
    4.- BLOCK: El usuario esta en la base de datos pero ha sido bloqueado
    5.- DISCONNECTED: El usuario esta en la base de datos y ha cerrado sesion
    6.- CONNECTED: El usuario esta en la base de datos y ha iniciado sesion

    Args:
        username (str): Nombre de usuario

    Raises:
        e: Error de conexión a la base de datos

    Returns:
        [lst]: Lista con los datos del usuario
    """
    try:
        table = "USER"
        schema = "entities"
        stm = "  SELECT * "
        stm += f" FROM {schema}.{table} "
        stm += f" WHERE USERNAME = '{username}' "
        stm += "  AND  (STATE = 5  OR STATE = 2 ) \n"
        user = nbd.persistence.getQuery(stm, table)
        if len(user) > 0:
            stm = f" UPDATE {schema}.{table} \n"
            stm += "  SET STATE = 6  "
            stm += f" WHERE USERNAME = '{username}' "
            res = nbd.persistence.setWrite(stm, table)
            if len(res) > 0:
                res["session"].commit()
                return user
        raise Exception("User Connected")
    except Exception as e:
        raise e
