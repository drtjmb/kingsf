from django.shortcuts import get_object_or_404, render
from pubs.models import Publication

def detail(request, pubid):
    pub = get_object_or_404(Publication, pk=pubid)
    return render(request, 'pubs/detail.html', {'pub': pub})
