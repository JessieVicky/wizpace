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
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=20)),
                ('description', models.CharField(default=b'', max_length=500)),
                ('nr_of_workers', models.IntegerField(null=True)),
                ('post_date', models.DateField(auto_now_add=True, null=True)),
                ('end_date', models.DateField(null=True)),
                ('owner', models.ForeignKey(related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
