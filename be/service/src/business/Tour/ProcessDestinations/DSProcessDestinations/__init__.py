try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)

import yaml
from src.business.System.GetNextVal import BSGetNextVal
from src.business.System.FindCatalog import BSFindCatalog
from src.business.Dto.tour import TourDto
from src.business.Dto import DestinationListDto
from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.infra.web.app.routes import app
import ast
import json

config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSProcessDestinations(tour_id, input):

    try:
        reslist = []
        data = dict(yaml.safe_load(input.get("data")))
        tour = TourDto(data).__dict__()
        destinations = dict(yaml.safe_load(tour["destinations"])).values()
        # jsondata = prepareJsonData(destinations)
        destinations = AnyListDto(destinations).__dict__["children"]
        destinationsToInsert = str(json.dumps(destinations))
        table = "TOUR"
        schema = "entities"
        next = nbd.persistence.getNextVal("tour_id", table, schema)
        if int(tour_id) < int(next):
            stm = " UPDATE " + schema + "." + table
            stm += " SET destinations='{}'".format(destinationsToInsert)
            stm += ", tour_state_id=4"
            where = " WHERE tour_id = '{}'".format(tour_id)
            stm += " " + where
            res = nbd.persistence.setWrite(stm, table)
            if len(res) > 0:
                reslist.append(res)

                table = "TOUR_DETAIL"
                destination_catalog = BSFindCatalog({
                    "data": {

                        "catalogs": ["destinations"]

                    }
                })
                destination_catalog = destination_catalog["catalogs"]["destinations"]
                index = 0
                for destination in destinations:
                    dest_code = [
                        x for x in destination_catalog if str(x["description"]).lower() == str(destination["destination"]).lower()]
                    dest_code = dest_code[0]["code"]
                    exp_days = destination["explorationDay"]

                    tour_detail_id = BSGetNextVal(
                        "TOUR_DETAIL", "tour_detail_id"
                    )+index
                    destination["tour_detail_id"] = tour_detail_id
                    dest_index = index
                    stm = f"""
                                INSERT INTO {schema}.{table}(TOUR_DETAIL_ID, TOUR_ID, DETAIL, DESTINATION_ID, EXPLORATION_DAYS, DESTINATION_INDEX)
                                VALUES ({tour_detail_id},{tour_id},\'{str(json.dumps(destination))}\',{dest_code},{exp_days},{dest_index})
                    """
                    res = nbd.persistence.setWrite(stm, table)
                    if len(res) > 0:
                        reslist.append(res)
                    index += 1
        return reslist
    except Exception as e:
        raise e
