from waitress import serve
import os
from naver_core import *
any_module(__file__, 3)
from werkzeug.serving import WSGIRequestHandler
WSGIRequestHandler.protocol_version = "HTTP/1.1"
from src.infra  import app
PORT = int(os.environ.get('SERVER_PORT', '5555'))
HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
SERVER = os.environ.get('SERVER', '0.0.0.0')
# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# CERT_DIR = os.path.join(FILE_DIR, "certificate.crt")
# KEY_DIR = os.path.join(FILE_DIR, "private.key")
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
print(f"RUNNING SERVER ON HOST {SERVER}")
serve(app, host=HOST, port=PORT, threads=100)  # WAITRESS!
#CREATED BY JACR6