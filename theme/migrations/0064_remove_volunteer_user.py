# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0063_volunteer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='user',
        ),
    ]
