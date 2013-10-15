from django.contrib import admin

from oj import models


class QuizAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Quiz, QuizAdmin)
