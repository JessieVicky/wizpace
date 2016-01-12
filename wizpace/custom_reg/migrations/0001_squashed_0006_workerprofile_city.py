# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shortuuidfield.fields
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    replaces = [(b'custom_reg', '0001_initial'), (b'custom_reg', '0002_auto_20150826_1150'), (b'custom_reg', '0003_auto_20150826_1244'), (b'custom_reg', '0004_auto_20150826_1246'), (b'custom_reg', '0005_workerprofile_country'), (b'custom_reg', '0006_workerprofile_city')]

    dependencies = [
        ('cities_light', '0004_auto_20150826_1150'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(unique=True, max_length=22, editable=False, blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('user', models.OneToOneField(related_name='client_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(unique=True, max_length=22, editable=False, blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('salary_amount', models.IntegerField(default=0, blank=True)),
                ('salary_currency', models.CharField(default=b'---', max_length=3, blank=True)),
                ('intro', models.TextField(max_length=1000, blank=True)),
                ('skills', models.ManyToManyField(to=b'custom_reg.Skill')),
                ('user', models.OneToOneField(related_name='worker_profile', to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(to='cities_light.Country', null=True)),
                ('city', models.ForeignKey(to='cities_light.City', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
