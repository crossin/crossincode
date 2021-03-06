import datetime
from django.contrib.auth.models import User
from django.db import models


class Log(models.Model):
    user = models.ForeignKey(User, editable=False)
    record = models.CharField(max_length=1024)
    exp = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)


class Stat(models.Model):
    user = models.OneToOneField(User, editable=False)
    exp = models.IntegerField(default=0)
    checkin_days = models.IntegerField(default=0)
    running_days = models.IntegerField(default=0)
    month_running = models.IntegerField(default=0)
    last_checkin = models.DateField(default=datetime.date.min)
    supports = models.IntegerField(default=0)


class Support(models.Model):
    user = models.ForeignKey(User, editable=False)
    supporter = models.ForeignKey(User, default=None, null=True, blank=True,
                                  editable=False, related_name='supported')
    support_ip = models.CharField(max_length=1024, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
