from django.db import models


# Create your models here.
class Location(models.Model):
    # this is a unique descriptor within an organization, like "zoo" or "aquarium" or "Philly branch"
    # opportunities may be available in multiple locations but a particular committment will be in a single location;
    # that is, volunteer X is committed to job Y in location Z
    title = models.CharField(max_length=255)
    organization = models.ForeignKey("accounts.Organization")
    def __str__(self):
        return self.name + " of " + self.organization.name
    class Meta:
        unique_together = (("title", "organization"),)
