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


def DSValidatePassword(username, password):
    try:
        table = "USER"
        pp = ""
        stm = """ SELECT * FROM entities.user WHERE USERNAME = \'{0}\'
        
        """.format(
            username
        )

        user = nbd.persistence.getQuery(stm, table)
        if len(user) > 0:
            pp = str(user[0]["password"]).strip()
        else:
            raise Exception("No Existe usuario")

        stm = """ SELECT CAST(django.DIGEST(\'{0}\','SHA256') AS BPCHAR) = \'{1}\' as VALID
                
        """.format(
            password, pp
        )

        res = nbd.persistence.getQuery(stm, table)
        return res

    except Exception as e:
        raise e
