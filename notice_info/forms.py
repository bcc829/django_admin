from django.forms import ModelForm
from .validation import validation_str_date_format
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

    class Meta:
        model = NoticeInfo
        fields = '__all__'
