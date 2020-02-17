from django.db import models
from django.utils import timezone


class Movie(models.Model):
    externalId = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)
