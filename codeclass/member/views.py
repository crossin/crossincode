from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from registration.backends.default.views import ActivationView \
    as BaseActivationView
from registration.models import RegistrationProfile

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


class ActivationView(BaseActivationView):
    # prevent django-registration duplicate signal bug
    def activate(self, request, activation_key):
        return RegistrationProfile.objects.activate_user(activation_key)
