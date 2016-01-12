# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_projects', '0005_auto_20150826_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='custom_reg.Skill', blank=True),
            preserve_default=True,
        ),
    ]
