from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import api as ccapi

admin.autodiscover()

from tastypie.api import Api

api = Api(api_name='alpha')
api.register(ccapi.LessonResource())

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
    # Examples:
    # url(r'^$', 'codeclass.views.home', name='home'),
    # url(r'^codeclass/', include('codeclass.foo.urls')),
)
