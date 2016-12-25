from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey("accounts.Organization")

    def __str__(self):
        return self.name + " of " + self.organization.name
