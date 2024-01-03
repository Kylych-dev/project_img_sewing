from django.contrib import admin
from .models import Shirt
@admin.register(Shirt)
class ShirtAdmin(admin.ModelAdmin):
    model = Shirt