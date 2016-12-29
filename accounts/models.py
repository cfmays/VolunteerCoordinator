from django.db import models
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    # Organization types/categories
    CHARITY = 'Charity'
    COMMERCIAL = 'Commercial'
    RELIGIOUS = 'Religious'
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=2, choices=(
        ('C', CHARITY),
        ('M', COMMERCIAL),
        ('R', RELIGIOUS),
    ))


class Role(models.Model):
    OWNER = 'Owner'
    ADMINISTRATOR = 'Administrator'
    COORDINATOR = 'Coordinator'
    INTERN = 'Intern'
    VOLUNTEER = 'Volunteer'
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=(
        ('O', OWNER),
        ('A', ADMINISTRATOR),
        ('C', COORDINATOR),
        ('I', INTERN),
        ('V', VOLUNTEER),
    ))
    # Permissions TBD


# class User(AbstractUser):
#     # Placeholder to allow customization of User model in future
#     pass
