from haystack import indexes;
from pubs.models import Publication

class PublicationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    year = indexes.CharField(model_attr='year', faceted=True)

    def get_model(self):
        return Publication
