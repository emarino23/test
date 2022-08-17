try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)

from src.infra.db import nbd

def DSGetMascota(id):

    try:
        table = "mascota"
        schema = "entities"        
        stm = f"""
             SELECT * FROM {schema}.{table} 
             WHERE  mascota_id = {id}
                             
                    
        """
        res = nbd.persistence.getQuery(stm, table)

        return res
    except Exception as e:
        raise e
