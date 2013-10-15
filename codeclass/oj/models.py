from django.db import models


class Quiz(models.Model):
    content = models.CharField(max_length=3000)
    test_code = models.CharField(max_length=300)
