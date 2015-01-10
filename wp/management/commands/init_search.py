from django.core.management.base import BaseCommand, CommandError
from pubs.models import Publication, Block
from wp.models import Fulltext, BoundingBox
from unicodedata import category
import re

class Command(BaseCommand):
    args = ''
    help = 'Prepare search data for Wellcome Player'

    def handle(self, *args, **options):

        fulltexts = []

        for pub in Publication.objects.filter(volume__publication__isnull=False).distinct():

            bboxes = []
            start_pos = 0
            fulltext = ''

            for block in Block.objects.filter(page__volume__publication=pub).order_by('page__volume__volume','page__page','block'):

                norm = block.text

                if isinstance(norm, str):
                    norm = norm.decode('utf-8')

                norm = u''.join(ch for ch in norm if category(ch)[0] != 'P')
                norm = u' '.join(norm.split()).strip().lower()
                if norm.endswith(u'\u00ac'): # U+00AC (not sign) introduced by abbyy
                    norm = norm[:-1]
                else:
                    norm = u'%s ' % norm # note trailing space
                fulltext += norm

                end_pos = start_pos + len(norm) - 1

                bboxes.append(
                    BoundingBox(
                        publication = pub,
                        block = block,
                        page = block.page.page,
                        start_pos = start_pos,
                        end_pos = end_pos,
                        x = int(block.l * BoundingBox.scale_factor),
                        y = int(block.t * BoundingBox.scale_factor),
                        w = int((block.r - block.l) * BoundingBox.scale_factor),
                        h = int((block.b - block.t) * BoundingBox.scale_factor),
                    )
                )

                start_pos = end_pos + 1 # next char

            fulltexts.append(
                Fulltext(
                    publication = pub,
                    text = fulltext
                )
            )

            BoundingBox.objects.bulk_create(bboxes)
            print '%s: created %d bounding boxes' % (pub.get_id(), len(bboxes))

        Fulltext.objects.bulk_create(fulltexts)
        print 'Created %d fulltexts' % len(fulltexts)
