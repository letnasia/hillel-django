from django.db import models
from products.models.store import Store
from products.models.product import Product


class StoreInventory(models.Model):
    store = models.ForeignKey('products.Store', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    product_details = models.TextField()

    class Meta:
        unique_together = ('store', 'product')

    def __str__(self):
        return f'Store: {self.store.name}, product: {self.product.name}'
