from django.db import models
from .Movie import Movie


class Person(models.Model):
    externalId = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie)
