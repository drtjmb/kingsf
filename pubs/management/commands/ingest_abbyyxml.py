from django.core.management.base import BaseCommand, CommandError
from xml.etree import ElementTree
from pubs.models import Publication, Volume, Page, Block
from os.path import isfile, isdir, join
from glob import glob
import re

class Command(BaseCommand):
    args = '<pubid> <volume> <pages_dir>'
    help = 'Ingests ABBYY OCR (XML)'

    def handle(self, *args, **options):

        id = args[0]

        pub = Publication.objects.get(pk=id)
        if pub is None:
            raise CommandError('Publication does not exist: %s' % id)

        dir = args[2]
        if not isdir(dir):
            raise CommandError('Not a directory: %s' % dir)

        vol = args[1]
        volume = Volume(publication=pub,volume=vol)
        volume.save()

        blocks = []

        for filename in sorted(glob(join(dir,'*.xml'))):

            if not isfile(filename):
                continue

            p = None
            match = re.search(r'(\d+)\.xml$', filename)
            if match:
                p = match.group(1)
            else:
                print 'Could not extract page number from %s' % filename
                continue

            page = Page(volume=volume,page=p)
            page.save()

            with open(filename,'rb') as fh:
                tree = ElementTree.parse(fh)
                root = tree.getroot()

                for i, block in enumerate(root.iter('{http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml}line')):
                   
                    blocks.append(
                        Block(
                            page=page,
                            block=i,
                            text=block.find('*').text,
                            l=block.get('l'),
                            t=block.get('t'),
                            r=block.get('r'),
                            b=block.get('b')
                        )
                    )

        print '%s (%s): %s pages, %d blocks' % (pub.get_id(), volume.get_volume(), volume.page_set.count(), len(blocks))
        Block.objects.bulk_create(blocks)
