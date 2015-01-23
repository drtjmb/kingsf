from django.shortcuts import get_object_or_404, render
from pubs.models import Publication
import haystack.views

def detail(request, pubid):
    pub = get_object_or_404(Publication, pk=pubid)
    return render(request, 'pubs/detail.html', {'pub': pub})

class FacetedSearchView(haystack.views.FacetedSearchView):
    """ just adding some extra context """
    def extra_context(self):
        context = super(FacetedSearchView, self).extra_context()

        sf = {}
        for facet in self.request.GET.getlist('selected_facets'):
            field, value = facet.split('_exact:')
            if not sf.has_key(field):
                sf[field] = []
            sf[field].append(value)
        context['selected_facets'] = sf

        return context
