from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    gender = models.CharField(max_length=100,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    contact = models.CharField(max_length=100,blank=True,null=True) 
    status = models.CharField(max_length=100,blank=True)
    is_admin = models.BooleanField(default=False)


