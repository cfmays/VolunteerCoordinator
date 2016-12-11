from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)


class Role(models.Model):
    title = models.CharField(max_length=100)
    # Permissions TBD