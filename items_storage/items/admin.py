from django.contrib import admin
from .models import Item

# Register your models here.

class Item_admin(admin.ModelAdmin):
    #Display list in admin
    list_display = ('name', 'description', 'price', 'created_at')
    #Sorting
    list_filter = ('name', 'price', 'created_at')

admin.site.register(Item, Item_admin)
