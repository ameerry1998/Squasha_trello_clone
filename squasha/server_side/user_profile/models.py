from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User_Profile(AbstractUser):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    #profile_pic = models.ImageField(blank=True, upload_to='profile_pics')
    username = models.CharField(max_length=255, unique=True,
    validators=[RegexValidator(r'^[a-zA-Z0-9_\.]*$', 'Only alphanumeric characters, underscores, and periods are allowed in your username.')])
    RoleChoices = [('A','Admin'),('D','Developer'),('O','Observer')]
    Role = models.CharField(max_length=1, choices=RoleChoices)
