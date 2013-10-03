from django.contrib import admin

from . import models


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'exp', 'gold']


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


class QuizAdmin(admin.ModelAdmin):
    pass


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']


class LearnedLessonAdmin(admin.ModelAdmin):
    pass


class LearnedCourseAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.Lesson, LessonAdmin)
admin.site.register(models.LearnedLesson, LearnedLessonAdmin)
admin.site.register(models.LearnedCourse, LearnedCourseAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Answer, AnswerAdmin)
