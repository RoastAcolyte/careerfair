# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0010_auto_20160524_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(blank=True, upload_to='resumes'),
        ),
    ]
