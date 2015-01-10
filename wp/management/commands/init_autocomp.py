from django.core.management.base import BaseCommand, CommandError
from nltk.corpus import stopwords
from wp.models import Fulltext, Term

class Command(BaseCommand):
    args = ''
    help = 'Prepare autocomplete data for Wellcome Player'

    def handle(self, *args, **options):

        stop = stopwords.words('english')

        for ft in Fulltext.objects.all():
            terms = set([])
            words = ft.text.split()
            for i, word in enumerate(words):
                if word in stop:
                    continue
                for x in range(1,4):
                    if len(words) >= i + x:
                        if words[i+x-1:i+x][0] in stop:
                            break
                        terms.add(' '.join(words[i:i+x]))

            t = [
                Term(
                    publication = ft.publication,
                    text = term,
                ) for term in iter(terms)
            ]
            Term.objects.bulk_create(t)
            print '%s: created %d terms' % (ft.publication_id, len(t))

# Alternative approach - focuses on nouns so might be better for site-wide autocomplete?
#
# from topia.termextract import extract
# extractor = extract.TermExtractor()
# extractor.filter = extract.permissiveFilter
# terms = []
# for ft in NormFulltext.objects.all():
#   for term in extractor(ft.text):
#       terms.append(
#           Term(
#               publication = ft.publication,
#               text = term[0],
#           )
#       )
#   Term.objects.bulk_create(terms)
