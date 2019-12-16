from django.db import models
from django.utils import timezone

import pytz
import datetime
from .textChoices import YesOrNo, AppKey, CountryCode
from .validation import validation_str_date_format


class NoticeInfo(models.Model):
    app_key = models.CharField(max_length=8, choices=AppKey.choices, default=AppKey.AOS)
    country_code = models.CharField(max_length=3, choices=CountryCode.choices, default=CountryCode.Korea)
    title = models.CharField(max_length=100, blank=True, null=True)
    contents = models.CharField(max_length=1024, blank=True, null=True)
    show_yn = models.CharField(max_length=1, choices=YesOrNo.choices, default=YesOrNo.YES)
    start_date = models.CharField(max_length=14, blank=True, null=True, validators=[validation_str_date_format])
    end_date = models.CharField(max_length=14, blank=True, null=True, validators=[validation_str_date_format])
    skip_yn = models.CharField(max_length=1, choices=YesOrNo.choices, default=YesOrNo.NO)
    id = models.BigAutoField(primary_key=True)
    reg_date = models.DateTimeField()
    btn_ok = models.CharField(max_length=100, blank=True, null=True)

    local_timezone = pytz.timezone('Asia/Seoul')

    def __str__(self):
        return self.title

    def was_show_popup_now(self):
        if self.show_yn == 'Y':
            now = timezone.now()
            date_start_date = self.get_date_to_start_date()
            date_end_date = self.get_date_to_end_date()
            return date_start_date <= now <= date_end_date
        else:
            return False

    def get_date_to_start_date(self):
        return self.local_timezone.localize(datetime.datetime.strptime(self.start_date, '%Y%m%d%H%M%S'))

    def get_date_to_end_date(self):
        return self.local_timezone.localize(datetime.datetime.strptime(self.end_date, '%Y%m%d%H%M%S'))

    def clean(self):
        validation_str_date_format

    was_show_popup_now.boolean = True
    was_show_popup_now.short_description = '현재 시간 기준 팝업 노출 여부'

    class Meta:
        managed = False
        app_label = 'notice_info'
        db_table = 'notice_info'
        ordering = ['-reg_date', '-show_yn']
