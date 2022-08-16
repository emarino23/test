try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSSendEmail import BSSendEmail
from naver_core import *

def FSSendEmail(data, type='naver'):
    """Método para enviar email.

    Args:
        data (dict): Diccionario com los datos del email.
        type (str, optional): Tipo de servicio a ser utilizado. Defaults to 'naver'.

    Returns:
        json: Retorna el status de envio del email.
    """    
    try:
        result = BSSendEmail(data, type)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e) 