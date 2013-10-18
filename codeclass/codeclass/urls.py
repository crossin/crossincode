from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration import views as reg_views, forms as reg_forms

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', reg_views.RegistrationView.as_view(
        form_class=reg_forms.RegistrationFormUniqueEmail),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^oj/', include('oj.urls')),
    url(r'^', include('school.urls')),

)
