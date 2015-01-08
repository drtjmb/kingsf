from django.core.management.base import BaseCommand, CommandError
from pubs.models import Publication, Line
from wp.models import NormFulltext, BoundingBox
from unicodedata import category
import re

class Command(BaseCommand):
    args = ''
    help = 'Prepares backend data for Wellcome Player'

    def handle(self, *args, **options):

        fulltexts = []
        bboxes = []

        for pub in Publication.objects.filter(has_fulltext=True):

            start_pos = 0
            fulltext = ''

            for line in pub.line_set.all():

                norm = line.text

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
                        line = line,
                        page = line.page,
                        start_pos = start_pos,
                        end_pos = end_pos,
                        x = int(line.l * BoundingBox.scale_factor),
                        y = int(line.t * BoundingBox.scale_factor),
                        w = int((line.r - line.l) * BoundingBox.scale_factor),
                        h = int((line.b - line.t) * BoundingBox.scale_factor),
                    )
                )

                start_pos = end_pos + 1 # next char

            fulltexts.append(
                NormFulltext(
                    publication = pub,
                    text = fulltext
                )
            )

            print pub.id

        BoundingBox.objects.bulk_create(bboxes)
        NormFulltext.objects.bulk_create(fulltexts)
