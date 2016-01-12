from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from account.signals import user_signed_up
from shortuuidfield import ShortUUIDField
from cities_light.models import City, Country

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class Skill(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name

class WorkerProfile(models.Model):
    uuid = ShortUUIDField(unique=True, editable=False)
    user = models.OneToOneField(User, related_name='worker_profile')

    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)

    salary_amount = models.IntegerField(blank=True, default=0)
    salary_currency = models.CharField(max_length=3, blank=True, default='---')

    city = models.ForeignKey(City, null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)

    intro = models.TextField(blank=True, max_length=1000)
    skills = models.ManyToManyField(Skill, blank=True)

    def __unicode__(self):
        return self.user.email

    @models.permalink
    def get_absolute_url(self):
        return ('profile_detail', [self.uuid])

    @models.permalink
    def get_portfolio_url(self):
        return ('profile_detail_portfolio', [self.uuid])

    @models.permalink
    def get_experience_url(self):
        return ('profile_detail_experience', [self.uuid])

class ClientProfile(models.Model):
    uuid = ShortUUIDField(unique=True)
    user = models.OneToOneField(User, related_name='client_profile')

    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)

    def __unicode__(self):
        return self.user.email

    @models.permalink
    def get_absolute_url(self):
        return ('profile_detail', [self.uuid])

@receiver(user_signed_up, sender=User)
def create_profile(user, form, **kwargs):
    if user:
        if form.cleaned_data['acc_type'] == u'work':
            WorkerProfile.objects.create(user=user)
        else:
            ClientProfile.objects.create(user=user)