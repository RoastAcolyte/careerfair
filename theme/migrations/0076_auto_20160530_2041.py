# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0075_companyrep_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='alumni_reps',
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='alumni_reps',
            field=models.TextField(default=''),
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='reps',
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='reps',
            field=models.TextField(default=''),
        ),
    ]
