from haystack import indexes;
from wp.models import Term

class TermIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True,model_attr='text')
    auto_text = indexes.EdgeNgramField(model_attr='text')
    publication_id = indexes.IntegerField(model_attr='publication_id', stored=True)

    def get_model(self):
        return Term
