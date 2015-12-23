from django.conf.urls import patterns, url

from checkin import views


urlpatterns = patterns(
    '',
    url(r'^do/$', views.checkin),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^$', views.home),

)
