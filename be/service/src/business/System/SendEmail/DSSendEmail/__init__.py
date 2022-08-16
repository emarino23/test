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


def DSSendEmail(email, type):
    """Método para enviar email.

    Args:
        data (dict): Diccionario com los datos del email.
        type (str, optional): Tipo de servicio a ser utilizado. Defaults to 'naver'.

    Returns:
        parentdb: Objeto de la clase NaverDB.
    """
    try:
        state = (lambda x: 6 if (x == "buycredits") else 1)(type)
        parentdb = []
        stm = """UPDATE entities.user
                    SET STATE = {}, CONFIRMATION = django.uuid_generate_v1()
                    WHERE EMAIL = \'{}\'
                    """.format(
            state, email
        )

        table = "USER"
        res = nbd.persistence.setWrite(stm, table)
        if len(res) > 0:
            res["session"].commit()
            parentdb.append(res["session"])

            stm = """SELECT * from entities.user 
                        WHERE EMAIL = \'{}\'
                        """.format(
                email
            )

            table = "USER"
            res = nbd.persistence.getQuery(stm, table)
            parentdb.append(res)
            return parentdb
    except Exception as e:
        raise e
