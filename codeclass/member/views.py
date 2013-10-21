from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

from member import models


@login_required
def profile_view(request):
    student = request.user.student
    courses = models.LearnedCourse.objects.filter(student=student)
    return TemplateResponse(
        request,
        'member/profile.html',
        {
            'student': student,
            'courses': courses,
        }
    )
