try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
from src.business.Dto import ClientDto
from src.infra.web.app.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSEditContact(input):
    try:
        data = input.get("data")
        client = ClientDto(data)
        print(client.__dict__())
        table = "CLIENT"
        res = nbd.persistence.updateDto(client, table, "dni")
        return res

    except Exception as e:
        raise e
