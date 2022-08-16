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


def DSCreateMascota(data):

    try:
        id = data.get("mascota_id")
        name = data.get("name")
        age = data.get("age")
        gender = data.get("gender")
        nickname = data.get("nickname")
        location = data.get("location")
        table = "mascota"
        schema = "entities" 
        if(id == 0):
            stm = f"""
                INSERT INTO entities.mascota( "name", age, gender, nickname, "location")
                VALUES( \'{name}\', {age}, \'{gender}\', \'{nickname}\', \'{location}\')
            """
        else:
            stm = f"""
               UPDATE entities.mascota
SET "name"=\'{name}\', age={age}, gender=\'{gender}\', nickname=\'{nickname}\', "location"=\'{location}\'
WHERE mascota_id={id};
            """
            
        res = nbd.persistence.setWrite(stm, table)

        return res
    except Exception as e:
        raise e
