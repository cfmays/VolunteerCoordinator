from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class Certification(models.Model):
    # Certs that an org can award to a user; could be verification of a skill, completion of training,
    # could result from production of documents (eg red cross first aid, YMCA lifeguard)
    # These could be proprietary to an organization (eg Herpetology Lab Animal Ambassador)
    title = models.CharField(max_length=255)
    date_awarded = models.DateField(default=datetime.date.today)
    term = models.IntegerField(blank=True, null=True)
    # the length of certification, in days; null == cert is valid forever
    is_proprietary = models.BooleanField(default=True)
    # whether this skill is particular to this org, say 'herp lab docent' or is general, like sewing or welding
    skills_required = models.ManyToManyField("Skill") # a list of skills required to achieve this cert; could
    #only be one to create an org-specific sign-off of a general skill
    @property
    def lapsed(self): # calculates whether the term has expired, unless term is null, then not lapsed
        if self.term is None:
            return False
        else:
            return datetime.date.today > self.date_awarded + datetime.timedelta(days = self.term)
            #is this OK or do I need () after datetime.date.today ???

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
    certifications = models.ManyToManyField("Certification")#date,expire date,proof documents (nullable)

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

class Skill(models.Model): # modified from https://hr.od.nih.gov/workingatnih/competencies/proficiencyscale.htm
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
    ))



class User(AbstractUser):
    photo = models.ImageField(upload_to='faces')
    # a photo of the User   ***** file field -need to intercept to shrink resolution; see caktus utility
    skills = models.ManyToManyField("Skill")
    #  a list of skills that this user has