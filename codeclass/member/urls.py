from django.conf.urls import include, patterns, url
from django.views.generic.base import TemplateView
from registration.backends.default.views import RegistrationView

from member import views, forms


urlpatterns = patterns(
    '',
    url(r'^$', views.profile_view),
    url(r'register/$',
        RegistrationView.as_view(form_class=forms.RegistrationForm),
        name='registration_register'),
    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$',
        views.ActivationView.as_view(),
        name='registration_activate'),
    url(r'^', include('registration.backends.default.urls')),

)
