from django.db import models

from crud_api.models import Item

class Message(models.Model):
    title = models.CharField(max_length=200)
    metatitle = models.CharField(max_length=500, default=None, blank=True, null=True)
    description = models.CharField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Item, related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'