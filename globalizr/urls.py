# Routing logic for API and html
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Homepage
    url(r'^$', 'globalizr.views.home', name='home'),
    url(r'^home/$', 'globalizr.views.home', name='home'),
    # About page
    url(r'^about/$', 'globalizr.views.about', name='about'),

    # World page: Debugging information.
    url(r'^world/$', 'globalizr.views.world', name='world'),

    # API
    #-- query
    url(r'^api/query/(\w+)/$', 'globalizr.api.views.query', name='query'),
)
