from django.db import models
from accounts.models import Shop, User


# Create your models here.
class Product(models.Model):
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)


class ShopProduct(models.Model):
    shop = models.ForeignKey(to='Shop', on_delete=models.CASCADE)
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()


class Category(models.Model):
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    details = models.TextField()


class Brand(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()


class Image(models.Model):
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    image = models.CharField(max_length=150)


class Off(models.Model):
    pass


class Comment(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    text = models.TextField()

    EXCELLENT = 5
    GOOD = 4
    MEDIOCRE = 3
    NOT_BAD = 2
    AWFUL = 1

    rates_choices = (
        (EXCELLENT, 'عالی'),
        (GOOD, 'خوب'),
        (MEDIOCRE, 'متوسط'),
        (NOT_BAD, 'بد'),
        (AWFUL, 'خیلی بد'),
    )

    rate = models.IntegerField(choices=rates_choices)
