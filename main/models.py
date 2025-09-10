import uuid
from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50)
    thumbnail = models.URLField(blank=True, null=True)
    news_views = models.PositiveIntegerField(default=0)
    stock = models.IntegerField()
    size = models.IntegerField()
    
    def __str__(self):
        return self.title
    