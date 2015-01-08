import json
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from pubs.models import Publication, Line
from wp.models import NormFulltext, BoundingBox
from collections import OrderedDict
from haystack.query import SearchQuerySet
from django.db.models import Q

def package(request, pubid):
    pub = get_object_or_404(Publication, pk=pubid)

    data = {
        'identifier': pub.get_id(),
        'bibliographicInformation': reverse('wp.views.biblio', args=[pub.get_id()]),
        'extensions': { 
            'isAllOpen': 'true'
        },
        'assetSequences': [
            {
                'extensions': {
                    'permittedOperations': [
                        'entireDocumentAsPdf',
                        'embed',
                    ],
                },
                'packageIdentifier': pub.get_id(),
                'index': 0,
                'assetType': 'seadragon/dzi',
                'assetCount': pub.num_pages,
                'supportsSearch': "true",
                'autoCompletePath': reverse('wp.views.autocomplete',args=[pub.get_id()]),
                'rootSection': {
                    'extensions': {
                        'accessCondition': 'Open',
                        'authStatus': 'Allowed',
                        'mods': {
                            'title': pub.title,
                        },
                    },
                    'title': pub.title,
                    'sectionType': 'Monograph',
                    'assets': range(0,pub.num_pages)
                },
            },
        ],
    }

    pages = []
    for i in range(1,pub.num_pages+1):
        path = 'kingsf/%s/01/%04d.tif' % (pub.get_id(), i)
        pages.append({
            'identifier': path,
            'order': i,
            'orderLabel': '%s' % i,
            'dziUri': '/dz/%s.dzi' % path,
            'fileUri': '/%s' % path,
            'thumbnailPath': '/thumb/%s' % path,
        })
    data['assetSequences'][0]['assets'] = pages

    return HttpResponse(json.dumps(data, indent=2, separators=(',',': ')), content_type="application/json")

def biblio(request, pubid):
    pub = get_object_or_404(Publication, pk=pubid)
    data = OrderedDict([
        ('Title', pub.title),
        ('Author(s)', pub.authors),
        ('Publication date', pub.year),
        ('Summary', pub.summary)
    ])
    return HttpResponse(json.dumps(data), content_type="application/json")

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def search(request, pubid):
    ft = get_object_or_404(NormFulltext, publication_id=pubid)
    t = request.GET.get('t').lower()

    data = []
    page = None
    n = 0
    lines = BoundingBox.objects.filter(line__publication_id=pubid) # TODO check lazy loading - is queryset only loaded from DB once or on each filter() ?
    for start_pos in find_all(ft.text, t):
        end_pos = start_pos + len(t) - 1
        for result in lines.filter(
            Q(start_pos__lte=start_pos,end_pos__gte=start_pos) | # t starts in line
            Q(start_pos__gt=start_pos,end_pos__lt=end_pos) | # t straddles line
            Q(start_pos__lte=end_pos,end_pos__gte=end_pos) # t ends in line
        ):
            if page is not None and page['index'] != result.page - 1:
                data.append(page)
                page = None
            if page is None:
                page = { 'index': result.page - 1, 'rects': [] }
            page['rects'].append({
                'hit': n,
                'x': result.x,
                'y': result.y,
                'w': result.w,
                'h': result.h,
            })
            n += 1
    if page is not None: data.append(page)
        
    return HttpResponse(json.dumps(data), content_type="application/json")

def autocomplete(request, pubid):
    sqs = SearchQuerySet().using('autocomplete').filter(publication_id=pubid,auto_text=request.GET.get('term', ''))[:10]
    suggestions = [result.auto_text for result in sqs]

    return HttpResponse(json.dumps(suggestions), content_type="application/json")

def fc(request):
    if 'callback' in request.REQUEST:
        data = {}
        data['Success'] = True
        data['Message'] = None
        data = '%s(%s);' % (request.REQUEST['callback'], json.dumps(data))
        return HttpResponse(data, "text/javascript")
    raise Http404