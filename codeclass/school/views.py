from django.template.response import TemplateResponse

from . import models


def home_view(request):
    languages = models.Language.objects.all()
    return TemplateResponse(request, 'home.html', {'languages': languages})


def language_view(request, language_id):
    language = models.Language.objects.get(id=language_id)
    courses = models.Course.objects.filter(language=language)
    return TemplateResponse(request, 'school/language.html', {
        'language': language,
        'courses': courses
    })


def course_view(request, course_id):
    course = models.Course.objects.get(id=course_id)
    lessons = models.Lesson.objects.filter(course=course)
    return TemplateResponse(request, 'school/course.html', {
        'course': course,
        'lessons': lessons
    })


def lesson_view(request, lesson_id):
    lesson = models.Lesson.objects.get(id=lesson_id)
    return TemplateResponse(request, 'school/lesson.html', {
        'lesson': lesson
    })
