try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSUpdatePlaylist import BSUpdatePlaylist
from naver_core import *
from flask import render_template, make_response


def FSUpdatePlaylist(input):
    """Método para actualizar playlist.

    Args:
        input (dict): Diccionario con los datos del playlist.

    Returns:
        json: Resultado del API.
    """
    try:
        result = BSUpdatePlaylist(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)
