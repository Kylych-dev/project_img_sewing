from django.contrib import admin
from .models import Stock, Warehouse
from ..product.models import Product

class StockInline(admin.TabularInline):
    model = Stock

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    inlines = [
        StockInline,
    ]
    list_display = ('name',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'quantity') 