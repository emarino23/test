try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..DSCreateContact import DSCreateContact
from naver_core import *


def BSCreateContact(input):
    try:
        res = DSCreateContact(input)
        if len(res) > 0:
            res.get('session').commit()
            return True
        raise Exception(630, 'No data to insert')

    except Exception as e:
        raise e
