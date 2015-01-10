from django.db import models
from pubs.models import Publication, Block

class Fulltext(models.Model):
    publication = models.ForeignKey(Publication)
    text = models.TextField()

class BoundingBox(models.Model):
    scale_factor = 0.5
    publication = models.ForeignKey(Publication)
    block = models.ForeignKey(Block)
    page = models.IntegerField(db_index=True)
    x = models.IntegerField()
    y = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()
    # start and ending character pos (in Fulltext.text)
    start_pos = models.IntegerField(db_index=True)
    end_pos = models.IntegerField(db_index=True)

class Term(models.Model):
    publication = models.ForeignKey(Publication)
    text = models.TextField()
