from django.db import models


class CountryCode(models.TextChoices):
    Korea = 'KR'
    Japan = 'JP'
    USA = 'US'
    Germany = 'DE'
    Italy = 'IT'
    OtherCountries = 'ETC'


class AppKey(models.TextChoices):
    AOS = 'COIOANP0'
    IOS = 'COIOIOP0'


class YesOrNo(models.TextChoices):
    YES = 'Y'
    NO = 'N'
