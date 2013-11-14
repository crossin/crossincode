from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

from oj import views


dajaxice_autodiscover()

urlpatterns = patterns(
    '',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^wechat/$', views.wechat_view),
    url(r'^output/$', views.output_view),
)
