from django.contrib import admin

# Register your models here.
from inside.models import *
admin.site.register(SanPham)
admin.site.register(UserProfileInfo)
