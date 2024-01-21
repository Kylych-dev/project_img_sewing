from django.contrib import admin
from .models import Cat, Owner

@admin.register(Cat)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Owner)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)