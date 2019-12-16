from django.contrib import admin
from .models import NoticeInfo
from .forms import NoticeInfoForm


class NoticeInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('기본 정보', {
            'fields': (('app_key', 'country_code', 'show_yn'),
                       ('skip_yn', 'reg_date', 'btn_ok'))
        }),
        ('제목/내용', {
            'fields': ('title', 'contents')
        }),
        ('시작/종료 일시', {
            'fields': ('start_date', 'end_date')
        }),
    )

    list_display = ('title', 'contents', 'app_key', 'country_code', 'show_yn', 'skip_yn', 'was_show_popup_now')
    form = NoticeInfoForm
    list_filter = ['app_key', 'country_code']


admin.site.register(NoticeInfo, NoticeInfoAdmin)
