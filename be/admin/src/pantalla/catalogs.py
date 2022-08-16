from django.db import models
from django.utils.translation import gettext_lazy as _

class UserType(models.IntegerChoices):
    Admin = 1, _('Admin')
    Agent = 2, _('Agent')
    Experience = 3, _('Experience')
    Travel = 4, _('Travel') 