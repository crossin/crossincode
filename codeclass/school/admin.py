from django.contrib import admin

from school import models


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'sequence', 'title', 'content']


class LearnedLessonAdmin(admin.ModelAdmin):
    pass


class LearnedCourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Lesson, LessonAdmin)
admin.site.register(models.LearnedLesson, LearnedLessonAdmin)
admin.site.register(models.LearnedCourse, LearnedCourseAdmin)
