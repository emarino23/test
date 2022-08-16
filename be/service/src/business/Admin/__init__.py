from .EditReport import EditReport
from .CreateReport import CreateReport
from .ListReportDetail import ListReportDetail
from .ListAllReport import ListAllReport
from .EditUser import EditUser
from .CreateUser import CreateUser
from .ListUserDetail import ListUserDetail
from .ListAllUser import ListAllUser
from .DeleteUser import DeleteUser
from .DeleteReport import DeleteReport
from .CreateCatalog import CreateCatalog
from .DeleteTour import DeleteTour
from .DeleteSupplier import DeleteSupplier

try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class Admin():
    def __init__(self):
        self.DeleteSupplier = DeleteSupplier()
        self.DeleteTour = DeleteTour()
        self.CreateCatalog = CreateCatalog()
        self.DeleteReport = DeleteReport()
        self.DeleteUser = DeleteUser()
        self.ListAllUser = ListAllUser()
        self.ListUserDetail = ListUserDetail()
        self.CreateUser = CreateUser()
        self.EditUser = EditUser()
        self.ListAllReport = ListAllReport()
        self.ListReportDetail = ListReportDetail()
        self.CreateReport = CreateReport()
        self.EditReport = EditReport()
        self.attributes={self.admin_type: None , self.props: None , self.admin_id: None }
