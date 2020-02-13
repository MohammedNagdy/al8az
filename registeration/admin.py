from django.contrib import admin
from .models import Article, Categories
from django.contrib.admin import AdminSite


# user name: nada
# pw: nadaowner

# chango the admin header
class MyAdminSite(AdminSite):
    site_header = 'al8az administration'


# Register your models here.
admin.site.register(Article)
admin.site.register(Categories)
