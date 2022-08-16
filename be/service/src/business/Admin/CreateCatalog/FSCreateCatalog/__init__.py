try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from ..BSCreateCatalog import BSCreateCatalog
from naver_core import *
import ast, json,re, yaml
def myconverter(o):
    char = str(o)
    return char
def FSCreateCatalog(input):
    try:
        state = input.get("state")
        if state == "tour":
            value = getValue(input, 'value')  
            value = yaml.safe_load(value)
            value = json.dumps(value, default=myconverter)
            value = json.loads(value)
            input["data"]["value"] = value
        result = BSCreateCatalog(input)
        return Ok(result)

    except Exception as e:
        return ErrorResponse(e)