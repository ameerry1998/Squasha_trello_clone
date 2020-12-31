from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_Profile


# Register your models here.

admin.site.register(User_Profile)
