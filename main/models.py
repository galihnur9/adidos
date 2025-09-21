import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shirt', 'Shirt'),
        ('pants', 'Pants'),
        ('shoes', 'Shoes'),
        ('socks', 'Socks'),
        ('jacket', 'Jacket'),
        ('sweater', 'Sweater'),
        ('shorts', 'Shorts'),
        ('accessories', 'Accessories'),
        ('others', 'Others'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='others')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    size = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    