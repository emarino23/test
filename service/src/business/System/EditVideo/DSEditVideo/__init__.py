try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
from src.infra.web.app.routes import app
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *

config = NaverConfig(app)
nbd = NaverDB(app, config)


def request_resource(resource):
    try:
        table = "CATALOG_DETAIL"
        schema = "entities"
        resource_name = resource[0]
        resource_type = resource[1]
        stm = f" SELECT relation->'resource_id' as resource_id FROM {schema}.{table} cd"
        stm += f" WHERE "
        stm += f" cd.catalog_id = '{resource_type}'"
        stm += f" AND upper(cd.description) = upper('{resource_name}')"
        res = nbd.persistence.getQuery(stm, table)[0]['resource_id']
        return res
    except Exception as e:
        raise e


def DSEditVideo(input):
    try:
        table = "TOUR"
        schema = "entities"
        tour_id = getValue(input, 'tour_id')
        stm = f" SELECT DESTINATIONS FROM {schema}.{table}"
        stm += f" WHERE "
        stm += f" tour_id = '{tour_id}'"
        destinations = nbd.persistence.getQuery(stm, table)
        if len(destinations) > 0:
            destinations = destinations[0]["destinations"]
            playlist_request = []
            playlist_response = []
            for destination in destinations:
                # destination = destinations[destination]
                dest_name = destination.get('destination')
                playlist_request.append([dest_name, 37])
                try:
                    days = json.loads(destination.get('daysData'))
                except:
                    days = (destination.get('daysData'))
                for day_id in days:
                    day = days[day_id]
                    experiences = day.get('experiences')
                    for experience in experiences:
                        playlist_request.append([experience, 35])
            for resource in playlist_request:
                res = request_resource(resource)
                playlist_response.append(res)
        else:
            raise Exception('No tour found')
        return playlist_response

    except Exception as e:
        raise e
