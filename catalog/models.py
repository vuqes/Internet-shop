from django.db import models


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, db_index=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Basket(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    name = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    stock = models.PositiveIntegerField()
    value = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Корзина'
        verbose_name_plural = 'Товары в корзине'

    # def __str__(self):
    #     return self.name
