"""deps module."""
try:
    
    from flask_restx import Resource, reqparse
    from flask import request, render_template, make_response
    from flask import flash,  redirect
    from werkzeug.utils import secure_filename
    from naver_core import *
    from flask_restx import Api, fields
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from flask_cors import CORS
    from naver_config import NaverConfig
    from naver_core import *
    from dotenv import load_dotenv
    from pathlib import Path
    from werkzeug.serving import WSGIRequestHandler
    from .constants import *
    from .utils import *
    from .core import *
    from .recoveryform import *
except Exception as e:
    print(e)
    pass
