from django.contrib import admin

from member import models


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'exp', 'gold']


class LearnedLessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'lesson', 'time_learned']


class LearnedCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'progress', 'time_learned']


admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.LearnedLesson, LearnedLessonAdmin)
admin.site.register(models.LearnedCourse, LearnedCourseAdmin)
