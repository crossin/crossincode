from django.db import models

from school import models as sc_models
from member import models as mb_models


class Question(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(mb_models.Student)
    lesson = models.ForeignKey(sc_models.Lesson, null=True)


class Answer(models.Model):
    content = models.CharField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(mb_models.Student)
    question = models.ForeignKey(Question)
