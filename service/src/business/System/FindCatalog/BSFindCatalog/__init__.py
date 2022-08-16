try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSFindCatalog import DSFindCatalog
from ..DSFindTableCatalog import DSFindTableCatalog
from naver_core import *
from src.business.Dto import CatalogDetailDto
from naver_db import NaverDB
from naver_config import NaverConfig
from src.infra.web.app.routes import app
import ast

config = NaverConfig(app)
ndb = NaverDB(app, config)

def BSFindCatalog(input):
    try:
        redis_response = ndb.persistence.redis.get(str(input))
        if redis_response is not None:
            query = redis_response.decode()
            res = ast.literal_eval(query)
            return res
        results = DSFindCatalog(input)
        
        if(isinstance(input, dict)):
            catalog_list = {"catalogs": {}}
            catalogs = getValue(input, 'catalogs')
            for catalog in catalogs:
                for result in results:
                    if result["catalog"] == catalog or catalog == "ALL":
                        catalogDto = CatalogDetailDto(result)
                        if catalogDto.catalog not in list(catalog_list["catalogs"]):
                            catalog_list["catalogs"][catalogDto.catalog] = []
                        catalog_list["catalogs"][catalogDto.catalog].append(
                            catalogDto.__dict__())

            tables = getValue(input, 'tables')
            if tables is not None:
                for table in tables:
                    name = table.get('name')
                    result = DSFindTableCatalog(table)
                    # catalogDto = CatalogDetailDto(result)
                    catalog_list["catalogs"][name] = (result)
                pass
            ndb.persistence.redis.set(str(input),str(catalog_list))
            return catalog_list
        catalogs = {}
        for result in results:
            catalog = result.get('catalog')
            exists = catalogs.get(catalog)
            if exists is not None:
                if(not isinstance(catalogs[catalog], list)):
                    catalogs[catalog] = list()
            else:
                catalogs[catalog] = list()
            catalogs[catalog].append(result)
        output = {"catalogs": catalogs}
        ndb.persistence.redis.set(str(input),str(output))
        return output
    except Exception as e:
        raise e
