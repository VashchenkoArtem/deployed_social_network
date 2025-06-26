from django.contrib import admin
from .models import Avatar, VerificationCode
# Register your models here.


admin.site.register([Avatar, VerificationCode])