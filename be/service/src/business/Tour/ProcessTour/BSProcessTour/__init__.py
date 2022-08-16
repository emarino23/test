try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
from ..DSProcessTour import DSProcessTour
from ...NewMatch import BSNewMatch
from ...ProcessDestinations import BSProcessDestinations
from ...ProcessDays import BSProcessDays
from ...FindTour import BSFindTour
from src.business.System.GetNextVal import BSGetNextVal
from src.business.System.EditVideo import BSEditVideo
from src.infra.docs.merger import DocGenerator
from naver_core import *


def finalProccess(data, tour_id):
    processed = DSProcessTour(tour_id)
    if len(processed) > 0:
        processed["session"].commit()
        doc_generator = DocGenerator(data)
        doc_generator.gen_tour_doc()
        # tour = BSFindTour(
        #     {"data": {"tour_id": tour_id}})[0]
        video = {
            "state": "create",
            "data": {
                "tour_id": tour_id,
                "title": tour_id,
                "description": tour_id,
            }}
        bs = BSEditVideo
        res = bs.BSEditVideo(video)
        return res
    raise Exception(605, "Error de Procesamiento de tour")


def BSProcessTour(tour_id, session, input):
    """Método de Procesamiento Tour

    Args:
        tour_id (int): Identificador de Tour
        input (dict): Diccionario con los datos de Tour

    Raises:
        Exception: Cuando no se puede procesar Tour
        Exception: Cuando no se puede procesar los destinos
        Exception: Cuando no se puede procesar los días
        Exception: Cuando no se puede crear el Match
        e: Todas las expeciones

    Returns:
        bool: [description]
    """
    try:
        data = dict(yaml.safe_load(input.get("data")))
        destinations = data.get("destinations")
        keys = list(destinations)
        first = keys[0]
        keyActivities = destinations[first]["key_activities"]
        tour = data.get("tour")
        purposes = tour.get("purposes")
        match = [purposes, keyActivities]
        if match is not None:
            session.commit()
            if destinations is not None:
                res_match = BSNewMatch(tour_id, match)
                if len(res_match) > 0:
                    res_match["session"].commit()
                    res_destinations = BSProcessDestinations(
                        tour_id, input
                    )
                    if len(res_destinations) > 0:
                        index = 0
                        destination_indexes = []
                        for res_destination in res_destinations:
                            res_destination["session"].commit()
                            last_row_id = (
                                BSGetNextVal(
                                    "TOUR_DETAIL", "tour_detail_id"
                                )
                                + index
                            )
                            if index > 0:
                                destination_indexes.append(last_row_id)
                            index += 1
                        for destination in destinations:
                            destination = destinations[destination]
                            destination_index = destination_indexes[0]
                            destination["tour_detail_id"] = destination_index
                            days = BSProcessDays(tour_id, destination)
                            if days is False:
                                raise Exception(
                                    605, "Error de Procesamiento de días")
                    return finalProccess(data, tour_id)
                raise Exception(605, "Error de Procesamiento de match")
            raise Exception(605, "No tiene destinos el tour")
        raise Exception(605, "No tiene match el tour")
    except Exception as e:
        raise e
