from django.db import models
from django.core.urlresolvers import reverse

class Publication(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    authors = models.TextField()
    year = models.CharField(max_length=4)
    summary = models.TextField()
    indexed = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_fulltext(self):
        text = []
        for line in self.line_set.order_by('number','pk'):
            text.append(line.text)
        return ' '.join(text)

    def get_absolute_url(self):
        return reverse('pubs.views.detail', args=['%06d' % self.id])

class Line(models.Model):
    publication = models.ForeignKey(Publication)
    page = models.IntegerField()
    text = models.TextField()
    l = models.IntegerField()
    t = models.IntegerField()
    r = models.IntegerField()
    b = models.IntegerField()

    def __str__(self):
        return self.text
