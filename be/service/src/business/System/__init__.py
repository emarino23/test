from .LogBlocked import LogBlocked
from .BlockUser import BlockUser
from .LoadTemplate import LoadTemplate
from .GetNextVal import GetNextVal
from .FindCatalog import FindCatalog
from .ProcessOptions import ProcessOptions
from .LogNotification import LogNotification
from .SendNotification import SendNotification
from .LogAlert import LogAlert
from .SendAlert import SendAlert
from .LogEmail import LogEmail
from .SendEmail import SendEmail
from .LogSms import LogSms
from .SendSms import SendSms
from .LogProblem import LogProblem
from .ValidateProblem import ValidateProblem
from .LogProduct import LogProduct
from .ValidateProduct import ValidateProduct
from .LogService import LogService
from .ValidateService import ValidateService
from .LogActivity import LogActivity
from .ValidateActivity import ValidateActivity
from .LogDestiny import LogDestiny
from .ValidateDestiny import ValidateDestiny
from .LogExperience import LogExperience
from .ValidateExperience import ValidateExperience
from .LogTour import LogTour
from .ValidateTour import ValidateTour
from .LogClient import LogClient
from .ValidateClient import ValidateClient
from .LogProspect import LogProspect
from .ValidateProspect import ValidateProspect
from .LogContact import LogContact
from .ValidateContact import ValidateContact
from .LogConsumption import LogConsumption
from .ValidateConsumption import ValidateConsumption
from .LogPay import LogPay
from .ValidatePay import ValidatePay
from .LogSale import LogSale
from .ValidateSale import ValidateSale
from .LogTour import LogTour
from .ValidateTour import ValidateTour
from .LogOpportunity import LogOpportunity
from .ValidateOpportunity import ValidateOpportunity
from .LogUser import LogUser
from .ValidateUser import ValidateUser
from .LogPoll import LogPoll
from .ValidatePoll import ValidatePoll 
from .LogConnection import LogConnection
from .EditVideo import EditVideo

try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
class System():
    def __init__(self):
        self.ValidatePoll = ValidatePoll()
        self.LogPoll = LogPoll()
        self.ValidateUser = ValidateUser()
        self.LogUser = LogUser()
        self.ValidateOpportunity = ValidateOpportunity()
        self.LogOpportunity = LogOpportunity()
        self.ValidateTour = ValidateTour()
        self.LogTour = LogTour()
        self.ValidateSale = ValidateSale()
        self.LogSale = LogSale()
        self.ValidatePay = ValidatePay()
        self.LogPay = LogPay()
        self.ValidateConsumption = ValidateConsumption()
        self.LogConsumption = LogConsumption()
        self.ValidateContact = ValidateContact()
        self.LogContact = LogContact()
        self.ValidateProspect = ValidateProspect()
        self.LogProspect = LogProspect()
        self.ValidateClient = ValidateClient()
        self.LogClient = LogClient()
        self.ValidateTour = ValidateTour()
        self.LogTour = LogTour()
        self.ValidateExperience = ValidateExperience()
        self.LogExperience = LogExperience()
        self.ValidateDestiny = ValidateDestiny()
        self.LogDestiny = LogDestiny()
        self.ValidateActivity = ValidateActivity()
        self.LogActivity = LogActivity()
        self.ValidateService = ValidateService()
        self.LogService = LogService()
        self.ValidateProduct = ValidateProduct()
        self.LogProduct = LogProduct()
        self.ValidateProblem = ValidateProblem() 
        self.LogProblem = LogProblem()
        self.SendSms = SendSms()
        self.LogSms = LogSms()
        self.SendEmail = SendEmail()
        self.LogEmail = LogEmail()
        self.SendAlert = SendAlert()
        self.LogAlert = LogAlert()
        self.SendNotification = SendNotification()
        self.LogConnection = LogConnection()
        self.LogNotification = LogNotification()
        self.LoadTemplate = LoadTemplate()
        self.GetNextVal = GetNextVal()
        self.FindCatalog = FindCatalog()
        self.ProcessOptions = ProcessOptions()
        self.BlockUser = BlockUser()
        self.LogBlocked = LogBlocked()
        self.EditVideo = EditVideo()
        self.attributes={self.props: None }
