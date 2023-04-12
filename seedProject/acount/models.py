from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_general = models.BooleanField(null=True ,default=True)
    is_active = models.BooleanField(null=True ,default=False)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)