from django.contrib import admin
from publications.models import Tag, Post
# Register your models here.


admin.site.register([Tag, Post])