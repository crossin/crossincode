from django.db import models

from oj import models as oj_models


class Language(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    count_student = models.IntegerField(default=0)
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    sequence = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=3000)
    count_student = models.IntegerField(default=0)
    count_finished = models.IntegerField(default=0)
    count_question = models.IntegerField(default=0)
    count_answer = models.IntegerField(default=0)
    course = models.ForeignKey(Course, related_name='lessons')
    quiz = models.OneToOneField(oj_models.Quiz, null=True, blank=True)

    @property
    def next_lesson(self):
        nl = Lesson.objects.filter(
            sequence__gt=self.sequence).order_by('sequence')[:1]
        if len(nl) > 0:
            return nl[0].id
        else:
            return None

    def __unicode__(self):
        return self.title
