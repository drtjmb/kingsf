from django.db import models
from django.core.urlresolvers import reverse

class Publication(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    authors = models.TextField()
    year = models.CharField(max_length=4)
    summary = models.TextField()
    has_fulltext = models.BooleanField('include in search results',default=False)
    featured = models.BooleanField('include in carousel',default=False)
    num_pages = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    def get_id(self):
        return '%06d' % self.id;

    def get_fulltext(self):
        text = []
        for line in self.line_set.order_by('page','number'):
            text.append(line.text)
        return ' '.join(text)

    def get_author_list(self):
        return self.authors.split(';')

    def get_absolute_url(self):
        return reverse('pubs.views.detail', args=[self.get_id()])

class Line(models.Model):

    publication = models.ForeignKey(Publication)
    page = models.IntegerField()
    number = models.IntegerField()
    text = models.TextField()
    # bounding box (original scan)
    l = models.IntegerField()
    t = models.IntegerField()
    r = models.IntegerField()
    b = models.IntegerField()

    def __str__(self):
        return self.text
