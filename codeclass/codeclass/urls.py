from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^oj/', include('oj.urls')),
    url(r'^user/', include('member.urls')),
    url(r'^school/', include('school.urls')),
    url(r'^', views.index_view),
)
