from django.db import models
from django.contrib.auth.models import User

class WorkExperience(models.Model):
    user = models.ForeignKey(User, related_name='experience')
    company = models.CharField(max_length=30, default='')
    title = models.CharField(max_length=30, default='')
    from_year = models.CharField(max_length=8, default='')
    to_year = models.CharField(max_length=8, default='')

    def __unicode__(self):
        return self.company

class Education(models.Model):
    user = models.ForeignKey(User, related_name='education')
    school = models.CharField(max_length=30, default='')
    programme = models.CharField(max_length=30, default='')
    from_year = models.CharField(max_length=8, default='')
    to_year = models.CharField(max_length=8, default='')

    def __unicode__(self):
        return self.school