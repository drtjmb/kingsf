from django.db import models
from pubs.models import Publication, Line

class NormFulltext(models.Model):
    publication = models.ForeignKey(Publication)
    text = models.TextField()

class BoundingBox(models.Model):
    scale_factor = 0.5
    line = models.ForeignKey(Line)
    page = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    w = models.IntegerField()
    h = models.IntegerField()
    # start and ending character pos (in entire document)
    start_pos = models.IntegerField()
    end_pos = models.IntegerField()

class Term(models.Model):
    publication = models.ForeignKey(Publication)
    text = models.TextField()
