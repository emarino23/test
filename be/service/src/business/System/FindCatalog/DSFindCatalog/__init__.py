try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)

from tkinter import N
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.infra.web.app.routes import app


config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSFindCatalog(input):

    try:
        table = "CATALOG"
        and_stm = ""
        if(isinstance(input, dict)):
            catalogs = str(tuple(input.get("data").get("catalogs"))
                           ).replace(",)", ")")
            and_stm = " and c.description in {} ".format(catalogs)
            if "ALL" in catalogs:
                and_stm = ""
        stm = f"""
             
                        select  distinct
                            (c.description)     as  catalog,
                            (cd."order")        as  order,
                            (cd.description)    as  description,
                            (cd.code)           as  code,
                            (cd.value)          as  value,
                            (cd.relation)          as  relation
             
 
                        from entities.catalog_detail cd 
                            join entities."catalog" c 
                                on c.catalog_id = cd.catalog_id 
                                where true
                            {and_stm}
                            and cd.is_active is true  
                            order by cd."order" asc
                             
                    
        """
        res = nbd.persistence.getQuery(stm, table, False)

        return res
    except Exception as e:
        raise e
