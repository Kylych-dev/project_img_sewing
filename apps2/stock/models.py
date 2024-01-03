from django.db import models
from ..product.models import Product 

class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    products = models.ManyToManyField(
        Product, 
        through='Stock'
        )
    
    class Meta:
        ordering = ('name',)
        # index_together = (('id', 'slug'),)

    def __str__(self) -> str:
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
        )
    warehouse = models.ForeignKey(
        Warehouse, 
        on_delete=models.CASCADE
        )
    quantity = models.IntegerField(default=0)

    class Meta:
        ordering = ('product',)
        # index_together = (('id',),)

    def __str__(self) -> str:
        return f"{self.product.name} - {self.warehouse.name} ({self.quantity})"

