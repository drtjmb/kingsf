from django.db import models
from django.core.urlresolvers import reverse

class Publication(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    authors = models.TextField()
    year = models.CharField(max_length=4)
    summary = models.TextField()
    featured = models.BooleanField('include in carousel',default=False)

    def __str__(self):
        return '[%s] %s' % (self.get_id(), self.title)

    def get_id(self):
        return '%06d' % self.id;

    def get_text(self):
        text = []
        for volume in self.volume_set.order_by('volume'):
            text.append(volume.get_text())
        return ' '.join(text)

    def get_author_list(self):
        return self.authors.split(';')

    def get_num_pages(self):
        count = 0
        for volume in self.volume_set.order_by('volume'):
            count += volume.get_num_pages()
        return count

    def has_fulltext(self):
        if self.get_num_pages > 0:
            return True
        return False

    def get_absolute_url(self):
        return reverse('pubs.views.detail', args=[self.get_id()])

class Volume(models.Model):
    publication = models.ForeignKey(Publication)
    volume = models.IntegerField(db_index=True)

    def __str__(self):
        return 'Vol. %s' % self.get_volume()

    def get_volume(self):
        return '%02d' % int(self.volume)

    def get_text(self):
        text = []
        for page in self.page_set.order_by('page'):
            text.append(page.get_text())
        return ' '.join(text)

    def get_num_pages(self):
        return self.page_set.count()

class Page(models.Model):
    volume = models.ForeignKey(Volume)
    page = models.IntegerField(db_index=True)

    def __str__(self):
        return 'p. %s' % self.get_page()

    def get_page(self):
        return '%04d' % self.page

    def get_text(self):
        text = []
        for block in self.block_set.order_by('block'):
            text.append(block.get_text())
        return ' '.join(text)

class Block(models.Model):
    page = models.ForeignKey(Page)
    block = models.IntegerField(db_index=True)
    text = models.TextField()
    # bounding box (original scan)
    l = models.IntegerField()
    t = models.IntegerField()
    r = models.IntegerField()
    b = models.IntegerField()

    def __str__(self):
        return self.text

    def get_text(self):
        return self.text
