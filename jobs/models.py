from django.db import models
from django.utils import timezone


# Create your models here.

class Job(models.Model):
    # this is a defined job, like "zoo docent" or "aquarium docent" or "office helper"
    title = models.CharField(max_length=255)
    requires_confirmation = models.BooleanField(default=False) #is the user allowed to sign up for this directly or must she apply / be approved?
    cancellation_until = models.DateTimeField(blank=True, null=True) #user can cancel until this cut-off, then needs approval
    skills_required = models.ManyToManyField("accomplishments.skill",null=True, blank=True)
    certs_required = models.ManyToManyField("accomplishments.certification",null=True, blank=True)

class Task(models.Model):
    # this is a particular job at a particular time with a given # users needed having given skills/certs
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    requires_confirmation = models.BooleanField(default=False) #is the user allowed to schedule herself or must she bid and wait for confirmation?
    job = models.ForeignKey(Job, null=True, blank=True)
    total_quantity = models.IntegerField() # how many volunteers are needed for this task at this time & location
    location = models.ForeignKey("mapping.Location",null=True, blank=True)
    volunteers = models.ManyToManyField("accounts.User",null=True, blank=True)

    skills_required = models.ManyToManyField("accomplishments.skill",null=True, blank=True, default=job.skills_required)
    # is this default cricket????

    certs_required = models.ManyToManyField("accomplishments.certification",null=True, blank=True)
    @property
    def quantity_available(self):
        return self.total_quantity - self.volunteers.count()



