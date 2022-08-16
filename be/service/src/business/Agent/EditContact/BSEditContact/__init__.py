try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSEditContact import DSEditContact 

def BSEditContact(input):
    try:
        res = DSEditContact(input)
        if len(res) > 0:
            res.get('session').commit()
            return True
            
        raise Exception(605, 'Error de Edición')

    except Exception as e:
        raise e