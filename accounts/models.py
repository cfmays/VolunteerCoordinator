from django.db import models
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    # Organization types/categories
    C = 'Charity'
    M = 'Commercial'
    R = 'Religious'
    name = models.CharField(max_length=2)
    category = (
        ('C', C)
        ('M', M)
        ('R', R)
    )


class Role(models.Model):
    title = models.CharField(max_length=100)
    # Permissions TBD


# class User(AbstractUser):
#     # Placeholder to allow customization of User model in future
#     pass
