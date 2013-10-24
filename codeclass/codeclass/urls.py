from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$',
        RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^oj/', include('oj.urls')),
    url(r'^user/', include('member.urls')),
    url(r'^', include('school.urls')),

)
