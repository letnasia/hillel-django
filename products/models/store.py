from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    opening_hour = models.IntegerField()
    closing_hour = models.IntegerField()
    specialization = models.CharField(max_length=255)
    products = models.ManyToManyField('products.Product', through='products.StoreInventory')

    def __str__(self):
        return f"[Store: {self.name}]"
