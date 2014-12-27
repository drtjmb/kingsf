from django.core.management.base import BaseCommand, CommandError
from xml.etree import ElementTree
from pubs.models import Publication, Page, Line
import os.path

class Command(BaseCommand):
    args = '<pubid> <page> <filename>'
    help = 'Ingests ABBYY OCR (XML)'

    def handle(self, *args, **options):

        id = args[0]
        try:
            pub = Publication.objects.get(pk=id)
        except Publication.DoesNotExist:
            print 'Missing pub %d' % id
            return

        page = args[1]
        # TODO Page may already exist
        p = pub.page_set.create(number=page)

        filename = args[2]
        if not os.path.isfile(filename):
            raise CommandError('File does not exist %s' % filename)

        with open(filename,'rb') as fh:
            tree = ElementTree.parse(fh)
            root = tree.getroot()

            for l in root.iter('{http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml}line'):
                p.line_set.create(text=l.find('*').text,l=l.get('l'),t=l.get('t'),r=l.get('r'),b=l.get('b'))
