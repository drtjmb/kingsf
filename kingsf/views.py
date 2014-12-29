from django.views.generic.base import TemplateView
from pubs.models import Publication

class CarouselView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(CarouselView, self).get_context_data(**kwargs)
        context['carousel'] = Publication.objects.all()[:10]
        return context
