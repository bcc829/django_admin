from django.contrib import admin

from notice_info.admin import NoticeInfoAdmin
from .models import NoticeInfo

# Register your models here.
admin.site.register(NoticeInfo, NoticeInfoAdmin)
