# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0022_auto_20160525_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='id',
            field=models.IntegerField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
