try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListReportDetail import FSListReportDetail
from .BSListReportDetail import BSListReportDetail
from .DSListReportDetail import DSListReportDetail


class ListReportDetail():
    def __init__(self):
        self.FSListReportDetail = FSListReportDetail
        self.BSListReportDetail = BSListReportDetail
        self.DSListReportDetail = DSListReportDetail