import json
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from pubs.models import Publication, Page
from wp.models import Fulltext, BoundingBox
from collections import OrderedDict
from haystack.query import SearchQuerySet
from django.db.models import Q

def package(request, pubid):
    pub = get_object_or_404(Publication, pk=pubid)

    pages = Page.objects.filter(volume__publication=pub).order_by('volume__volume','page')
    num_pages = pages.count()

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
                'assetCount': num_pages,
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
                    'assets': range(0,num_pages)
                },
            },
        ],
    }

    p = []
    for i, page in enumerate(pages, start=1):
        path = 'kingsf/%s/%s/%s.tif' % (pub.get_id(), page.volume.get_volume(), page.get_page())
        p.append({
            'identifier': path,
            'order': i,
            'orderLabel': '%s' % i,
            'dziUri': '/dz/%s.dzi' % path,
            'fileUri': '/%s' % path,
            'thumbnailPath': '/thumb/%s' % path,
        })
    data['assetSequences'][0]['assets'] = p

    return HttpResponse(json.dumps(data), content_type="application/json")

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
    sub = ' %s ' % sub # search on word boundaries
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start + 1
        start += len(sub)

def search(request, pubid):
    ft = get_object_or_404(Fulltext, publication_id=pubid)
    t = request.GET.get('t').lower()

    query = Q()
    for start_pos in find_all(ft.text, t):
        end_pos = start_pos + len(t) - 1
        query |= Q(start_pos__lte=start_pos,end_pos__gte=start_pos) # t starts in line
        query |= Q(start_pos__gt=start_pos,end_pos__lt=end_pos) # t straddles line
        query |= Q(start_pos__lte=end_pos,end_pos__gte=end_pos) # t ends in line
        if len(query) > 100:
            break

    data = []
    page = None
    n = 0
    bboxes = BoundingBox.objects.filter(publication_id=pubid) # TODO check lazy loading - is queryset only loaded from DB once or on each filter() ?
    for result in bboxes.filter(query):
        # TODO need page number within combined volumes
        if page is not None and page['index'] != result.page:
            data.append(page)
            page = None
        if page is None:
            page = { 'index': result.page, 'rects': [] }
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
