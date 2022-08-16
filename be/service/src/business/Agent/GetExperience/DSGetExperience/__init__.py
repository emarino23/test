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


def DSGetExperience(input):
    try:
        table = "EXPERIENCE"
        (
            destination,
            experience,
            key_activities,
            travel_rhtythms,
            destination_option,
        ) = input.get("data").values()
        if isinstance(destination, str) and destination != "":
            destination = [destination]
        if isinstance(destination, list) and len(destination) == 0:
            destination = None

        if isinstance(experience, str) and experience != "":
            experience = [experience]
        if isinstance(experience, list) and len(experience) == 0:
            experience = None

        stm_ka = ""
        if len(key_activities) > 0:
            stm_ka = f" and (e.key_activity_id   ) in {str(tuple(key_activities)).replace(',)',')')}"
            stm_ka += f" and (e.key_activity2_id   ) in {str(tuple(key_activities)).replace(',)',')')}"
        stm_tr = ""
        if len(travel_rhtythms) > 0:
            stm_tr = f" and (e.travel_ritm_id ) in {str(tuple(travel_rhtythms)).replace(',)',')')}"
        stm_to = ""
        if destination_option != None:
            stm_to = f" and (e.destination_option_id ) ='{destination_option}'"
        stm_dest = ""
        if destination != None:
            stm_dest = f" and (d.destination_title in {str(tuple(destination)).replace(',)',')').upper()} "
        stm_exp = ""
        if experience != None:
            stm_exp = f" and e.experience_title like upper('%{experience}%')) "

        order = """ order by e."order" """
        select = "select distinct"
        columns = """
        
                d.destination_title destination, 
                e.experience_title title, e.experience_photo image, 
                e.experience_video_photo galleryimage, e.experience_video video, 
                e."order", e.description description, e.experience_next as next,
                (e.props)::jsonb    props 
        
        """
        body = """
                    from entities.experience e 
                        join entities.destination d 
                            on e.destination_id =d.destination_id 
                            where true
        """
        stm = (
            select
            + columns
            + body
            + stm_ka
            + stm_tr
            + stm_to
            + stm_dest
            + stm_exp
            + order
        )
        res = nbd.persistence.getQuery(stm, table)
        return res
    except Exception as e:
        raise e
