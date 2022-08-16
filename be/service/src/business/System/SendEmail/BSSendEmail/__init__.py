try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    __path__ = __import__("pkgutil").extend_path(__path__, __name__)
from ..DSSendEmail import DSSendEmail
from naver_core import *
import os


emailtype = dict(
    {
        "confirmation": {
            "template": "confirmation",
            "subject": "CRS: REGISTRO CON CONFIRMACIÓN",
            "server": "http://uiodesign.fortiddns.com:9999/User/Confirm",
            "code": "confirmation",
        },
        "buycredits": {
            "template": "buycredits",
            "subject": "CRS: REGISTRO DE COMPRAS",
            "server": "http://uiodesign.fortiddns.com:9999/User/Confirm",
            "code": "username",
        },
        "forgot": {
            "template": "forgot",
            "subject": "CRS: RECUPERACIÓN DE USUARIO",
            "server": "http://uiodesign.fortiddns.com:9999/User/Forgot",
            "code": "confirmation",
        },
    }
)


def BSSendEmail(input, type):
    """Método de envío de correo electrónico.

    Args:
        input (dict): Diccionario con los datos del usuario.
        type (str): Tipo de correo electrónico a enviar.

    Raises:
        Exception: Error al enviar el correo electrónico.

    Returns:
        bool: True si el correo fue enviado correctamente.
    """
    result = []
    try:
        email = getValue(input, "email")
        result = DSSendEmail(email, type)
        if len(result) > 0:
            data = result[1][0] if len(result[1]) > 0 else {}
            send = EmailSender(data, emailtype.get(type))
            if send:
                result[0].commit()
            return "Se te envió un correo"

    except Exception as e:
        if len(result) > 0:
            result[0].rollback()
        raise e


def EmailSender(data, type):
    """Método para enviar correo electrónico.

    Args:
        data (dict): Diccionario con los datos del usuario.
        type (dict): Tipo de correo electrónico a enviar.

    Raises:
        e: Error al enviar el correo electrónico.

    Returns:
        boolean:  True si el correo fue enviado correctamente.
    """
    try:
        import codecs
        from src.infra.web.app.routes import TEMPLATE_FOLDER

        TEMPLATE = os.path.join(TEMPLATE_FOLDER, type.get("template") + ".html")
        f = codecs.open(TEMPLATE, "r")
        body = f.read()
        body = body.replace("SERVER", type.get("server"))
        body = body.replace("CODE", data.get(type.get("code")))
        f.close()
        email = str(data.get("email")).strip()
        subject = type.get("subject")
        from src.infra.web.app.routes import app
        from naver_net import NaverNet

        Net = NaverNet(app)
        Net.sender.sendmail(email, subject, body)
        return True
    except Exception as e:
        raise e
