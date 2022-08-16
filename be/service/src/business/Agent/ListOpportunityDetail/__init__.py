try: 
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)
from .FSListOpportunityDetail import FSListOpportunityDetail
from .BSListOpportunityDetail import BSListOpportunityDetail
from .DSListOpportunityDetail import DSListOpportunityDetail


class ListOpportunityDetail():
    def __init__(self):
        self.FSListOpportunityDetail = FSListOpportunityDetail
        self.BSListOpportunityDetail = BSListOpportunityDetail
        self.DSListOpportunityDetail = DSListOpportunityDetail