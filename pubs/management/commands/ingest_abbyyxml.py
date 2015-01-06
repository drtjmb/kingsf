from django.core.management.base import BaseCommand, CommandError
from xml.etree import ElementTree
from pubs.models import Publication, Line
from os.path import isfile, isdir, join
from glob import glob
from unicodedata import category
import re

class Command(BaseCommand):
    args = '<pubid> <filename>'
    help = 'Ingests ABBYY OCR (XML)'

    def handle(self, *args, **options):

        id = args[0]
        pub, created = Publication.objects.get_or_create(pk=id)

        dir = args[1]
        if not isdir(dir):
            raise CommandError('Not a dir: %s' % dir)

        lines = []
        start_pos = 0

        for filename in sorted(glob(join(dir,'*.xml'))):

            if not isfile(filename):
                continue

            page = None
            match = re.search(r'(\d+)\.xml$', filename)
            if match:
                page = match.group(1)

            with open(filename,'rb') as fh:
                tree = ElementTree.parse(fh)
                root = tree.getroot()

                for line in root.iter('{http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml}line'):
                   
                    raw = line.find('*').text

                    norm = raw
                    if isinstance(norm, str):
                        norm = norm.decode('utf-8')

                    norm = u''.join(ch for ch in norm if category(ch)[0] != 'P')
                    norm = u' '.join(norm.split()).strip().lower()
                    if norm.endswith(u'\u00ac'): # U+00AC (not sign) introduced by abbyy
                        norm = norm[:-1]
                    else:
                        norm = u'%s ' % norm # note trailing space

                    end_pos = start_pos + len(norm) - 1

                    lines.append(
                        Line(
                            publication=pub,
                            page=page,
                            text_raw=raw,
                            text=norm,
                            start_pos=start_pos,
                            end_pos=end_pos,
                            l=line.get('l'),
                            t=line.get('t'),
                            r=line.get('r'),
                            b=line.get('b')
                        )
                    )

                    start_pos = end_pos + 1 # next char

        print '%s : %d lines' % (id, len(lines))
        Line.objects.bulk_create(lines)

        pub.has_fulltext = True
        pub.num_pages = lines[-1].page
        pub.save()
