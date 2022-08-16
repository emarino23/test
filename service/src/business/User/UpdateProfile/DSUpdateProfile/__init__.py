try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)

from naver_db import NaverDB
from naver_config import NaverConfig
from naver_core import *
from src.infra.web.app.routes import app


config = NaverConfig(app)
nbd = NaverDB(app, config)


def DSUpdateProfile(
    identification,
    avatar,
    password,
    nickname,
):
    try:

        stm = """ UPDATE GAMER
                    SET 
                         """
        setavatar = " AVATAR = {0}, ".format(
            nbd.persistence.existValue(avatar, "AVATAR")
        )
        setpassword = " PASSWORD = {0}, ".format(
            nbd.persistence.existValue(password, "PASSWORD")
        )
        setnickname = " NICKNAME = {0} ".format(
            nbd.persistence.existValue(nickname, "NICKNAME")
        )
        where = " WHERE IDENTIFICATION = {0} ".format(
            nbd.persistence.existValue(identification, "IDENTIFICATION")
        )

        stm = stm + setavatar + setpassword + setnickname + where

        table = "GAMER"
        res = nbd.persistence.setWrite(stm, table)
        return res

    except Exception as e:
        raise e
