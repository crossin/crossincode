from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, editable=False)
    username = models.CharField(max_length=30, db_index=True, editable=False)
    exp = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username
