from django.contrib import admin
from .models import *


class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'available', 'stock')
    search_fields = ('id', 'name', 'price',)
    list_display_links = ('id', 'name', 'available')


class Categories(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_display_links = ('id', 'name',)


class BasketAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name', 'price',)
    list_display_links = ('name', 'price',)


admin.site.register(Category, Categories)
admin.site.register(Product, Products)
admin.site.register(Basket, BasketAdmin)
