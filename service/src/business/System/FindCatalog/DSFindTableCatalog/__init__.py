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


def DSFindTableCatalog(input, schema="entities"):

    try:
        table = input.get("name")
        code = input.get("code")
        description = input.get("description")
        stm = """
             SELECT DISTINCT {0} "order", {0} code,{1} description FROM {2}.{3}
             group by code, description                               
        """.format(
            code, description, schema, table
        )
        res = nbd.persistence.getQuery(stm, table)

        return res
    except Exception as e:
        raise e
