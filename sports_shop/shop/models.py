from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey('Categories', models.PROTECT)
    supplier = models.ForeignKey('Suppliers', models.PROTECT)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    producing_country = models.ForeignKey('ProducingCountries', models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        managed = True
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        return self.name


class Suppliers(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'suppliers'
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProducingCountries(models.Model):
    name = models.CharField(max_length=255)
    index = models.CharField(max_length=10, unique=True, verbose_name='Индекс страны')

    class Meta:
        db_table = 'producing_countries'
        verbose_name = 'Производящая страна'
        verbose_name_plural = 'Производящие страны'

    def __str__(self):
        return self.name
