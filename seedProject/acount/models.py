from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # is_general = models.BooleanField(default=True, null= True)
    # is_approval = models.BooleanField(default=True, null=False)
    pass
