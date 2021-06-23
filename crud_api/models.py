from django.db import models
from datetime import datetime

class Item(models.Model):
    title = models.CharField(max_length=200)
    metatitle = models.CharField(max_length=500, default=None, blank=True, null=True)
    description = models.CharField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'