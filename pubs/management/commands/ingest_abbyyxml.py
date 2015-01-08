from django.core.management.base import BaseCommand, CommandError
from xml.etree import ElementTree
from pubs.models import Publication, Line
from os.path import isfile, isdir, join
from glob import glob
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

                for number, line in enumerate(root.iter('{http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml}line')):
                   
                    lines.append(
                        Line(
                            publication=pub,
                            page=page,
                            number=number,
                            text=line.find('*').text,
                            l=line.get('l'),
                            t=line.get('t'),
                            r=line.get('r'),
                            b=line.get('b')
                        )
                    )

        print '%s : %d lines' % (id, len(lines))
        Line.objects.bulk_create(lines)

        pub.has_fulltext = True
        pub.num_pages = lines[-1].page
        pub.save()
