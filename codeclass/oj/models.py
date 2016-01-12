from django.db import models


class Quiz(models.Model):
    content = models.CharField(max_length=3000)
    pre_code = models.CharField(max_length=3000)
    test_code = models.CharField(max_length=300)

    def __unicode__(self):
        return self.content


class Sample(models.Model):
    seq = models.IntegerField()
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    code = models.CharField(max_length=3000)
    url = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title
