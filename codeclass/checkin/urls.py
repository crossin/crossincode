from django.conf.urls import patterns, url

from checkin import views


urlpatterns = patterns(
    '',
    url(r'^do/$', views.checkin),
    url(r'^login/$', views.login_user),
    url(r'^register/$', views.register_user),
    url(r'^$', views.home),

)
