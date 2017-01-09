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
    certifications = models.ManyToManyField("Certification")
    # certifications this organization awards or is interested in

class Role(models.Model):
    OWNER = 'Owner'
    ADMINISTRATOR = 'Administrator'
    COORDINATOR = 'Coordinator'
    INTERN = 'Intern'
    VOLUNTEER = 'Volunteer'
    TEMP = 'Temp'
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=2, choices=(
        ('O', OWNER),
        ('A', ADMINISTRATOR),
        ('C', COORDINATOR),
        ('I', INTERN),
        ('V', VOLUNTEER),
        ('T', TEMP),
    ))
    # Permissions TBD


class User(AbstractUser):
    photo = models.ImageField(upload_to='faces')
    # a photo of the User   ***** file field -need to intercept to shrink resolution; see caktus utility
    skills = models.ManyToManyField("Skill")
    #  a list of skills that this user has