# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'custom_settings', '0001_initial'), (b'custom_settings', '0002_auto_20150721_1402'), (b'custom_settings', '0003_auto_20150721_1403'), (b'custom_settings', '0004_auto_20150721_1408'), (b'custom_settings', '0005_auto_20150721_1413')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(default=b'', max_length=30)),
                ('title', models.CharField(default=b'', max_length=30)),
                ('from_year', models.CharField(default=b'', max_length=8)),
                ('to_year', models.CharField(default=b'', max_length=8)),
                ('user', models.ForeignKey(related_name='experience', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(default=b'', max_length=30)),
                ('from_year', models.CharField(default=b'', max_length=8)),
                ('to_year', models.CharField(default=b'', max_length=8)),
                ('user', models.ForeignKey(related_name='education', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
