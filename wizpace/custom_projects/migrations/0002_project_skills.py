# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_projects', '0001_initial'),
        ('custom_reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='custom_reg.Skill'),
            preserve_default=True,
        ),
    ]
