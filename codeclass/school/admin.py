from django.contrib import admin

from school import models


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'sequence', 'title', 'content']


admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Lesson, LessonAdmin)
