from django.db import models
from django.contrib.auth.models import User

from custom_reg.models import Skill

class Project(models.Model):
    owner = models.ForeignKey(User, related_name='projects')
    title = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=500, default='')
    skills = models.ManyToManyField(Skill, blank=True)
    nr_of_workers = models.IntegerField(null=True)

    post_date = models.DateField(auto_now_add=True, null=True)
    end_date = models.DateField(null=True)

    def __unicode__(self):
        return self.owner.first_name + ", " + self.title