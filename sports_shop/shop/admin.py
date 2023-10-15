from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'supplier', 'description',
                    'photo', 'producing_country')
    list_display_links = ('id', 'name', 'category', 'supplier', 'producing_country')
    search_fields = ('name', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'address')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class ProducingCountriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')
    list_display_links = ('id', 'name')
    search_fields = ('name',)



admin.site.register(Products, ProductAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(Suppliers, SupplierAdmin)
admin.site.register(ProducingCountries, ProducingCountriesAdmin)
