try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSClientEdit import BSClientEdit
from naver_core import *
from flask import render_template, make_response

def FSClientEdit	(data):
    """Método para editar un Cliente.

    Args:
        data (dict): Diccionario con los datos del Cliente.

    Returns:
        json: Resultado del API.
    """
    try:
        result = BSClientEdit(data)
        return Ok(result)
    except Exception as e:
        return ErrorResponse(e) 