try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSProcessDays import BSProcessDays
from naver_core import *
from flask import render_template, make_response

def FSProcessDays	(input):
    """Método para crear un nuevo Reporte.

    Args:
        input (dict): Diccionario con los datos del Reporte.

    Returns:
        json: Resultado del API.
    """
    try:
        tour_id = getValue(input, "tour_id")
        destination = getValue(input, "destination")
        result = BSProcessDays(tour_id, destination)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e) 