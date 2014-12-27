from django.conf.urls import patterns, include, url
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView
from pubs import views

sqs = SearchQuerySet().facet('year').facet('author')

urlpatterns = patterns('haystack.views',
    url(r'^search/', FacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs), name='haystack_search'),
    url(r'^(?P<pubid>\d+)/', views.detail, name='detail'),
)
