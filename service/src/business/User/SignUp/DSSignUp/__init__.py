try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.infra.web.app.routes import app
from src.business.Dto import UserDto

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSSignUp(data):
    """Método para crear un nuevo Reporte.

    Args:
        data (dict): Diccionario con los datos del Reporte.

    Returns:
        res: Resultado de la operación.
    """
    try:
        user = UserDto(data)
        stm = f"""
        INSERT INTO entities.user
        (identification, username,   lastname, email, phone, state,  created, updated, "password")
        VALUES('{user.identification}', '{user.username}', '{user.lastname}',   '{user.email}', '{user.phone}',  0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '{user.password}')
    
        """
        table = "USER"
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
