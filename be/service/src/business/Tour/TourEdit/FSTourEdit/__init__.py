try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSTourEdit import BSTourEdit
from naver_core import * 
import json, yaml


def prepareTour(input):
    def myconverter(o):
        char = str(o)
        return char
    value = getValue(input, 'value')  
    value = yaml.safe_load(value)
    value = json.dumps(value, default=myconverter)
    value = json.loads(value)
    input["data"]["value"] = value
    return input
    
def FSTourEdit	(input): 
    """_summary_

    Args:
        input (_type_): _description_

    Returns:
        _type_: _description_
    """
    try: 
            
        result = BSTourEdit(input)
        return Ok(result)
    except Exception as e:
        return ErrorResponse(e) 