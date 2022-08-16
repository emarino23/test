try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSForgot import BSForgot
from naver_core import *

def FSForgot(input):
    """Método para recuperar contraseña

    Args:
        input (dict): Diccionario con los datos de entrada.
        
    Returns:
        json: Mensaje de respuesta en formato json.
    """    
    try:
        password = input.get('password')
        confirmation = input.get('confirmation')
        result = BSForgot(password, confirmation)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e) 