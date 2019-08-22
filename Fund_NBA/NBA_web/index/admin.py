from django.contrib import admin

# Register your models here.

from .models import NBAData

# 把创建的model库 连接网页
admin.site.register(NBAData)