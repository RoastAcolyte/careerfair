# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0108_auto_20160614_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyrep',
            name='company',
            field=models.CharField(max_length=60, null=True),
        ),
    ]