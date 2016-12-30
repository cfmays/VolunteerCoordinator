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

class Location(models.Model):
    #this is a unique descriptor within an organization, like "zoo" or "aquarium" or "Philly branch"
    #opportunities may be available in multiple locations but a particular committment will be in a single location;
    #that is, volunteer X is committed to job Y in location Z
    title = models.CharField(max_length=100) #this should be a unique key field
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE) #do these cascade's need () after?


class Volunteer(models.Model):
    volunteer = models.OneToOneField(User, on_delete=models.CASCADE)
    # I see that AbstractUser is imported; will we use that instead of User?
    # describes a person
    # I would like to be able to store a photo of the User
    # need a "skills" list


class Task(models.Model)
    # this is a defined job, like "zoo docent" or "aquarium docent" or "office helper"
    title = models.CharField(max_length=100)
    requires_confirmation = models.BooleanField #is the user allowed to schedule herself or must she bid and wait for confirmation?
    cancellation_until = models.DateTimeField #user can cancel until this cut-off, then needs approval
    # need a "skills required" list

class Opportunity(models.Model):
    # this is a task offered at a particular location at a particular time
    title = models.CharField(max_length=100) #do we need this, or do we just use the Task title?
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    quantity_needed = models.IntegerField # how many volunteers are needed for this op at this time & location
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_time = models.DateTimeField
    end_time = models.DateTimeField



class Commitment(models.Model):
    # this is a particular volunteer signed up for a particular opportunity
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    confirmed = models.BooleanField
    cancelled = models.BooleanField



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
