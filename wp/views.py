import json
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from pubs.models import Publication, Line
from collections import OrderedDict
from haystack.query import SearchQuerySet

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
                #'autoCompletePath': reverse('wp.views.autocomplete',args=[pub.get_id]),
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

def fc(request):
    if 'callback' in request.REQUEST:
        data = {}
        data['Success'] = True
        data['Message'] = None
        data = '%s(%s);' % (request.REQUEST['callback'], data)
        return HttpResponse(data, "text/javascript")
    raise Http404
