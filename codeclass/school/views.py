from django.template.response import TemplateResponse
from django.shortcuts import redirect

from school import models
from member import models as mb_modles


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
    if request.method == 'POST':
        student = request.user.student
        course = lesson.course
        mb_modles.LearnedLesson.objects.get_or_create(
            student=student,
            lesson=lesson
        )
        lc, created = mb_modles.LearnedCourse.objects.get_or_create(
            student=student,
            course=course
        )
        count_all = course.lessons.count()
        count_learned = mb_modles.LearnedLesson.objects.filter(
            student=student,
            lesson__course=course
        ).count()
        progress = int(round(100.0 * count_learned / count_all))
        lc.progress = progress
        lc.save()
        return redirect('lesson', lesson_id=lesson.next_lesson)
    return TemplateResponse(request, 'school/lesson.html', {
        'lesson': lesson
    })
