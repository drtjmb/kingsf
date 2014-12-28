# see https://docs.djangoproject.com/en/dev/howto/custom-management-commands/

from django.core.management.base import BaseCommand, CommandError
from pymarc import MARCReader
import re
from pubs.models import Publication
import os.path

class Command(BaseCommand):
    args = '<filename>'
    help = 'Ingests MARC records'

    def handle(self, *args, **options):

        filename = args[0]
        if not os.path.isfile(filename):
            raise CommandError('File does not exist %s' % filename)

        pubs = []

        with open(filename,'rb') as fh:
            reader = MARCReader(fh, to_unicode=True)
            for record in reader:

                id = None
                if record['999'] is not None:
                    id = record['999']['c']

                if id is None:
                    continue

                pub = Publication(pk=id)
                pubs.append(pub)

                if record.title() is not None:
                    pub.title = record.title()

                if record['260'] is not None:
                    year = record['260']['c']
                    if year is not None:
                        match = re.search(r'\d{4}', year)
                        if match:
                            pub.year = match.group()

                if record['520'] is not None:
                    summary = record['520']['a']
                    if summary is not None:
                        pub.summary = summary

                authors = []
                for author in record.get_fields('100') + record.get_fields('700'):
                    if author['e'] is None:
                        authors.append(author['a'].strip())
                pub.authors = ';'.join(authors)

        Publication.objects.bulk_create(pubs)
