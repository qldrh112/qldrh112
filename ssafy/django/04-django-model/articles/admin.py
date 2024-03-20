from django.contrib import admin
from .models import Article

# Register your models here.
# amdin 사이트에 등록한다. Article class를
admin.site.register(Article)