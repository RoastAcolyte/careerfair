# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0050_auto_20160528_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='resume',
            field=models.FileField(blank=True, upload_to='resumes'),
        ),
    ]
