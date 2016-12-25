from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)
    org_type = (
        ('C', 'Charity')
        ('M', 'Commercial')
        ('R', 'Religious')
    )


class Role(models.Model):
    title = models.CharField(max_length=100)
    # Permissions TBD


# class User(AbstractUser):
#     # Placeholder to allow customization of User model in future
#     pass
