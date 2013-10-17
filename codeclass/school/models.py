from django.db import models

from member import models as mb_models
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
    course = models.ForeignKey(Course)
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


STUTES_CHOICES = (
    ('N', 'new'),
    ('L', 'learned'),
    ('P', 'passed')
)


class LearnedLesson(models.Model):
    student = models.ForeignKey(mb_models.Student)
    lesson = models.ForeignKey(Lesson)
    status = models.CharField(max_length=1, choices=STUTES_CHOICES,
                              default='N')


class LearnedCourse(models.Model):
    student = models.ForeignKey(mb_models.Student)
    course = models.ForeignKey(Course)
    progress = models.IntegerField(default=0)
