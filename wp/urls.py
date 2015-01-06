from django.conf.urls import patterns, include, url
from wp import views

urlpatterns = patterns('',
    url(r'^package/(?P<pubid>\d+)', views.package, name='wp_package'),
    url(r'^biblio/(?P<pubid>\d+)', views.biblio, name='wp_biblio'),
    url(r'^service/search/(?P<pubid>\d+)', views.search, name='wp_search'),
    #url(r'^autocomplete/(?P<pubid>\d+)', views.autocomplete, name='wp_autocomplete'),
    url(r'^fc', views.fc, name='wp_fc'),
)
