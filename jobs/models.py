from django.db import models
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    # Location to be added after location table created
