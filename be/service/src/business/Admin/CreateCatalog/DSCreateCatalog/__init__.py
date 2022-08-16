try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
from src.infra.web.app.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
import json

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSCreateCatalog(input):
    try:
        data = input.get("data")
        update = input.get("update") or False
        relation = input.get("relation") or {}
        catalog_id = data.get("catalog_id")
        order = data.get("order")
        description = data.get("description")
        is_active = data.get("is_active")
        code = data.get("code")
        value = json.dumps(data.get("value")).replace("NaN", '""')
        table = "CATALOG_DETAIL"
        schema = "entities"
        stm = f" INSERT INTO {schema}.{table}"
        stm += f"""(catalog_id,
                    "order",
                    description,
                    is_active,
                    code,
                    value
                    )"""
        stm += f""" VALUES ({catalog_id},{order},'{description}',{is_active},{code},\'{value}\')"""
        if update:
            stm = f" UPDATE {schema}.{table} SET "
            stm += f"description='{description}', "
            stm += f"value='{value}', "
            stm += f"relation='{json.dumps(relation)}' "
            stm += f" WHERE catalog_id={catalog_id} AND " 
            stm += f" code='{code}'"

        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
