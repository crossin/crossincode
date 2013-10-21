from django.conf.urls import patterns, url

from school import views


urlpatterns = patterns(
    '',
    url(r'^$', views.home_view),
    url(r'^language/(?P<language_id>\d+)/$', views.language_view),
    url(r'^course/(?P<course_id>\d+)/$', views.course_view),
    url(r'^lesson/(?P<lesson_id>\d+)/$', views.lesson_view, name='lesson'),
)
