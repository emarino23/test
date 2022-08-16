# try: 
#     __import__('pkg_resources').declare_namespace(__name__)
# except ImportError:
#     __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSUpdateProfile import FSUpdateProfile
from .BSUpdateProfile import BSUpdateProfile
from .DSUpdateProfile import DSUpdateProfile


class UpdateProfile():
    def __init__(self):
        self.FSUpdateProfile = FSUpdateProfile
        self.BSUpdateProfile = BSUpdateProfile
        self.DSUpdateProfile = DSUpdateProfile