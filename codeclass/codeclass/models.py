from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, editable=False)
    username = models.CharField(max_length=30, db_index=True, editable=False)
    exp = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username


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


class Quiz(models.Model):
    content = models.CharField(max_length=3000)
    test_code = models.CharField(max_length=300)


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=3000)
    count_student = models.IntegerField(default=0)
    count_finished = models.IntegerField(default=0)
    count_question = models.IntegerField(default=0)
    count_answer = models.IntegerField(default=0)
    course = models.ForeignKey(Course)
    quiz = models.OneToOneField(Quiz, null=True, blank=True)

    def __unicode__(self):
        return self.title


STUTES_CHOICES = (
    ('N', 'new'),
    ('L', 'learned'),
    ('P', 'passed')
)


class LearnedLesson(models.Model):
    student = models.ForeignKey(Student)
    lesson = models.ForeignKey(Lesson)
    status = models.CharField(max_length=1, choices=STUTES_CHOICES,
                              default='N')


class LearnedCourse(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    progress = models.IntegerField(default=0)


class Question(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Student)
    lesson = models.ForeignKey(Lesson, null=True)


class Answer(models.Model):
    content = models.CharField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Student)
    question = models.ForeignKey(Question)
