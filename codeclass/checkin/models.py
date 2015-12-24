from django.contrib.auth.models import User
from django.db import models


class Log(models.Model):
    user = models.ForeignKey(User, editable=False)
    record = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now_add=True)


class Stat(models.Model):
    user = models.OneToOneField(User, editable=False)
    exp = models.IntegerField(default=0)
    checkin_days = models.IntegerField(default=0)
    running_days = models.IntegerField(default=0)
    month_running = models.IntegerField(default=0)
    last_checkin = models.DateField(default=None, is_null=True, blank=True)
