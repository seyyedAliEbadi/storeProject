from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


class Profile(models.Model):
    pass


class Address(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    alley = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.city}-{self.street}-{self.alley}'


class Shop(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    description = models.TextField()
    image = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class Email(models.Model):
    subject = models.CharField(max_length=150)
    body = models.TextField()
