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
    num_pages = models.IntegerField()

    def __str__(self):
        return self.title

    def get_id(self):
        return '%06d' % self.id;

    def get_fulltext(self):
        text = []
        for line in self.line_set.order_by('page','start_pos'):
            text.append(line.text)
        return ''.join(text) # note ''

    def get_fulltext_raw(self):
        text_raw = []
        for line in self.line_set.order_by('page','start_pos'):
            text.append(line.text_raw)
        return ' '.join(text_raw)

    def get_author_list(self):
        return self.authors.split(';')

    def get_absolute_url(self):
        return reverse('pubs.views.detail', args=[self.get_id()])

class Line(models.Model):

    scale_factor = 0.5

    publication = models.ForeignKey(Publication)
    page = models.IntegerField()
    text = models.TextField()
    text_raw = models.TextField()
    # start and ending character pos (in entire document)
    start_pos = models.IntegerField()
    end_pos = models.IntegerField()
    # bounding box (original scan)
    l = models.IntegerField()
    t = models.IntegerField()
    r = models.IntegerField()
    b = models.IntegerField()

    def __str__(self):
        return self.text

    def get_x(self):
        return self.l * self.scale_factor

    def get_y(self):
        return self.t * self.scale_factor

    def get_width(self):
        return ( self.r - self.l ) * self.scale_factor

    def get_height(self):
        return ( self.b - self.t ) * self.scale_factor
