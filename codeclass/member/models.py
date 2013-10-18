from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from registration.signals import user_activated


class Student(models.Model):
    user = models.OneToOneField(User, editable=False)
    exp = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username


@receiver(user_activated, dispatch_uid='create_student')
def create_student(sender, user, request, **kwargs):
    from django.db import IntegrityError
    try:
        Student.objects.create(user=user)
    except IntegrityError:
        # prevent django-registration duplicate signal bug
        pass
