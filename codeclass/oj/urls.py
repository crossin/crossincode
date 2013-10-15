from django.conf.urls.defaults import patterns, include, url

from dajaxice.core import dajaxice_autodiscover, dajaxice_config


dajaxice_autodiscover()

urlpatterns = patterns(
    '',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
