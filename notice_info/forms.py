from django.forms import ModelForm
from .validation import validation_str_date_format, validation_empty_str
from .models import NoticeInfo
from django import forms


class NoticeInfoForm(ModelForm):
    contents = forms.CharField(widget=forms.Textarea)

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']
        return validation_str_date_format(start_date)

    def clean_end_date(self):
        end_date = self.cleaned_data['end_date']
        return validation_str_date_format(end_date)

    def clean_btn_ok(self):
        btn_ok = self.cleaned_data['btn_ok']
        return validation_empty_str(btn_ok)

    class Meta:
        model = NoticeInfo
        fields = '__all__'
