# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0020_auto_20160525_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='company_uid',
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='id',
            field=models.IntegerField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
