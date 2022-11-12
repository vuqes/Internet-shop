from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
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
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    value = models.PositiveIntegerField(blank=True)
    user_of = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Корзина'
        verbose_name_plural = 'Товары в корзине'


class Account(models.Model):
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='users_photo/%Y/%m/%d', blank=True)
    phone = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
