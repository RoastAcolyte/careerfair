# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0051_auto_20160528_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='GPA',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
