from django.db import models


class AppKey(models.TextChoices):
    AOS_DEV = 'COIOANP0'
    IOS_DEV = 'COIOIOP0'
    AOS_PRE = 'COIFANP2'
    IOS_PRE = 'COIFIOP2'
    AOS_FREEZE = 'COIFANP1'
    IOS_FREEZE = 'COIFIOP1'
    AOS_STG = 'COIOANP1'
    IOS_STG = 'COIOIOP1'
