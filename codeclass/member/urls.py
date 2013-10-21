from django.conf.urls import patterns, url

from member import views


urlpatterns = patterns(
    '',
    url(r'^$', views.profile_view),
)
