from django.db import models
from django.utils import timezone


# Create your models here.

class Job(models.Model):
    # this is a defined job, like "zoo docent" or "aquarium docent" or "office helper"
    title = models.CharField(max_length=255)
    requires_confirmation = models.BooleanField(default=False) #is the user allowed to schedule herself or must she bid and wait for confirmation?
    cancellation_until = models.DateTimeField(blank=True, null=True) #user can cancel until this cut-off, then needs approval
    # need a "skills required" list

class Task(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    job = models.ForeignKey(Job, null=True, blank=True)
    quantity_needed = models.IntegerField() # how many volunteers are needed for this op at this time & location
    location = models.ForeignKey("mapping.Location")
    volunteers = models.ManyToManyField("accounts.User")


