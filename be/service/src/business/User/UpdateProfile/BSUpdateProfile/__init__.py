try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSUpdateProfile import DSUpdateProfile
from naver_core import *


def BSUpdateProfile(input):
    """Método para atualizar perfil de usuario.

    Args:
        input (dict): Diccionario de datos de entrada.

    Raises:
        e: Excepción.

    Returns:
        boolean: True si se actualizó el perfil de usuario, Raise en caso contrario.
    """    
    try:
        identification=getValue(input, 'identification')
        avatar=getValue(input, 'avatar')
        password=getValue(input, 'password')
        nickname=getValue(input, 'nickname')
        result = DSUpdateProfile(identification=identification, avatar=avatar, password=password, nickname=nickname)
        if len(result) > 0:
            result['session'].commit()
            return True
        raise Exception(621,'No se pudo actualizar el perfil')

    except Exception as e:
        raise e
