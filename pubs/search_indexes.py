from haystack import indexes;
from pubs.models import Publication

class PublicationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='pubs/indexes/publication_text.txt')
    author = indexes.MultiValueField(model_attr='get_author_list', faceted=True)
    year = indexes.CharField(model_attr='year', faceted=True)

    def get_model(self):
        return Publication

    def index_queryset(self,using=None):
        """ Only index publications with full text """
        return self.get_model().objects.filter(volume__publication__isnull=False).distinct()
