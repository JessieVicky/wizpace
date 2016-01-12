# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(default=b'', max_length=30)),
                ('programme', models.CharField(default=b'', max_length=30)),
                ('from_year', models.CharField(default=b'', max_length=8)),
                ('to_year', models.CharField(default=b'', max_length=8)),
                ('user', models.ForeignKey(related_name='education', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
    ]
