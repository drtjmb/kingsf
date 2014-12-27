from django.db import models
from django.core.urlresolvers import reverse

class Publication(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    year = models.CharField(max_length=4)
    summary = models.TextField()
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_author_names(self):
        names = []
        for author in Author.objects.filter(publication=self):
            names.append(author.name)
        return names

    def get_absolute_url(self):
        return reverse('pubs.views.detail', args=['%06d' % self.id])

class Author(models.Model):
    name = models.CharField(max_length=200)
    publication = models.ForeignKey(Publication)

    def __str__(self):
        return self.name

class Page(models.Model):
    number = models.IntegerField()
    publication = models.ForeignKey(Publication)

    def __str__(self):
        return self.number

class Line(models.Model):
    text = models.TextField()
    x = models.IntegerField()
    y = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()
    page = models.ForeignKey(Page)

    def __str__(self):
        return self.text
