from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from kingsf.views import CarouselView
from pubs.models import Publication

urlpatterns = patterns('',
    url(r'^$', CarouselView.as_view(template_name='index.html')),
    url(r'^about.html$', TemplateView.as_view(template_name='about.html')),
    url('', include('pubs.urls')),
    url('^wp/', include('wp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
