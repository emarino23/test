"""utils module."""
from .deps import *
 


def removeBytePrefix(value):
    """Method to remove the byte prefix from the response
    Args:
        value (value): value to be decorated

    Returns:
        value: Replaced value
    """
    return str(value).replace("b'", "").replace("'", "")


def decryptdata():
    data = request.headers.get('token')
    tokendecrypted = decrypt(encrypt(pksalt, pksalt), pksalt)
    salt = removeBytePrefix(tokendecrypted.decode('utf8'))
    jdata = removeBytePrefix(request.get_json(
        force=True)['data']).encode('utf8')
    res = decrypt(jdata, salt).decode('utf8')
    jsondata = ast.literal_eval(jsonConvert(res))
    data = {"data": jsondata}
    return data


def secure_method(func):
    def inner(*args, **kwargs):
        token = request.headers.get('token')
        if token is None:
            return ErrorResponse(MAINTENANCE)
        if token != TOKEN:
            return ErrorResponse(MAINTENANCE)
        returned_value = func(*args, **kwargs)
        return returned_value
    inner.__name__ = func.__name__
    return inner


def encrypted(function):
    """Method decorator to encrypt the response
    Args:
        function (function): Function to be decorated
    Returns:
        function: Decorated function
    """
    def wrapper(data):

        f = function
        res = f(data)
        res['data'] = str(encrypt(str(res['data']), pksalt))
        return res
    return wrapper


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
