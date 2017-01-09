from django.db import models
from django.utils import timezone

class Certification_Award(models.Model):
    # an award of a cert to a particular user at a particular level
    TRAINEE = 'Trainee'
    NOVICE = 'Novice'
    COMPETENT = 'Competent'
    ADVANCED = 'Advanced'
    EXPERT = 'Expert'
    title = models.CharField(max_length=255)
    user = models.ForeignKey("User")
    date_awarded = models.DateField(default=timezone.now)
    organization = models.ForeignKey("accounts.Organization", null=True, blank=True)
    # the organization that awarded this certification
    confirmed_by = models.ForeignKey("accounts.User", null=True, blank=True)
    # the (higher level) user that authorized this certification
    certification = models.ForeignKey("Certification")
    level = models.CharField(max_length=2, choices= (
        ('T', TRAINEE),
        ('N', NOVICE),
        ('C', COMPETENT),
        ('A', ADVANCED),
        ('E', EXPERT),
    ))

    # proof documents -- do we want to allow user to upload them?
    #     just a list that a coordinator can tick off?

    @property
    def lapsed(self): # calculates whether the term has expired, unless term is null, then never lapses
        if self.term is None:
            return False
        else:
            return timezone.now > self.date_awarded + timezone.timedelta(days = self.certification.term)

class Certification(models.Model):
    # Certs that an org can award to a user; could be verification of a skill, completion of training,
    # could result from production of documents (eg red cross first aid, YMCA lifeguard)
    # These could be proprietary to an organization (eg Herpetology Lab Animal Ambassador)
    title = models.CharField(max_length=255)
    term = models.IntegerField(blank=True, null=True)
    # the length of certification, in days; null === cert is valid forever
    is_proprietary = models.BooleanField(default=True)
    # whether this skill is particular to this org, say 'herp lab docent' or is general, like sewing or welding
    skills_required = models.ManyToManyField("Skill") # a list of skills required to achieve this cert; could
    #only be one to create an org-specific sign-off of a general skill

class Skill(models.Model):
    TRAINEE = 'Trainee'
    NOVICE = 'Novice'
    COMPETENT = 'Competent'
    ADVANCED = 'Advanced'
    EXPERT = 'Expert'
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=2, choices= (
        ('T', TRAINEE),
        ('N', NOVICE),
        ('C', COMPETENT),
        ('A', ADVANCED),
        ('E', EXPERT),
    )) # levels modified from https://hr.od.nih.gov/workingatnih/competencies/proficiencyscale.htm
