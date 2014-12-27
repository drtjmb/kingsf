from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kingsf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^about.html$', TemplateView.as_view(template_name='about.html')),
    url(r'^pubs/', include('pubs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
