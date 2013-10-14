from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

from . import api as ccapi, views

admin.autodiscover()
dajaxice_autodiscover()

api = Api(api_name='alpha')
api.register(ccapi.LessonResource())

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),

    url(r'^$', views.home_view),
    url(r'^language/(?P<language_id>\d+)/$', views.language_view),
    url(r'^course/(?P<course_id>\d+)/$', views.course_view),
    url(r'^lesson/(?P<lesson_id>\d+)/$', views.lesson_view),

#    url(r'^run/code/$', ajax.run_code)
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
