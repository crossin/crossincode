from tastypie.resources import ModelResource
from . import models


class LessonResource(ModelResource):
    class Meta:
        queryset = models.Lesson.objects.all()
