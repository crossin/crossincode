from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^checkin/', include('checkin.urls')),
    url(r'^oj/', include('oj.urls')),
    url(r'^user/', include('member.urls')),
    url(r'^school/', include('school.urls')),
    url(r'^wechat/', include('wechat.urls')),
    url(r'^$', 'codeclass.views.index_view'),
)
