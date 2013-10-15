from django.contrib import admin

from forum import models


class QuestionAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Answer, AnswerAdmin)
